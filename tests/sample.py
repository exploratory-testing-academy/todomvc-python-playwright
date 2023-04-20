@pytest.fixture(scope="session")
def my_context_arguments(url):
    return {
        "base_url": url,
        "locale": "fi-FI",
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
        "java_script_enabled": True,
        "storage_state": {
            "origins": [{
                "origin": url,
                "localStorage": [{"name": "todos-vanillajs", "value": '[{"title":"Macaroni Penguin.","completed":false,"id":1681973331983}]'}],
            }]
        }
    }


