import json
from playwright.sync_api import Page, expect


def test_handles_server_500_on_redirect(page: Page):
    page.route(
        "**/logged-in-successfully*",
        lambda route: route.fulfill(
            status=500,
            content_type="text/html",
            body="<h1>500 Internal Server Error</h1>",
        ),
    )

    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_role("heading", name="Logged In Successfully")).not_to_be_visible()
    expect(page.get_by_text("500 Internal Server Error")).to_be_visible()


def test_mocks_api_response_payload_in_browser(page: Page):
    mocked_user = {
        "id": 999,
        "name": "Mocked QA Engineer",
        "email": "qa.mock@example.com",
    }

    page.route(
        "**/users/1",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps(mocked_user),
        ),
    )

    page.goto("https://jsonplaceholder.typicode.com/users/1")
    body_text = page.locator("body").inner_text()
    assert "Mocked QA Engineer" in body_text
    assert "qa.mock@example.com" in body_text
