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


def test_edit_existing_row_updates_confirmation(page: Page):
    page.goto(EXCEPTIONS_URL)
    row_one_input = page.locator("#row1 input")

    page.locator("#row1").get_by_role("button", name="Edit").click()
    expect(row_one_input).to_be_editable()

    row_one_input.fill("Updated burger order")
    page.locator("#row1").get_by_role("button", name="Save").click()

    expect(page.locator("#confirmation")).to_have_text("Row 1 was saved")
