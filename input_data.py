from playwright.sync_api import Page
class InputData():
    def __init__(self, user: Page):
       self.page = user

    def create_basic_data(self, todo_nb: int, complete_nb: int):
        self.create_todos(todo_nb)
        self.mark_completed(complete_nb)

    def create_todos(self, nb: int):
        for nb in range(nb):
            self.page.locator(".new-todo").fill(f"{nb} todo")
            self.page.keyboard.press("Enter") 

    def mark_completed(self, nb: int):
        self.page.locator(f".toggle >> nth={nb}").check()