import pytest
from playwright.sync_api import Page, BrowserContext

@pytest.fixture(scope="function")
def page_to_url(page: Page) -> Page:
    page.goto('https://todomvc.com/examples/vanillajs/')
    yield page

#marker example - can run tests with 'pytest -m "my_markers"'
def pytest_configure(config):
    config.addinivalue_line("markers", "my_markers: this is how my marker is used")

@pytest.fixture(scope="session")
def my_browser(browser) -> Page:
    c = browser.new_context()
    p = c.new_page()
    p.goto('https://todomvc.com/examples/vanillajs/')
    yield p
    c.close()
