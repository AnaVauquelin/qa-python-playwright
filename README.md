# Python + Playwright QA Automation Framework

![CI Pipeline](https://github.com/AnaVauquelin/qa-python-playwright/actions/workflows/main.yml/badge.svg)

End-to-end UI and REST API test automation framework built with **Python**, **Pytest**, and **Playwright**, following the **Page Object Model (POM)** design pattern and integrated with a multi-stage **GitHub Actions CI/CD** pipeline.

---

## Tech Stack
- **Language:** Python 3.11
- **Test Runner:** Pytest
- **UI & API Automation:** Playwright (`sync_api`, `APIRequestContext`, network interception via `page.route()`)
- **Code Quality & Linting:** Ruff
- **CI/CD:** GitHub Actions (Dockerized execution, cross-browser matrix for Chromium & Firefox, branch protection status gates)

---

## Project Structure
```text
├── .github/workflows/
│   └── main.yml          # Multi-stage CI/CD pipeline (Lint -> API -> UI Matrix -> Summary Gate)
├── pages/                # Page Object Model classes & locators
├── tests/                # UI, E2E, parameterized, network mocking, and REST API test suites
├── conftest.py           # Shared Pytest fixtures & browser/API context configuration
├── pyproject.toml        # Ruff linter & project configuration
├── pytest.ini            # Pytest markers & CLI options
└── requirements.txt      # Project dependencies
