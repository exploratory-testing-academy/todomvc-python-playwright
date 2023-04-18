from playwright.sync_api import BrowserContext

from utils.logger import Logger


class TodoLocalStorage:
    def __init__(self, context: BrowserContext):
        self.cont = context

    def get_local_storage_value(self) -> list:
        for k, v in self.cont.request.storage_state().items():
            Logger().debug(f"Browser context Key: {k} Value: {v}")
            if k == "origins":
                origins = v
                for i in origins:
                    local_s = i.get("localStorage")
                    if local_s:
                        for y in local_s:
                            ls_content = y.get("value")
                            Logger().debug(f"{ls_content}")
                            return ls_content
        raise ValueError("No expected content in browser context")

"""
    def set_context(self):
        this = {
            baseURL: 'http://localhost:3000',
            browserName: 'firefox',
            headless: true,
            locale: "fi-FI"
            storageState
                viewport: {width: 1280, height: 720},
                          ignoreHTTPSErrors: true,
        video: 'on-first-retry'
        screenshot: 'only-on-failure'
        }"""