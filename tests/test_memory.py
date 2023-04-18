from data.data import Data
from objects.todo_local_storage import TodoLocalStorage
from objects.todo_page import TodoPage
from utils.logger import Logger

log = Logger()


class TestMemory:

    def test_memory(self, br, br_page):
        first_todo = Data().get_fake_sentence(nb_words=2)

        local_storage_content = TodoLocalStorage(br).get_local_storage_value()
        assert local_storage_content

        p = TodoPage(br_page)
        assert p.is_todo_list_visible()
        p.fill_todo(first_todo)
        p.submit_todo_with_enter()
        p.verify_complete_match_todo_text(first_todo)
        local_storage_content_after = TodoLocalStorage(br).get_local_storage_value()
        assert first_todo in local_storage_content_after
        assert p.is_todo_list_visible()

        br_page.close()

        new_page = br.new_page()
        second_todo = Data().get_fake_sentence(nb_words=2)

        new_p = TodoPage(new_page)
        new_p.navigate_to()
        local_storage_content = TodoLocalStorage(new_page.context).get_local_storage_value()
        assert first_todo in local_storage_content
        new_p.fill_todo(second_todo)
        new_p.submit_todo_with_enter()
        local_storage_content_after = TodoLocalStorage(new_page.context).get_local_storage_value()
        assert first_todo in local_storage_content_after
        assert second_todo in local_storage_content_after
        new_p.verify_contains_todo_text(first_todo)



