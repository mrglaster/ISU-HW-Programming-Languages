from interpreter import Parser
from interpreter.ast import BinOp, Number


class NodeVisitor:
    def visit(self, node):  # pragma: no cover
        pass


def visit_number(node):
    return float(node.token.value)


class Interpreter(NodeVisitor):

    def __init__(self):
        self.parser = Parser()

    def visit(self, node):
        if isinstance(node, Number):
            return visit_number(node)
        elif isinstance(node, BinOp):
            return self.visit_binop(node)

    def visit_binop(self, node):
        match node.op.value:
            case '+':
                return self.visit(node.left) + self.visit(node.right)
            case '-':
                return self.visit(node.left) - self.visit(node.right)
            case '*':
                return self.visit(node.left) * self.visit(node.right)
            case '/':
                result = self.visit(node.right)
                if result != 0:
                    return self.visit(node.left) / self.visit(node.right)
                raise SyntaxError("Divide by 0 !")
            case '%':
                result = self.visit(node.right)
                if result != 0:
                    return self.visit(node.left) % self.visit(node.right)
                raise SyntaxError("Divide by 0 !")
            case '^':
                return self.visit(node.left) ** self.visit(node.right)

    @staticmethod
    def clean_string(code: str) -> str:
        return code.replace('\t', '').replace('\n', '').replace(' ', '')

    def eval(self, code):
        tree = self.parser.parse(self.clean_string(code))
        result = self.visit(tree)
        if self.parser.lexer._current_signing:
            self.parser.lexer.namespace[self.parser.lexer._current_signing] = result
            self.parser.lexer._current_signing = None
        return result

    def check_ends(self):
        s = self.parser.lexer.endings
        if len(s) % 2 != 0 or not len(s):
            return False
        if s.endswith('g') and s.startswith('b'):
            l_allowed = True
            for char in s[1:-1]:
                if char not in ('b', 'l'):
                    return False
                if char == 'l' and not l_allowed: # pragma: no cover
                    return False
                if char == 'g': # pragma: no cover
                    l_allowed = False
            return True
        return False

    def get_namespace(self):
        return self.parser.lexer.namespace

    def print_namespace(self): # pragma: no cover
        if not len(self.parser.lexer.namespace):
            print("Namespace is empty!")
        else:
            print()
            print("{:<8} {:<40}".format('Variable', 'Value'))
            for k, v in self.parser.lexer.namespace.items():
                print("{:<8} {:<40}".format(k, v))

    def process_program(self, program: list):
        for i in program:
            self.eval(i)
        if not self.check_ends():
            raise SyntaxError("BEGIN & END tokens problem!")
