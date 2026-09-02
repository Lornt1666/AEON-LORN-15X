# AEON-LORN-15X Class Contracts

Each class returns PASS, HOLD, or REFUSE. Print is not proof.

| ID | Domain | Function | May mutate | Halt if |
|---|---|---|---|---|
| 01 | Core governance | Mode lock, token isolation, wake_id, owner=Lornt1666 | ledger read | axioms missing |
| 02 | Trend scraper | Ingest arXiv, GitHub trending, web signals for space-ag, automation, quantum-ready pipelines | read-only net | apply=true and sources empty |
| 03 | Methodology | Choose architecture pattern (services, actor, contract, batch) with warrant | none | no warrant |
| 04 | Research rigor | Novelty score vs existing Lornt1666 repos, duplication check, hallucination prune | none | invented papers |
| 05 | Parametric | Scale complexity, file depth, dependency map | none | unbounded deps |
| 06 | Heuristics | Prune low-leverage concepts | none | prune with no rule |
| 07 | Computational | Algorithms, models, simulation scripts | file write in cycle dir | unregistered solver claimed as verified |
| 08 | Systems | Data flow, API schema, container config | file write in cycle dir | missing required subsystem |
| 09 | Architecture | Full-stack scaffold (Python, Rust, TypeScript, Dockerfile) | file write in cycle dir | layout contradicts map |
| 10 | Generative | N_variants parallel packages, 1 to 5 | file write in cycle dir | variant with no fitness metric |
| 11 | Automation | CI/CD loop spec, exception contract, self-heal plan | file write after Class 13 PASS | FMEA not PASS |
| 12 | Procurement | Named APIs and deps only. No live buy | read-only | live purchase without apply |
| 13 | Risk / FMEA | Lint, unit-test plan, secret scan, vuln scan, RPN | none | RPN gate fail or secret hit |
| 14 | Project evolution | Semver, changelog, local ledger delta | ledger write | cycle graph or missing class |
| 15 | Output and Git | Commit plan and push execution | GitHub only when MODE=apply | Class 13 not PASS, dry-run live verb, wrong owner |

Dependency edges:

```
01 → 02 → 03 → 04 → 05 → 06 → 08 → 09 → 10
                ↘ 13 ↗           ↗
05 → 07 → 13 → 11
13 → 12
13 + 14 → 15
```

Class 15 may not claim repo-ready unless MODE=apply and GATES all PASS.

## Key variables

- T_interval — doctrine poll interval. Not executed inside this agent wake.
- N_variants — parallel architectures per cycle, 1 to 5. Default 1.
- Lambda_novelty — minimum novelty to keep an artifact. Default 0.85. Score is a documented heuristic, not a measured embedding unless a scorer exists.
- R_test — required local checks before WOULD-PUSH. Default all declared checks PASS. Do not claim 100% coverage without a runner report.
- Omega_repo — owner namespace Lornt1666.
