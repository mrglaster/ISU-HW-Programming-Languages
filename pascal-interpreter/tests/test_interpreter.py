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

    def test_simple_assign(self, interpreter):
        program = ["BEGIN", "x:=2+2*2;", "END."]
        eval_code(interpreter, program)
        assert interpreter.get_namespace()['x'] == 6

    def test_several_variables_simple(self, interpreter):
        program = ["BEGIN", "x:=2+2*2;", "y:=(2+2)*2;", 'END.']
        eval_code(interpreter, program)
        assert interpreter.get_namespace()['x'] == 6
        assert interpreter.get_namespace()['y'] == 8

    def test_variable_usage(self, interpreter):
        program = ["BEGIN", "x:=2+2*2;", "y:=(2+2)*2;", "z:=x*y;", "END."]
        eval_code(interpreter, program)
        assert interpreter.get_namespace()['x'] == 6
        assert interpreter.get_namespace()['y'] == 8
        assert interpreter.get_namespace()['z'] == 48

    def test_valid_self_assign(self, interpreter):
        program = ["BEGIN", "a:=12;", "a:=a;", "END."]
        eval_code(interpreter, program)
        assert interpreter.get_namespace()['a'] == 12

    def test_internal_code_blocks(self, interpreter):
        program = ["BEGIN", "y:=2;", "BEGIN", "a:=3;", "a:=a;", "b:=10 + a + 10 * y / 4;", "c := a - b;", "END;",
                   "x := 11;", "END."]
        eval_code(interpreter, program)
        variables = interpreter.get_namespace()
        assert variables['x'] == 11.0
        assert variables['y'] == 2.0
        assert variables['a'] == 3.0
        assert variables['b'] == 18.0
        assert variables['c'] == -15.0

    def test_use_all_math_operations(self, interpreter):
        program = ["BEGIN", "x := (((2 + 2 * 2 / 4)^3) % 3) * 24;", "END."]
        eval_code(interpreter, program)
        assert interpreter.get_namespace()['x'] == 0

    def test_negative_variable(self, interpreter):
        program = ["BEGIN", "a:=4;", "a:=-a;", "END."]
        eval_code(interpreter, program)
        assert interpreter.get_namespace()['a'] == -4
