import os


class Helpers:

    @staticmethod
    def get_project_root() -> str:
        return f"{os.path.dirname(os.path.abspath(__file__))}/.."

    def get_data_root(self) -> str:
        return f"{self.get_project_root()}/data"
