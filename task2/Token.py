import TokenType


class Token:

    def __init__(self, type_: TokenType, value: str):
        self.type = type_
        self.value = value

    def __str__(self) -> str:
        return f"Token ({self.type}, {self.value})"
