import pytest
from playwright.sync_api import expect, BrowserContext


@pytest.mark.parametrize("input_text", ["test", "foo bar baz "], ids=["first", "foobarbaz"])
def test_add_todo(page_to_url, input_text):
    page_to_url.locator(".new-todo").fill(input_text)
    page_to_url.locator(".new-todo").press("Enter")
    expect(page_to_url.locator(".todo-list li label")).to_have_text(input_text.strip())

def test_add_todo_with_off_focus(page_to_url):
    page_to_url.locator(".new-todo").fill("test")
    page_to_url.locator("footer.info").click()
    expect(page_to_url.locator(".todo-list li label")).to_have_text("test")

def test_should_not_add_empty_todos(page_to_url):
    page_to_url.locator(".new-todo").fill("")
    page_to_url.locator(".new-todo").press("Enter")
    assert page_to_url.locator(".todo-list li").count() == 0

def test_todo_completed(page_to_url):
    page_to_url.locator(".new-todo").fill("mark as completed")
    page_to_url.locator(".new-todo").press("Enter")
    page_to_url.locator(".toggle").check()
    assert page_to_url.locator(".todo-list li.completed").is_visible()

def test_todo_deleted(page_to_url):
    page_to_url.locator(".new-todo").fill("will soon be deleted")
    page_to_url.locator(".new-todo").press("Enter")
    page_to_url.locator(".todo-list").hover()
    page_to_url.locator(".destroy").click()

def test_counter_displays_nb_of_todos(page_to_url):
#should display the current number of todo items
    page_to_url.locator(".new-todo").fill("first todo")
    page_to_url.keyboard.press("Enter")
    page_to_url.locator(".new-todo").fill("second todo")
    page_to_url.keyboard.press("Enter")
    expect(page_to_url.locator(".todo-count")).to_have_text("2 items left")

@pytest.mark.my_markers("this")
def test_data_persists_on_local_storage(my_browser):
    my_browser.locator(".new-todo").fill("first todo")
    my_browser.keyboard.press("Enter") 
    my_browser.context.new_page().goto('https://todomvc.com/examples/vanillajs/')
    expect(my_browser.locator(".todo-count")).to_have_text("1 item left")
