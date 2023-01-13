from enum import Enum, auto


class TokenType(Enum):
    NUMBER = auto()
    EOL = auto()
    VARIABLE = auto()
    ASSIGN = auto()
    SEMI = auto()
    TYPE = auto()
    POINTER = auto()
    REFERENCE = auto()
