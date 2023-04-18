import os

import pytest

from playwright.sync_api import Browser, Page, BrowserContext
from slugify import slugify

from utils.logger import Logger


@pytest.fixture(scope="session", autouse=True)
def url(pytestconfig):
    url = None
    if url is None:
        url = pytestconfig.getoption("base_url")
    yield url

@pytest.fixture(scope="session")
def br(browser: Browser, my_context_arguments, pytestconfig, request: pytest.FixtureRequest) -> BrowserContext:
    Logger().debug("Opened a session shared browser context")
    new_context = browser.new_context(**my_context_arguments)
    new_context.tracing.start(snapshots=True, screenshots=True)
    yield new_context
    new_context.tracing.stop(path=_build_result_folder(pytestconfig, request, "trace.zip"))
    new_context.close()


@pytest.fixture(scope="function")
def br_page(br, url) -> Page:
    Logger().debug("This page has been opened from session shared browser context")
    new_page = br.new_page()
    new_page.goto(url)
    yield new_page


@pytest.fixture(scope="session")
def my_context_arguments(url):
    context_args = {
        "base_url": url,
        "locale": "fi-FI",
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
        "java_script_enabled": True,
    }
    return context_args


@pytest.fixture(scope="function", autouse=True)
def log_test(request: pytest.FixtureRequest):
    name_of_test = request.node.name
    Logger().info(f"Begin {name_of_test}")
    yield
    Logger().debug(f"End {name_of_test}")


def _build_result_folder(pytestconfig, request: pytest.FixtureRequest, folder_or_file_name: str) -> str:
    return os.path.join(pytestconfig.getoption("--output"), slugify(request.node.name), folder_or_file_name)


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
