# Product Experiment Hub

A product decision toolkit containing a concise experiment brief, metric definitions, and a statistical guardrail calculator for two-variant conversion experiments.

## Contents

- [`docs/experiment-brief.md`](docs/experiment-brief.md): problem framing, hypothesis, scope, and decision rules.
- [`docs/metrics.md`](docs/metrics.md): event taxonomy and guardrails.
- `analyze.py`: dependency-free conversion-rate analysis with a two-proportion z-test approximation.

## Run

```powershell
python analyze.py --control-conversions 482 --control-visitors 8000 --treatment-conversions 535 --treatment-visitors 8050
```

Use the result alongside the guardrail and qualitative checks defined in the brief; do not use a p-value in isolation as a launch decision.
