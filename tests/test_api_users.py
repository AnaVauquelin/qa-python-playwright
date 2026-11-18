import pytest
from playwright.sync_api import APIRequestContext, Playwright

API_BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    context = playwright.request.new_context(
        base_url=API_BASE_URL,
        ignore_https_errors=True,
    )
    yield context
    context.dispose()


def test_get_user_returns_valid_profile(api_context: APIRequestContext):
    response = api_context.get("/users/1")
    assert response.status == 200

    body = response.json()
    assert body["id"] == 1
    assert "@" in body["email"]
    assert "company" in body


def test_create_post_returns_201(api_context: APIRequestContext):
    payload = {
        "title": "Release readiness check",
        "body": "Automated smoke validation",
        "userId": 1,
    }
    response = api_context.post("/posts", data=payload)
    assert response.status == 201

    created = response.json()
    assert created["title"] == payload["title"]
    assert "id" in created
