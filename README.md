# Week 6 - Python CI Project

A small Logistics Data Analytics Python project demonstrating Continuous Integration with GitHub Actions.

## Features
- Loads logistics shipment data from CSV
- Calculates delivery KPIs
- Runs automated tests with pytest
- Checks code quality with Ruff
- Generates a JUnit XML test report
- GitHub Actions runs automatically on every push and pull request

## Project Structure
```text
week6_ci_python_project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   └── shipments.csv
├── src/
│   ├── __init__.py
│   └── logistics.py
├── tests/
│   └── test_logistics.py
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── pyproject.toml
├── run.py
└── README.md
```

## Local Setup
```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements-dev.txt
```

Run the project:
```bash
python run.py
```

Run tests:
```bash
pytest
```

Generate a test report:
```bash
pytest --junitxml=test-report.xml
```

Run linting:
```bash
ruff check .
```

## CI Pipeline
The GitHub Actions workflow:
1. Checks out the repository.
2. Sets up Python.
3. Installs dependencies.
4. Runs Ruff linting.
5. Runs pytest.
6. Generates a JUnit XML test report.
7. Uploads the test report as a workflow artifact.

The workflow fails automatically if linting or tests fail.

## Triggering CI
Push any commit to GitHub or open/update a pull request. GitHub Actions will start the workflow automatically.

## Viewing CI Logs
Open the GitHub repository and select **Actions**. Choose the latest workflow run to view each step and its logs.

## Challenges and Solutions
One challenge was making the local environment match the CI environment. This was addressed by specifying the Python version and dependencies in the workflow and requirements files. Another challenge was ensuring that a failed test stops the pipeline. Pytest's default non-zero exit code is used by GitHub Actions, so a failed test causes the workflow to fail.

## Verification
The project can be verified locally with:
```bash
ruff check .
pytest --junitxml=test-report.xml
```

A successful execution confirms that the code passes linting and the automated test suite.
