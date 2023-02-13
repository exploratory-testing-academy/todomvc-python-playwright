import pytest
from playwright.sync_api import expect

@pytest.mark.my_markers("this")
@pytest.mark.parametrize("input_text", ["test", "foo bar baz "], ids=["first", "foobarbaz"])
def test_add_todo(page_to_url, input_text):
    page_to_url.locator(".new-todo").fill(input_text)
    page_to_url.locator(".new-todo").press("Enter")
    expect(page_to_url.locator(".todo-list li label")).to_have_text(input_text.strip())
    #assert input_text.strip() in page_to_url.locator(".todo-list li label").inner_text()

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
