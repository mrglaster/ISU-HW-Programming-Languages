import pytest
from interpreter import Parser
from interpreter.ast import Number, BinOp
from interpreter.token import Token, TokenType


class TestOthers:
    def test_number_token_str(self):
        demo_token = Token(TokenType.NUMBER, "12")
        a = Number(token=demo_token)
        assert str(a) == f"Number (Token(TokenType.NUMBER, 12))"

    def test_binop_str(self):
        demo_token_a = Token(TokenType.NUMBER, "12")
        demo_token_b = Token(TokenType.NUMBER, "12")
        demo_token_c = Token(TokenType.OPERATOR, "+")
        bin_op = BinOp(Number(demo_token_a), demo_token_c, Number(demo_token_b))
        print(f"RESULT IS: {bin_op}")
        assert str(bin_op) == f"BinOp+ (Number (Token(TokenType.NUMBER, 12)), Number (Token(TokenType.NUMBER, 12)))"

    def test_token_str(self):
        a = Token(TokenType.NUMBER, "12")
        assert str(a) == "Token(TokenType.NUMBER, 12)"

    def test_check_token(self):
        parser = Parser()
        parser._current_token = Token(TokenType.NUMBER, "42")
        with pytest.raises(SyntaxError):
            parser.check_token(TokenType.OPERATOR)

    def test_other_stuff(self):
        parser = Parser()
        result = parser.parse("x:=2*2;")
        assert result is not None

    def test_invalid_factor(self):
        tt = Token(12, str(24))
        parser = Parser()
        parser._current_token = tt
        with pytest.raises(SyntaxError):
            parser.factor()

    def test_operator_factor(self):
        tt = Token(TokenType.OPERATOR, '+')
        parser = Parser()
        parser._current_token = tt
        with pytest.raises(SyntaxError):
            parser.factor()
