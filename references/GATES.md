# AEON-LORN-15X Gates

## Mode honesty

Dry-run allowed verbs: planned, simulated, would-push, would-create, apply=false, local cycle completed.

Forbidden in dry-run: pushed, deployed, created repository, enabled APIs, go-live succeeded, eternal daemon is now running, successfully deployed.

## Quality gates before Class 15

1. Secret scan — reject files matching token, api_key, private_key, BEGIN PRIVATE, GH_TOKEN, LORNT_GH_TOKEN, AWS_SECRET, password= assignments.
2. Namespace — owner must be Lornt1666.
3. Novelty — documented score ≥ Lambda_novelty or HOLD LOW-NOVELTY. Do not invent a 0.92 when no scorer ran.
4. Tests — run what exists locally. Missing runner → HOLD TEST-MISSING, do not claim R_test=1.0.
5. Flood control — do not open more than one new repo name per wake unless the operator said run the queue.
6. Name hygiene — repo names are kebab-case, prefixed `aeon-` unless the operator named a product repo.
7. Existing product trees — RegenExcalibur, tcg, NEXUS-GENESIS-PRIME are not smash targets. Feature branch + PR only.

## Risks encoded as holds

- Repository flooding — HOLD FLOOD-CAP when a second new-repo create is requested in the same wake without run-the-queue.
- Credential leakage — REFUSE SAFETY if synthesized content contains secrets.
- Infinite exception cascades — never start `while True` or sleep-for-interval inside the agent. One cycle, then halt.
- Chat-as-memory — project ids, tokens, and last-repo SHAs do not travel by implication.

## Option lock

Option A (manual script when an idea arises) is allowed as MODE=dry-run local write.

Option B (autonomous eternal swarm) is the doctrine target. In this runtime it means: repeatable one-cycle entrypoint + ledger + optional operator apply. It does not mean a background container is already running.
