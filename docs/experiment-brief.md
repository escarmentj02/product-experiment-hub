# Experiment brief: clearer activation checklist

## Problem

New users complete account setup but often fail to reach their first successful workflow in the first session.

## Hypothesis

Showing a short, state-aware checklist after setup will increase first-workflow completion without raising support contact rate.

## Scope

Target newly created self-serve accounts on web. Exclude invited enterprise users and accounts with existing setup activity.

## Primary metric

First-workflow completion within 24 hours of account creation.

## Guardrails

- Support contacts per activated account must not rise more than 5%.
- Page-load p95 must remain within 100 ms of control.
- No material decline in completion for accessibility-tool users.

## Decision rule

Launch if the primary metric has a statistically distinguishable positive movement, each guardrail remains within limit, and qualitative feedback reveals no high-severity usability issue. Otherwise iterate or stop.
