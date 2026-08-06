# Metric contract

| Event | Required properties | Purpose |
| --- | --- | --- |
| `account_created` | `account_id`, `created_at`, `acquisition_channel` | Experiment eligibility |
| `checklist_viewed` | `account_id`, `variant`, `step_count` | Exposure validation |
| `workflow_completed` | `account_id`, `workflow_type`, `completed_at` | Primary conversion |
| `support_contact_created` | `account_id`, `category`, `created_at` | Support guardrail |

The analysis window is 24 hours from `account_created`. Deduplicate events by `account_id` and use the variant assigned at first exposure.
