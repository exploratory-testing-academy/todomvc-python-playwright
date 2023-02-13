import pytest
from playwright.sync_api import Page

@pytest.fixture(scope="function")
def page_to_url(page) -> Page:
    page.goto('https://todomvc.com/examples/vanillajs/')
    return page


def pytest_configure(config):
    config.addinivalue_line("markers", "my_markers: this is how my marker is used")