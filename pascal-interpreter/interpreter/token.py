from enum import Enum, auto

SUPPORTED_MATH_OPERATORS = ['+', '-', '*', '/', '%', '^']
REGULAR_MATH_OPERATIONS = ['+', '-']
HIGH_PRIORITY_MATH_OPERATIONS = ['*', '/', '%', '^']

BEGIN_NAME = 'BEGIN'
END_NAME_EXTERNAL = 'END.'
END_NAME_INTERNAL = 'END;'
VARIABLE_ALPHABET = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()


class TokenType(Enum):
    NUMBER = auto()
    OPERATOR = auto()
    EOL = auto()
    LPAREN = auto()
    RPAREN = auto()
    PROG_BEGIN = auto()
    PROG_END_EXTERNAL = auto()
    PROG_END_INTERNAL = auto()


class Token:

    def __init__(self, type_: TokenType, value: str):
        self.type_ = type_
        self.value = value

    def __str__(self):  # pragma: no cover
        return f"Token({self.type_}, {self.value})"
