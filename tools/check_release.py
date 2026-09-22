#!/usr/bin/env python3
"""
check_release.py: release consistency check for the definition-of-done repository.

Run from anywhere:  python3 tools/check_release.py [repo-root]
Exit 0 when every check passes, 1 when any fails, 2 when a check could not run.
It reads. It never writes.

What it checks, and why each check exists:

  1. Version and date lockstep. The README version table is the reference. The README How to
     Cite block, the newest CHANGELOG.md entry and CITATION.cff must carry the same version, and
     the dates must agree. CHANGELOG.md v1.1.2 records How to Cite lagging the README by a
     release, found by reading and not by a guard; this is the guard.
  2. Companion mastheads. Every markdown file other than README.md, CHANGELOG.md and LICENSE.md
     carries "Part of [...](README.md) | vX.Y.Z | CC BY-NC-SA 4.0". That version names the release
     in which the file's substance last changed (CHANGELOG.md, Versioning). So the named release
     must exist in CHANGELOG.md and must not exceed the README version, and a companion changed
     since the last tag, or changed in the working tree, must name the README version. The last
     part needs git and is reported NOT CHECKED without it.
  3. Internal links and heading anchors, outside fenced code blocks, in every markdown file. A
     link to a file that is not there, or to a heading that is not there, is a defect.
  4. Dates. Every CHANGELOG.md entry heading is "## vX.Y.Z (YYYY-MM-DD)" with a real date, the
     entries run in descending version order and no entry is dated after the README release.
  5. Cross-file consistency of the things the v1.1.2 review found inconsistent: the README tier
     table's test counts against the template's Section A heading; the Kitchen version pinned in
     the README's governing-versions table against both templates' "Kitchen version applied"
     fields; each template's stated instrument version against its own masthead.
  6. House style. Every markdown file except LICENSE.md ends with the closing line and contains
     no em dash.

A check that cannot find its input reports a failure, never a pass (a guard that cannot run
must not report safety).
"""
import datetime
import os
import re
import sys

CLOSING = "**Final Liability rests with the Human.**"
MASTHEAD = re.compile(
    r"^Part of \[The Definition of Done Is the Work of the Human\]\((?:\.\./)?README\.md\) \| v(\d+\.\d+\.\d+) \| CC BY-NC-SA 4\.0",
    re.M)
MD_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^\s*(```|~~~)")
SKIP_MASTHEAD = {"README.md", "CHANGELOG.md", "LICENSE.md"}

failures = []
notes = []


def fail(msg):
    failures.append(msg)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def fenced_lines(lines):
    """1-based line numbers inside fenced code blocks, fence lines included."""
    inside = set()
    open_fence = None
    for i, line in enumerate(lines, 1):
        m = FENCE.match(line)
        if m:
            if open_fence is None:
                open_fence = m.group(1)
                inside.add(i)
                continue
            if m.group(1) == open_fence:
                inside.add(i)
                open_fence = None
                continue
        if open_fence is not None:
            inside.add(i)
    return inside


def slug(heading):
    """GitHub-style anchor: strip emphasis, lowercase, keep letters, digits, spaces and hyphens,
    then spaces to hyphens."""
    h = re.sub(r"[*_`]", "", heading).strip()
    h = h.lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def headings(text):
    out = []
    lines = text.splitlines()
    inside = fenced_lines(lines)
    for i, line in enumerate(lines, 1):
        if i in inside:
            continue
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if m:
            out.append(slug(m.group(1)))
    return out


def vtuple(v):
    return tuple(int(x) for x in v.split("."))


def valid_date(s):
    try:
        datetime.date.fromisoformat(s)
        return True
    except ValueError:
        return False


