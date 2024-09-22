import re
from playwright.sync_api import Page, expect


def test_login_page(page: Page):
    page.goto("http://localhost:8000")

    # Enter username and password then click login button
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").fill("12")

    page.get_by_role("button", name="Log In").click()

    # Expects next page to have a heading with the name of "This is home page".
    expect(page.get_by_text("This is home page")).to_be_visible()
