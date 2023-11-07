from interpreter.token import SUPPORTED_MATH_OPERATORS, TokenType, Token, BEGIN_NAME, END_NAME_EXTERNAL, \
    VARIABLE_ALPHABET, END_NAME_INTERNAL


class Lexer:
    def __init__(self):
        self._pos = 0
        self._text = ""
        self._current_char = None

        self.namespace = {}
        self._current_signing = None
        self.ends_count_external = 0
        self.endings = ""

    def init(self, text):
        self._text = text
        self._pos = 0
        self._current_char = self._text[self._pos]

    def forward(self):
        self._pos += 1
        if self._pos > len(self._text) - 1:
            self._current_char = None
        else:
            self._current_char = self._text[self._pos]

    def skip(self): # pragma: no cover
        while (self._current_char is not None and
               self._current_char.isspace()):
            self.forward()

    def number(self):
        result = []
        while (self._current_char is not None and
               (self._current_char.isdigit() or
                self._current_char == ".")):
            result.append(self._current_char)
            self.forward()
        return "".join(result)

    def __has_assign(self):
        return ':=' in self._text

    def __substitute(self):
        for i in self._text:
            if i in VARIABLE_ALPHABET:
                if i in self.namespace:
                    self._text = self._text.replace(i, str(self.namespace[i]))

    def __assign_check(self):
        if not self.__has_assign():
            raise SyntaxError(f"Invalid syntax: {self._text}")
        assign_position = self._text.find(':=')
        if assign_position == 0:
            raise SyntaxError(f"Invalid syntax: {self._text}")

        left_part = self._text[:assign_position]
        right_part = self._text[assign_position + 2:-1]

        if left_part.isnumeric():
            raise SyntaxError(f"Unable to assign value to the number: {self._text}")

        if len(left_part) != 1:
            raise SyntaxError(f"Sorry Mario, but we support only 1-symbol-long variables. Got: {left_part}")

        previous = ''
        for i in right_part:
            if i.isalpha() and previous.isalpha():
                raise SyntaxError("It seems, you try to use n-symbols-long variable, but we don't support it yet")
            previous = i

        self._current_signing = left_part
        if left_part not in self.namespace:
            self.namespace[left_part] = 0
        self._text = right_part
        self.__substitute()
        self._current_char = self._text[0]

    def next(self):
        if BEGIN_NAME in self._text:
            self.endings += 'b'
            return Token(TokenType.PROG_BEGIN, self._text)

        if END_NAME_EXTERNAL in self._text:
            self.ends_count_external += 1
            if self.ends_count_external > 1:
                raise SyntaxError("Too many Program End (END.) Tokens! Use END; instead!")
            self.endings += 'g'
            return Token(TokenType.PROG_END_EXTERNAL, self._text)

        if END_NAME_INTERNAL in self._text:
            self.endings += 'l'
            return Token(TokenType.PROG_END_INTERNAL, self._text)

        if not self._text.endswith(';') and self._current_signing is None:
            raise SyntaxError(f'{self._text} <- Semicolon Expected!')

        if not self._current_signing:
            self.__assign_check()

        while self._current_char:
            if self._current_char.isspace(): # pragma: no cover
                self.skip()
                continue
            if self._current_char.isdigit():
                return Token(TokenType.NUMBER, self.number())
            if self._current_char in SUPPORTED_MATH_OPERATORS:
                op = self._current_char
                self.forward()
                return Token(TokenType.OPERATOR, op)
            if self._current_char == "(":
                op = self._current_char
                self.forward()
                return Token(TokenType.LPAREN, op)
            if self._current_char == ")":
                op = self._current_char
                self.forward()
                return Token(TokenType.RPAREN, op)
            raise SyntaxError(f"Bad token: {self._current_char}")
