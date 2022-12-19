import typing


class Session:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def sample(self, data: typing.Any) -> None:
        self.data = data

    def query(self, instructions: str) -> str:
        return "TODO"
