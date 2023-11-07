import pytest
from interpreter.interpreter import Interpreter


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()


def eval_code(interpreter, code):
    interpreter.process_program(code)


class TestInterpreter:
    interpreter = Interpreter()

    def test_program_skeleton(self, interpreter):
        program = ["BEGIN", "END."]
        eval_code(interpreter, program)
        assert not len(interpreter.get_namespace())

    @pytest.mark.parametrize(
        "interpreter, code", [(interpreter, ["BEGIN", "END;"]),
                              (interpreter, ["BEGIN"]),
                              (interpreter, ["END;"]),
                              (interpreter, ["BEGIN", "x:=2+2", "END."]),
                              (interpreter, ["BEGIN", "x:=a+2;", "END."]),
                              (interpreter, ["x:=2+2;"]),
                              (interpreter, ["BEGIN","x:=12/0;","END."]),
                              (interpreter, ["BEGIN", "x:=12%0;", "END."]),
                              (interpreter, ["BEGIN", "iddkofdkofdkofdkoko;", "END."]),
                              (interpreter, ["BEGIN", ":=24;", "END."]),
                              (interpreter, ["BEGIN", "24:=24;", "END."]),
                              (interpreter, ["BEGIN", "var:=24+24;", "END."]),
                              (interpreter, ["BEGIN", "BEGIN", "x:=24;", "END.", "END."]),
                              (interpreter, ["BEGIN", "BEGIN", "x:=var+13;", "END.", "END."])]

    )
    def test_syntax_errors(self, interpreter, code):
        with pytest.raises(SyntaxError):
            eval_code(interpreter, code)

    @pytest.mark.parametrize(
        "interpreter, ending", [(interpreter, "bl"),
                                (interpreter, "bbgl"),
                                (interpreter, "baag"),
                                (interpreter, "gglbb"),
                                (interpreter, "bblbl"),
                                (interpreter, "bblggg"),
                                (interpreter, "bblbxl"),
                                (interpreter, "")]


    )
    def test_check_endings_processing(self, interpreter, ending):
        interpreter.parser.lexer.endings = ending
        assert not interpreter.check_ends()