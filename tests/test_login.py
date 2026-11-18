import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

SUCCESS_URL = "https://practicetestautomation.com/logged-in-successfully/"
VALID_USERNAME = "student"
VALID_PASSWORD = "Password123"


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    lp = LoginPage(page)
    lp.open()
    return lp


def test_valid_login_and_logout(page: Page, login_page: LoginPage):
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    expect(page).to_have_url(SUCCESS_URL)
    expect(page.get_by_role("heading", name="Logged In Successfully")).to_be_visible()
    expect(page.get_by_text(f"Congratulations {VALID_USERNAME}. You successfully logged in!")).to_be_visible()

    logout_link = page.get_by_role("link", name="Log out")
    expect(logout_link).to_be_visible()
    logout_link.click()

    expect(page).to_have_url(LoginPage.URL)


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        pytest.param("incorrectUser", VALID_PASSWORD, "Your username is invalid!", id="invalid-username"),
        pytest.param(VALID_USERNAME, "incorrectPassword", "Your password is invalid!", id="invalid-password"),
        pytest.param("", VALID_PASSWORD, "Your username is invalid!", id="empty-username"),
        pytest.param(VALID_USERNAME, "", "Your password is invalid!", id="empty-password"),
    ],
)
def test_invalid_login_shows_error(page: Page, login_page: LoginPage, username: str, password: str, expected_error: str):
    login_page.login(username, password)

    expect(page).to_have_url(LoginPage.URL)
    login_page.expect_error(expected_error)
