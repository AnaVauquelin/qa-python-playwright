# Python + Playwright QA Automation Framework

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
```

---

## Key Features
- **Page Object Model (POM):** Clean separation of locators/page interactions and test assertions.
- **Cross-Browser UI Testing:** Automated runs on Chromium and Firefox with `retain-on-failure` Playwright tracing and screenshots.
- **REST API & Network Layer Testing:** Direct HTTP endpoint validation (`GET`, `POST`, `PUT`, `DELETE`) and client-side request/response mocking.
- **CI/CD Quality Gate:** Enforced branch protection rules requiring passing lint checks, API tests, and cross-browser UI suites before merging Pull Requests.

---

## Getting Started

### 1. Clone the repository & set up a virtual environment
```bash
git clone [https://github.com/AnaVauquelin/qa-python-playwright.git](https://github.com/AnaVauquelin/qa-python-playwright.git)
cd qa-python-playwright
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies & Playwright browsers
```bash
pip install -r requirements.txt
playwright install
```

### 3. Run the test suite & linter
```bash
# Run all tests
pytest -v

# Run linter
ruff check pages/ tests/
```
