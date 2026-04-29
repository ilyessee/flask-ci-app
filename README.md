# Flask CI App

A Flask to-do list app with linting, testing, Git hooks, and GitHub Actions CI.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the app

```bash
python -m app
```

## Linting

```bash
ruff check app
```

## Tests

```bash
pytest
```

## Git Hook (pre-push)

After cloning, install the hook once:

```bash
cp pre-push.hook .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

This will run `ruff check app` and `pytest` before every `git push`, blocking the push if either fails.

## GitHub Actions CI

The workflow at `.github/workflows/ci.yml` runs automatically on every pull request targeting the `dev` branch. It:
1. Installs dependencies
2. Runs `ruff check app`
3. Runs `pytest`

The PR is blocked if either step fails.

## Project Structure

```
flask-ci-app/
├── app/
│   ├── __init__.py        # Flask app factory + routes
│   ├── utils.py           # Pure utility functions
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── tests/
│   ├── test_unit_example.py
│   └── test_integration_example.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml         # ruff + pytest config
├── requirements.txt
├── pre-push.hook          # copy to .git/hooks/pre-push
└── .gitignore
```
