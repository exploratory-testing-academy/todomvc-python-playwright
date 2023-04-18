import pytest
from playwright.sync_api import expect
from input_data import InputData

class TestBasic:

    @pytest.mark.parametrize("input_text", ["test", "foo bar baz "], ids=["first", "foobarbaz"])
    def test_add_todo(self, page_to_url, input_text):
        page_to_url.locator(".new-todo").fill(input_text)
        page_to_url.locator(".new-todo").press("Enter")
        expect(page_to_url.locator(".todo-list li label")).to_have_text(input_text.strip())

    def test_add_todo_with_off_focus(self, page_to_url):
        page_to_url.locator(".new-todo").fill("test")
        page_to_url.locator("footer.info").click()
        expect(page_to_url.locator(".todo-list li label")).to_have_text("test")

    def test_should_not_add_empty_todos(self, page_to_url):
        page_to_url.locator(".new-todo").fill("")
        page_to_url.locator(".new-todo").press("Enter")
        assert page_to_url.locator(".todo-list li").count() == 0

    def test_todo_completed(self, page_to_url):
        page_to_url.locator(".new-todo").fill("mark as completed")
        page_to_url.locator(".new-todo").press("Enter")
        page_to_url.locator(".toggle").check()
        assert page_to_url.locator(".todo-list li.completed").is_visible()

    def test_todo_deleted(self, page_to_url):
        page_to_url.locator(".new-todo").fill("will soon be deleted")
        page_to_url.locator(".new-todo").press("Enter")
        page_to_url.locator(".todo-list").hover()
        page_to_url.locator(".destroy").click()

    def test_counter_displays_nb_of_todos(self, page_to_url):
    #should display the current number of todo items
        page_to_url.locator(".new-todo").fill("first todo")
        page_to_url.keyboard.press("Enter")
        page_to_url.locator(".new-todo").fill("second todo")
        page_to_url.keyboard.press("Enter")
        expect(page_to_url.locator(".todo-count")).to_have_text("2 items left")

    @pytest.mark.my_markers("this")
    def test_data_persists_on_local_storage(self, my_browser):
        InputData(my_browser).create_todos(1)
        my_browser.context.new_page().goto('https://todomvc.com/examples/vanillajs/')
        expect(my_browser.locator(".todo-count")).to_have_text("1 item left")

    @pytest.mark.my_markers("this")
    def test_filters_all_default(self, page_to_url):
        InputData(page_to_url).create_basic_data(3, 0)
        expect(page_to_url).to_have_url("https://todomvc.com/examples/vanillajs/")
        assert page_to_url.locator("[data-id]").count() == 3

    def test_filters_completed(self, page_to_url):
        InputData(page_to_url).create_basic_data(3, 0)
        page_to_url.locator("//a[text()='Completed']").click()
        expect(page_to_url).to_have_url("https://todomvc.com/examples/vanillajs/#/completed")
        assert page_to_url.locator("[data-id].completed").count() == 1

    def test_filters_active(self, page_to_url):
        InputData(page_to_url).create_basic_data(3, 0)
        page_to_url.locator("//a[text()='Active']").click()
        expect(page_to_url).to_have_url("https://todomvc.com/examples/vanillajs/#/active")
        assert page_to_url.locator("[data-id]").count() == 2

    def test_start_with_data_from_storage(self, page_to_url):
       pass

