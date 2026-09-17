# CI Pipeline Documentation

## Tool Used
GitHub Actions is used as the Continuous Integration platform.

## Pipeline Stages
- Environment setup with Python 3.11
- Dependency installation
- Ruff code linting
- Pytest automated testing
- JUnit XML test report generation
- Test report artifact upload

## Quality Control
The workflow uses normal command exit codes. If Ruff reports linting errors or pytest reports a failed test, the corresponding GitHub Actions step exits with a non-zero status and the workflow fails.

## Local Replication
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
ruff check .
pytest --junitxml=test-report.xml
```

## GitHub Verification
After pushing the project:
1. Open the repository on GitHub.
2. Select the **Actions** tab.
3. Open the **Python CI** workflow.
4. Select the latest run.
5. Review the linting and test logs.
6. Download the `test-report` artifact when the workflow finishes.

## Suggested Final Verification
Make a small documentation or Python change, commit it, and push:
```bash
git add .
git commit -m "Verify CI pipeline"
git push
```

The push triggers the workflow automatically.
