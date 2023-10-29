import pytest
from interpreter.interpreter import Interpreter


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()


class TestInterpreter:
    interpreter = Interpreter()

    def test_add(self, interpreter):
        assert interpreter.eval("2+2") == 4.0

    def test_sub(self, interpreter):
        assert interpreter.eval("2-2") == float(0)

    def test_add_with_letter(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2+a")

    def test_add_with_letter_others(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("t+2")

    def test_wrong_operator(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2&3")

    @pytest.mark.parametrize(
        "interpreter, code", [(interpreter, "2 + 2"),
                              (interpreter, "2 +2 "),
                              (interpreter, " 2+2")]
    )
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(code) == float(4)

    @pytest.mark.parametrize(
        "interpreter, code", [(interpreter, "2-2"),
                              (interpreter, "2 -  2 "),
                              (interpreter, " 2-2")]
    )
    def test_sub_variants(self, interpreter, code):
        assert interpreter.eval(code) == 0.0

    @pytest.mark.parametrize(
        "interpreter, code", [(interpreter, "2*2"),
                              (interpreter, "2 *  2 ")]
    )
    def test_multiply_spaces(self, interpreter, code):
        assert interpreter.eval(code) == 4.0

    def test_power(self, interpreter):
        assert 4.0 == interpreter.eval("2^2")
        assert 27.0 == interpreter.eval("3 ^3")

    def test_division(self, interpreter):
        assert 5.0 == interpreter.eval("10 /2")

    def test_division_zero(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2/0")

    def test_modulo(self, interpreter):
        assert 0.0 == interpreter.eval("10%2")
        assert 1.0 == interpreter.eval("5     %     2")

    def test_module_division_zero(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval("2%0")

    def test_brackets(self, interpreter):
        assert interpreter.eval("(2+2)    * 2") == 8.0
        assert interpreter.eval("2 + 2 * 2") == 6.0

