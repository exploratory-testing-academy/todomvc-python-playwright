from playwright.sync_api import Page, expect


class TodoPage:
    def __init__(self, page: Page):
        self.p = page

    _todo_input = "input.new-todo"
    _todo_list = ".todo-list"

    # Navigation
    def navigate_to(self):
        self.p.goto("https://todomvc.com/examples/vanillajs")

    # Return functions
    def is_todo_list_visible(self) -> bool:
        return self.p.locator(self._todo_input).is_visible()

    def get_todo_count(self) -> int:
        return self.p.locator("").count()

    # Action functions
    def fill_todo(self, text: str):
        self.p.locator(self._todo_input).fill(text)

    def submit_todo_with_enter(self):
        self.p.keyboard.press("Enter")

    def submit_todo_with_focus_change(self):
        self.p.locator("footer.info").click()

    # Verify functions
    def verify_complete_match_todo_text(self, text: str):
        expect(self.p.locator(self._todo_list)).to_have_text(text)

    def verify_contains_todo_text(self, text: str):
        expect(self.p.locator(self._todo_list)).to_contain_text(text)

    def verify_todo_count(self, expected_count: int):
        assert expected_count == self.get_todo_count()
