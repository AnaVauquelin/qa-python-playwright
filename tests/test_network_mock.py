from playwright.sync_api import Page, expect


def test_handles_server_500_gracefully(page: Page):
    page.route(
        "**/practice-test-login/**",
        lambda route: route.fulfill(status=500, body="Internal Server Error")
        if route.request.method == "POST"
        else route.continue_(),
    )

    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()

    expect(page).not_to_have_url("https://practicetestautomation.com/logged-in-successfully/")