def changed_since_release(root):
    """Repository-relative paths changed since the latest vX.Y.Z tag or in the working tree.
    None when git is unavailable; the caller reports NOT CHECKED rather than passing."""
    import subprocess

    def git(*args):
        r = subprocess.run(["git", "-C", root] + list(args), capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(r.stderr.strip())
        return r.stdout

    try:
        git("rev-parse", "--is-inside-work-tree")
        names = set()
        for line in git("status", "--porcelain").splitlines():
            if len(line) > 3:
                names.add(line[3:].strip().strip('"'))
        tags = [t for t in git("tag", "--list").split() if re.fullmatch(r"v\d+\.\d+\.\d+", t)]
        if tags:
            latest = max(tags, key=lambda t: vtuple(t[1:]))
            for line in git("diff", "--name-only", latest, "HEAD").splitlines():
                names.add(line.strip())
        return names
    except (RuntimeError, FileNotFoundError, OSError):
        return None


def md_files(root):
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", ".github")]
        for fn in filenames:
            if fn.endswith(".md"):
                out.append(os.path.join(dirpath, fn))
    return sorted(out)


def main(root):
    root = os.path.abspath(root)
    readme_p = os.path.join(root, "README.md")
    if not os.path.exists(readme_p):
        print(f"FAIL: {readme_p} not found; nothing checked")
        return 2
    readme = read(readme_p)

    # ---- 1. version and date lockstep ---------------------------------------------------
    m = re.search(r"^\| v(\d+\.\d+\.\d+) \| (\d{4}-\d{2}-\d{2}) \(KST\) \| (\w+) \| ", readme, re.M)
    ver = iso = None
    if not m:
        fail("README.md: version table row not found in the form '| vX.Y.Z | YYYY-MM-DD (KST) | Status | ...'")
    else:
        ver, iso = m.group(1), m.group(2)
        if not valid_date(iso):
            fail(f"README.md: version table date {iso} is not a real date")
        notes.append(f"README release v{ver} · {iso} · {m.group(3)}")

    entries = []
    cl_p = os.path.join(root, "CHANGELOG.md")
    if ver:
        cm = re.search(r"^## How to Cite\s*\n(.*?)(?=^## |\Z)", readme, re.M | re.S)
        if not cm:
            fail("README.md: How to Cite section not found")
        else:
            cited = set(re.findall(r"\bv(\d+\.\d+\.\d+)\b", cm.group(1)))
            if cited != {ver}:
                fail(f"README.md: How to Cite carries {sorted(cited) or 'no version'}, version table is v{ver}")

        cff_p = os.path.join(root, "CITATION.cff")
        if not os.path.exists(cff_p):
            fail("CITATION.cff: missing")
        else:
            cff = read(cff_p)
            vm = re.search(r"^version:\s*[\"']?v?([0-9][^\s\"']*)", cff, re.M)
            dm = re.search(r"^date-released:\s*[\"']?(\d{4}-\d{2}-\d{2})", cff, re.M)
            if not vm:
                fail("CITATION.cff: no version line")
            elif vm.group(1) != ver:
                fail(f"CITATION.cff: version {vm.group(1)} differs from README v{ver}")
            if not dm:
                fail("CITATION.cff: no date-released line")
            elif dm.group(1) != iso:
                fail(f"CITATION.cff: date-released {dm.group(1)} differs from README date {iso}")

        if not os.path.exists(cl_p):
            fail("CHANGELOG.md: missing")
        else:
            cl = read(cl_p)
            for hm in re.finditer(r"^## v(\d+\.\d+\.\d+) \((\d{4}-\d{2}-\d{2})\)\s*$", cl, re.M):
                entries.append((hm.group(1), hm.group(2)))
            bad = [l for l in cl.splitlines() if l.startswith("## v")
                   and not re.match(r"^## v\d+\.\d+\.\d+ \(\d{4}-\d{2}-\d{2}\)\s*$", l)]
            for l in bad:
                fail(f"CHANGELOG.md: entry heading not in the form '## vX.Y.Z (YYYY-MM-DD)': {l!r}")
            if not entries:
                fail("CHANGELOG.md: no entry heading in the form '## vX.Y.Z (YYYY-MM-DD)'")
            else:
                if entries[0][0] != ver:
                    fail(f"CHANGELOG.md: newest entry v{entries[0][0]} differs from README v{ver}")
                if entries[0][1] != iso:
                    fail(f"CHANGELOG.md: newest entry date {entries[0][1]} differs from README date {iso}")

    # ---- 4. dates (run here so the entries list is in hand) ----------------------------
    if entries:
        for v, d in entries:
            if not valid_date(d):
                fail(f"CHANGELOG.md: v{v} is dated {d}, not a real date")
            elif iso and valid_date(iso) and datetime.date.fromisoformat(d) > datetime.date.fromisoformat(iso):
                fail(f"CHANGELOG.md: v{v} is dated {d}, after the README release date {iso}")
        vs = [vtuple(v) for v, _ in entries]
        if vs != sorted(vs, reverse=True):
            fail("CHANGELOG.md: entries are not in descending version order")
        if len(set(vs)) != len(vs):
            fail("CHANGELOG.md: duplicate entry versions")
        notes.append(f"CHANGELOG entries: {len(entries)}, oldest v{entries[-1][0]} ({entries[-1][1]})")

    # ---- 2. companion mastheads ----------------------------------------------------------
    files = md_files(root)
    if not files:
        fail("no markdown files found under the repository root")
    entry_versions = {v for v, _ in entries}
    changed = changed_since_release(root)
    companions = [p for p in files if os.path.basename(p) not in SKIP_MASTHEAD]
    if not companions:
        fail("no companion markdown files found")
    hit = []
    for p in companions:
        rel = os.path.relpath(p, root)
        text = read(p)
        pm = MASTHEAD.search(text)
        if not pm:
            fail(f"{rel}: no masthead 'Part of [The Definition of Done Is the Work of the Human](README.md) | vX.Y.Z | CC BY-NC-SA 4.0'")
            continue
        cver = pm.group(1)
        if entries and cver not in entry_versions:
            fail(f"{rel}: masthead names v{cver}, which has no CHANGELOG.md entry")
        if ver and vtuple(cver) > vtuple(ver):
            fail(f"{rel}: masthead names v{cver}, later than the README v{ver}")
        if changed is not None and ver and rel in changed:
            hit.append(rel)
            if cver != ver:
                fail(f"{rel}: changed since the last release but its masthead names v{cver}, not v{ver}")
    if changed is None:
        notes.append(f"companions checked: {len(companions)}; changed-since-release test NOT CHECKED (no git history available)")
    else:
        notes.append(f"companions checked: {len(companions)}; changed since the last release: {len(hit)}"
                     + (f" ({', '.join(hit)})" if hit else ""))

    # ---- 3. internal links and anchors ---------------------------------------------------
    heading_cache = {}
    link_count = 0
    for p in files:
        text = read(p)
        lines = text.splitlines()
        inside = fenced_lines(lines)
        for i, line in enumerate(lines, 1):
            if i in inside:
                continue
            for target in MD_LINK.findall(line):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                link_count += 1
                file_part, _, anchor = target.partition("#")
                if file_part:
                    tp = os.path.normpath(os.path.join(os.path.dirname(p), file_part))
                    if not os.path.exists(tp):
                        fail(f"{os.path.relpath(p, root)}:{i}: link target not found: {file_part}")
                        continue
                else:
                    tp = p
                if anchor:
                    if not tp.endswith(".md"):
                        fail(f"{os.path.relpath(p, root)}:{i}: anchor on a non-markdown target: {target}")
                        continue
                    if tp not in heading_cache:
                        heading_cache[tp] = headings(read(tp))
                    if anchor not in heading_cache[tp]:
                        fail(f"{os.path.relpath(p, root)}:{i}: anchor #{anchor} not found in {os.path.relpath(tp, root)}")
    notes.append(f"internal links checked: {link_count} across {len(files)} markdown files")

    # ---- 5. cross-file consistency -------------------------------------------------------
    tier_row = re.search(r"^\| Pass or fail tests \(Section A\) \| (.+?) \| (.+?) \| (.+?) \|", readme, re.M)
    if not tier_row:
        fail("README.md: tier table row '| Pass or fail tests (Section A) | ... |' not found")
    dod_p = os.path.join(root, "templates", "definition-of-done-template.md")
    cr_p = os.path.join(root, "templates", "confirmation-record-template.md")
    if not os.path.exists(dod_p):
        fail("templates/definition-of-done-template.md: missing")
    elif tier_row:
        dod = read(dod_p)
        hm = re.search(r"^## Section A\. Pass or Fail Tests \((.+?)\)", dod, re.M)
        if not hm:
            fail("definition-of-done-template.md: Section A heading with its test counts not found")
        else:
            t1 = tier_row.group(1).replace(" to ", " to ")
            t2 = tier_row.group(2)
            heading_counts = hm.group(1)
            if not (t2 in heading_counts and t1 in heading_counts):
                fail(f"definition-of-done-template.md: Section A heading '({heading_counts})' does not carry the README tier table counts "
                     f"('{t2}' for Tier 2 and 3, '{t1}' for Tier 1)")
            else:
                notes.append(f"tier test counts agree: Tier 1 {t1}, Tier 2 and 3 {t2}")
    km = re.search(r"^\| \[Slow AI Kitchen\]\([^)]+\) \| v(\d+\.\d+\.\d+) \((\d{4}-\d{2}-\d{2}), KST\) \|", readme, re.M)
    if not km:
        fail("README.md: governing-versions row for the Slow AI Kitchen not found")
    else:
        kver = km.group(1)
        tm = re.search(r"\(v(\d+\.\d+\.\d+), Tier Application Map\)", readme)
        if not tm:
            fail("README.md: tier table paragraph does not name the Kitchen version '(vX.Y.Z, Tier Application Map)'")
        elif tm.group(1) != kver:
            fail(f"README.md: tier table names Kitchen v{tm.group(1)}, governing-versions table names v{kver}")
        for tp in (dod_p, cr_p):
            if not os.path.exists(tp):
                fail(f"{os.path.relpath(tp, root)}: missing")
                continue
            t = read(tp)
            fm = re.search(r"^\| Kitchen version applied[^|]*\| Slow AI Kitchen v(\d+\.\d+\.\d+) \|", t, re.M)
            if not fm:
                fail(f"{os.path.relpath(tp, root)}: 'Kitchen version applied' field not found")
            elif fm.group(1) != kver:
                fail(f"{os.path.relpath(tp, root)}: Kitchen version applied v{fm.group(1)} differs from README v{kver}")
            im = re.search(r"^\| Instrument version \| (?:Definition of Done template|Confirmation Record template) v(\d+\.\d+\.\d+) \|", t, re.M)
            mh = MASTHEAD.search(t)
            if not im:
                fail(f"{os.path.relpath(tp, root)}: 'Instrument version' field not found")
            elif mh and im.group(1) != mh.group(1):
                fail(f"{os.path.relpath(tp, root)}: Instrument version v{im.group(1)} differs from the file's masthead v{mh.group(1)}")
            mm = re.search(r"^\| Method version[^|]*\| definition-of-done v \|", t, re.M)
            if not mm:
                fail(f"{os.path.relpath(tp, root)}: 'Method version' field must be the blank 'definition-of-done v', filled by the user from the README")
        notes.append(f"Kitchen version pinned: v{kver}, consistent across README and both templates")

    # ---- 6. house style ------------------------------------------------------------------
    for p in files:
        rel = os.path.relpath(p, root)
        if os.path.basename(p) == "LICENSE.md":
            continue
        text = read(p)
        last = [l for l in text.splitlines() if l.strip()]
        if not last or last[-1].strip() != CLOSING:
            fail(f"{rel}: last non-empty line is not the closing line {CLOSING}")
        for i, line in enumerate(text.splitlines(), 1):
            if "—" in line:
                fail(f"{rel}:{i}: em dash")
    notes.append("house style: closing line and em-dash check run on every markdown file except LICENSE.md")

    # ---- report ------------------------------------------------------------------------------
    for n in notes:
        print(f"  note: {n}")
    if failures:
        print(f"\nFAIL ({len(failures)}):")
        for f_ in failures:
            print(f"  - {f_}")
        return 1
    print("\nPASS: every check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))
