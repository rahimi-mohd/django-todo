import re
from playwright.sync_api import Page, expect

URL = "http://localhost:8000"
user = {
    "username": "admin",
    "password": "12",
}

new_user = {
    "username": "sya",
    "email": "s@email.com",
    "password": "namasayabingo12",
    "password_conf": "namasayabingo12",
}


def test_functionality(page: Page):
    page.goto(URL)

    # test login the website and go to the home page
    # Enter username and password then click login button
    page.get_by_label("Username").fill(user["username"])
    page.get_by_label("Password").fill(user["password"])

    page.get_by_role("button", name="Login").click()

    # Expects next page to have a heading with the name of "This is home page".
    expect(page.get_by_text(f"Hello {user["username"]}")).to_be_visible()

    # check if todo empty
    expect(page.get_by_text("Congratulations!! You don't have any pending Todos.")).to_be_visible()

    # test entering a todo and display it on the screen
    page.get_by_label("Content").fill("first todo")
    page.get_by_role("button", name="Add").click()

    expect(page.get_by_text("first todo")).to_be_visible()

    # change status from in progress to done
    page.get_by_role("link", name="In Progress").click()
    expect(page.get_by_text("Done")).to_be_visible()

    # click Done todo and delete it
    page.get_by_role("link", name="Done").click()
    expect(page.get_by_text("Pwoshhh.....first todo deleted")).to_be_visible()

    # logout and go to login page back
    page.get_by_role("button", name="Log Out").click()
    expect(page.get_by_role("button", name="Login")).to_be_visible()

def test_register_user_and_login(page: Page):
    page.goto(URL)

    # click on the register here link and go to register page
    page.get_by_role("link", name="Register Here!").click()
    expect(page.get_by_text("Add New Account")).to_be_visible()

    # fill in username, email, password and password confirmation
    page.get_by_label("Username").fill(new_user["username"])
    page.get_by_label("Email").fill(new_user["email"])
    page.get_by_label("Password", exact=True).fill(new_user["password"])
    page.get_by_label("Password confirmation", exact=True).fill(new_user["password_conf"])

    # click on register button
    page.get_by_role("button", name="Register").click()

    # get messages show username registered successfully
    expect(page.get_by_text(f"{new_user["username"]} register successfully.")).to_be_visible()

    # go to login page and try to login
    expect(page.get_by_role("button", name="Login")).to_be_visible()

    page.get_by_label("Username").fill(new_user["username"])
    page.get_by_label("Password").fill(new_user["password"])

    page.get_by_role("button", name="Login").click()

    # Expects next page to have a heading with the name of "This is home page".
    expect(page.get_by_text(f"Hello {new_user["username"]}")).to_be_visible()


# go to admin page and delete new user account
def test_admin_page_delete_new_user(page: Page):
    page.goto(f"{URL}/admin/")
    expect(page.get_by_role("link", name="Django administration")).to_be_visible()

    # enter admin username and password, and click Log in
    page.get_by_label("Username:").fill(user["username"])
    page.get_by_label("Password:").fill(user["password"])
    page.get_by_text("Log in").click()

    expect(page.get_by_role("link", name="Django administration")).to_be_visible()

    # click on Users, choose new user's username and click delete action
    page.get_by_role("link", name="Users").click()
    page.get_by_role("checkbox", name=new_user["username"]).click()
    # to handle select, get it name and the option value
    page.select_option("select[name='action']", value="delete_selected")
    page.get_by_role("button", name="Go").click()

    # go to delete confirmation page
    expect(page.get_by_text("Are you sure?")).to_be_visible()

    # click sure button, and get success message
    page.get_by_text("Yes, I’m sure").click()
    expect(page.get_by_title("Successfully deleted 1 user."))

    # log out from admin page and redirect to login page
    page.get_by_role("button", name="LOG OUT").click()
    expect(page.get_by_role("button", name="Login")).to_be_visible()
