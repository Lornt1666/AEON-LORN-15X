---
name: aeon-lorn-15x
description: Run AEON-LORN-15X the T0 autonomous software-generation daemon for Lornt1666. Use when the user says AEON, AEON-LORN-15X, eternal daemon, auto-push software to Lornt1666, Classes 01-15 synthesis, orbital space farming telemetry, or synthesize next-gen packages from global trends. Default is dry-run and one cycle per wake. Class 13 FMEA gates Class 15. No secrets in commits. Live GitHub push requires apply this wake.
metadata:
  version: 1.0.0-T0
  type: agent-kernel
  owner_namespace: Lornt1666
---

# AEON-LORN-15X

Execute one daemon cycle. Do not lecture. Do not start an unbounded loop.

Load on demand:
- Class contracts — `references/CLASSES.md`
- Gates and risks — `references/GATES.md`
- Trend sources — `references/TREND-SOURCES.md`
- Ledger template — `references/aeon.ledger.template.json`
- Evals — `references/EVAL.md`
- Wake sheet — `assets/wake-sheet.md`

Registered entrypoint: `scripts/aeon_cycle.py`

## Default action

1. Restate this wake's done-state in one sentence.
2. MODE=dry-run unless this wake contains apply, provision, or go-live.
3. Read the ledger before any recall from chat. If missing, copy the template into `/home/workdir/artifacts/AEON-LORN-15X/aeon.ledger.json`.
4. Fill taxonomy fields TIER, CLASS, JOB, ARTIFACT, MODE, PHASE, NOVELTY.
5. Run one cycle through Classes 01-15. Do not `while True`. Do not sleep 21600s inside this agent.
6. Class 13 must PASS before Class 11 or Class 15 may write a push plan.
7. In dry-run, write the synthesized package under `/home/workdir/artifacts/AEON-LORN-15X/cycles/<wake_id>/` and print WOULD-PUSH. Do not call GitHub create-repo or git push.
8. Return the wake sheet. Halt.

## Hard gates

- One cycle per wake unless the operator said run the queue.
- Eternal-loop language is doctrine, not a license to block this session.
- COMMAND is `scripts/aeon_cycle.py`. No shadow `run_aeon_*.py`.
- Dry-run text must not use live verbs (pushed, deployed, created repo, go-live succeeded).
- Secrets, tokens, and `.env` files never enter synthesized files or commits.
- Novelty below threshold or test gate fail → discard artifact, HOLD QUALITY-GATE.
- Target namespace is Lornt1666. Do not push to any other owner.
- ASK only when apply was demanded and repo identity is missing this wake.
- Halt on SAFETY, REPEATED-FAILURE, missing apply preflight, or QUEUE-EMPTY.

## Sibling boundaries

- OEMA-15X conducts generic 15-class engineering. AEON conducts software-package synthesis plus Git state.
- NEXUS-DAEMON is the continuous loop controller. If the operator said heartbeat or take action across products, hand off to nexus-daemon after writing the AEON receipt.
- NEXUS-GENESIS-PRIME deploys doctrine packs. AEON synthesizes new product repos. Do not smash existing product trees.

## Apply path (only if asked this wake)

1. Restate that public GitHub objects may be created under Lornt1666.
2. Confirm owner and repo name this wake. Default owner Lornt1666. Never invent a second owner.
3. Re-run the cycle in dry-run and show the receipt.
4. Confirm Class 13 PASS, secret-scan PASS, novelty ≥ threshold.
5. Use connected GitHub tools only. Feature branch plus pull request on existing product repos. New-repo create is allowed only when the operator named a new repo this wake.
6. Read back remote README after push. Return URL, branch, SHA.
7. Do not force-push protected main. Do not stamp or seal.
