from playwright.sync_api import expect

def test_add_todo(page):
    page.goto("https://todomvc.com/examples/vanillajs/")
    input_field = page.get_by_placeholder("What needs to be done?")
    input_field.fill("Learning Playwright")
    input_field.press("Enter")
    expect(page.locator(".todo-list li label")).to_have_text("Learning Playwright")