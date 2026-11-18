from playwright.sync_api import Page, expect

EXCEPTIONS_URL = "https://practicetestautomation.com/practice-test-exceptions/"


def test_dynamic_row_appears_after_delay(page: Page):
    page.goto(EXCEPTIONS_URL)
    page.get_by_role("button", name="Add").click()

    row_two_input = page.locator("#row2 input")
    expect(row_two_input).to_be_visible(timeout=7000)

    row_two_input.fill("Playwright auto-wait")
    page.locator("#row2").get_by_role("button", name="Save").click()

    expect(page.locator("#confirmation")).to_have_text("Row 2 was saved")
