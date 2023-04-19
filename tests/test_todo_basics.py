from data.data import Data
from objects.todo_page import TodoPage
from utils.logger import Logger

log = Logger()


class TestTodoBasics:

    def test_add_todo(self, page):
        p = TodoPage(page)
        p.navigate_to()
        the_todo = Data().get_fake_sentence(nb_words=2)
        log.debug(f"{the_todo}")
        p.fill_todo(the_todo)
        p.submit_todo_with_enter()
        p.verify_complete_match_todo_text(the_todo)

    def test_add_todo_2(self, page):
        d = Data().get_fake_sentence(nb_words=2)
        log.debug(f"{d}")
        my_todos = TodoPage(page)
        my_todos.navigate_to()
        my_todos.fill_todo(d)
        my_todos.submit_todo_with_enter()
        my_todos.verify_complete_match_todo_text(d)

