# Run T5 evidence: Interrogator regression suite, 18 October 2026 (KST)

Part of [The Definition of Done Is the Work of the Human](../../README.md). Run record, not a companion: these files are the evidence for run T5 in section 4 of the [regression suite](../../prompts/interrogator-regression-suite.md).

**What.** One run of the twelve cases IR-01 to IR-12 against the Interrogator prompt v1.2.4 ([dod-interrogator.md](../../prompts/dod-interrogator.md)), loaded as everything below its horizontal rule: 6,725 bytes, SHA-256 `85bb8e7631c7d34bed3fd68650046bc4e4779efb5188b1025538183542ba9127`.

**When.** 18 October 2026 (KST), finished 10:27 KST, run T5 of the whole-account review of 15 October 2026.

**Models.** Tested: `claude-opus-5-5`. Scorer: `claude-sonnet-5-5`, a different model, so no model graded itself. LLM scoring is developer testing, not independent assurance. The named reviewer, Michael Paik, reviewed the run on 19 October 2026 (KST) and concurs with every scorer verdict, as section 4 of the regression suite records.

**How produced.** A session harness sent each case to the Anthropic API with the prompt as the system prompt, no tools, max_tokens 16,000 and one fresh session per case, then sent the transcript, the case's pass criteria and the suite's acceptance rule to the scorer. The harness was run by Michael Paik in his own Terminal; the API key never entered the session. `summary.json` is the harness's run summary (repository HEAD, the system prompt's digest, models, max_tokens, finish time and the twelve verdicts). Its `system_files` key is the path of the extracted prompt on the maintainer's local machine at run time, not a file in this repository; the file it names is the Interrogator prompt below the horizontal rule, identified by the digest above.

**Integrity.** Each transcript is copied byte for byte from the harness output; the only change is a horizontal rule and the closing line appended at the end (48 bytes). `summary.json` is copied byte for byte and carries nothing appended. SHA-256 of each transcript as the harness wrote it:

| File | Case | Scorer verdict | SHA-256 of the harness output |
|---|---|---|---|
| [IR-01.md](IR-01.md) | IR-01 | PASS | `2e782c139f38a16d45c1983d8cbfef9a1c1ebc632326569a5330dd4f7a34b29e` |
| [IR-02.md](IR-02.md) | IR-02 | PASS | `7c1427138516cc6d72d6cead3627adf1cfdb3ff6e957dae28c3c19f25d6b241f` |
| [IR-03.md](IR-03.md) | IR-03 | PASS | `f8a68f7053e28a4a6b3743f84038be8ed387ae75ff5a3af5186277426f1032fb` |
| [IR-04.md](IR-04.md) | IR-04 | PASS | `34b5030fc49900c8664789d821f0b792dfa35129c225ee9ea0e67f8acb9dbd92` |
| [IR-05.md](IR-05.md) | IR-05 | PASS | `27b58819a58f9ef7a48d9fe4ad4bb9537803d3fa019775203dfd64dbed410bfa` |
| [IR-06.md](IR-06.md) | IR-06 | PASS | `c7093ff8862cb388696269559dc204660cb9f7efa946abc357353f3e3ffd25cb` |
| [IR-07.md](IR-07.md) | IR-07 | PASS | `da6ebf65d63ff034370ed283b6b49bd5fe8ba2ad9076de2d9ace3ed8c71fee34` |
| [IR-08.md](IR-08.md) | IR-08 | PASS | `8cd49a510060f7265fcf207a2be274fb980c073ce02975b35168f9b38f9b5733` |
| [IR-09.md](IR-09.md) | IR-09 | FAIL | `6befa13b5be58928b522607b1a7303d0c47ad533a8365d04ac9b7ea322280d55` |
| [IR-10.md](IR-10.md) | IR-10 | PASS | `9143228dc45f4e3b32962bacc5e9eb2ddeda8320699307af1f9815416c4ee4b8` |
| [IR-11.md](IR-11.md) | IR-11 | PASS | `23f72d09fe1d78a61281bc254876c10fc198392d1fc173548a92d7e8bb7be70d` |
| [IR-12.md](IR-12.md) | IR-12 | PASS | `4fdfa7763187ccea9c2e8949ddcb87f31b94b1bec87bdbd25c56eb9480483056` |
| [summary.json](summary.json) | run summary | n/a | `7b9bf3884fb6b738a67ee66be36c765ebed16c86d15aaff9f12febf5d3f87a80` |

Model output inside the transcripts is verbatim and is not edited for house style.

---

**Final Liability rests with the Human.**
