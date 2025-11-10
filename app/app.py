Step 3: Workflow Implementation

Every time you commit, GitHub Actions:

Runs your build & test stages.

Deploys automatically if tests pass.

To simulate real-world scenarios:

Introduce a syntax error in your code → commit → observe pipeline failure.

Fix the issue → commit again → observe successful recovery.

This allows you to collect data for:

Failed deployments (for CFR)

Recovery times (for MTTR)
