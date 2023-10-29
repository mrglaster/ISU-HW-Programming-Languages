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

    def eval(self, code):
        tree = self.parser.parse(code)
        return self.visit(tree)
