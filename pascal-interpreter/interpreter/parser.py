from .ast import Number, BinOp
from .lexer import Lexer
from .token import Token, TokenType, HIGH_PRIORITY_MATH_OPERATIONS, REGULAR_MATH_OPERATIONS


class Parser:
    def __init__(self):
        self._current_token = None
        self.lexer = Lexer()

    def check_token(self, type_: TokenType):
        if self._current_token.type_ == type_:
            self._current_token = self.lexer.next()
        else:
            raise SyntaxError("invalid token order")

    def factor(self):
        token = self._current_token
        if token is None: # pragma: no cover
            raise SyntaxError("Invalid factor")
        if token.type_ == TokenType.NUMBER:
            self.check_token(TokenType.NUMBER)
            return Number(token)
        if token.type_ == TokenType.LPAREN:
            self.check_token(TokenType.LPAREN)
            result = self.expr()
            self.check_token(TokenType.RPAREN)
            return result
        if token.type_ == TokenType.OPERATOR:
            self.check_token(TokenType.OPERATOR)
            return BinOp(Number(Token(TokenType.NUMBER, "0")), token, self.factor())
        if token.type_ == TokenType.PROG_END_EXTERNAL or token.type_ == TokenType.PROG_END_INTERNAL or token.type_ == TokenType.PROG_BEGIN:
            return 42
        raise SyntaxError("Invalid factor")

    def term(self):
        result = self.factor()

        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            if self._current_token.value not in HIGH_PRIORITY_MATH_OPERATIONS:
                break
            token = self._current_token
            self.check_token(TokenType.OPERATOR)
            return BinOp(result, token, self.term())
        return result

    def expr(self):
        result = self.term()
        if result == 42:
            pass
        while self._current_token and (self._current_token.type_ == TokenType.OPERATOR):
            if self._current_token.value not in REGULAR_MATH_OPERATIONS:
                break  # pragma: no cover
            token = self._current_token
            self.check_token(TokenType.OPERATOR)
            result = BinOp(result, token, self.term())
        return result

    def parse(self, code):
        self.lexer.init(code)
        self._current_token = self.lexer.next()
        return self.expr()
