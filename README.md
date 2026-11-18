![Playwright UI & API Tests](https://github.com/AnaVauquelin/qa-python-playwright/actions/workflows/tests.yml/badge.svg)

End-to-end UI, REST API, and network-interception test automation suite built with **Python**, **Playwright**, and **Pytest**.

## Architecture & Coverage
- **Page Object Model (`pages/`)**: Decouples page locators and actions from test assertions.
- **UI & Parameterized Flows (`tests/test_login.py`)**: Positive authentication/logout flows and data-driven negative validation.
- **Dynamic Waits (`tests/test_exceptions.py`)**: Asynchronous DOM handling without hard sleeps.
- **REST API Testing (`tests/test_api_users.py`)**: CRUD and payload validation using Playwright's `APIRequestContext`.
- **Network Interception (`tests/test_network_mock.py`)**: Simulates `500` server errors via `page.route()`.
- **CI/CD (`.github/workflows/tests.yml`)**: Automated execution on every push and pull request with trace artifact uploads on failure.

## Run Locally
```bash
pip install -r requirements.txt
playwright install chromium
pytest -v
