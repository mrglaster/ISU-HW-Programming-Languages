import sys
import os
from interpreter.interpreter import Interpreter


def interpreter_cmd(interpreter: Interpreter) -> None:
    while True:
        print("in> ", end="")
        text = input()
        print(f": {text}")
        if text == "exit" or len(text) < 1:
            break
        try:
            result = interpreter.eval(text)
            print(f"out> {result}")
        except (SyntaxError, ValueError, TypeError) as e:
            print(f"{type(e).__name__}: {e}", file=sys.stderr)
    print("Done!")


def process_code_array(interpreter: Interpreter, program_code: list) -> None:
    for i in program_code:
        interpreter.eval(i)


def interpreter_file(interpreter: Interpreter, file_path: str) -> None:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error! File {file_path} was not found!")
    with open(file_path, 'r', encoding='utf-8') as f:
        program_code = f.readlines()
        interpreter.process_program(program_code)


if __name__ == "__main__":
    interp = Interpreter()
    interpreter_file(interp, 'demo_program.pas')
