from playwright.sync_api import Page, expect


class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.error_banner = page.locator("#error")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def expect_error(self, message: str):
        expect(self.error_banner).to_be_visible()
        expect(self.error_banner).to_have_text(message)
