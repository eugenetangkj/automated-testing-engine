import ast


class VariableRenamer(ast.NodeTransformer):
    def __init__(self):
        super().__init__()
        self.var_count = 0
        self.name_mapping = {}

    # pylint: disable=invalid-name
    def visit_FunctionDef(self, node):
        self.name_mapping = {}
        for arg in node.args.args:
            new_name = f"var_{self.var_count}"
            self.var_count += 1
            self.name_mapping[arg.arg] = new_name
            arg.arg = new_name
        self.generic_visit(node)
        return node

    # pylint: disable=invalid-name
    def visit_Name(self, node):
        if node.id in self.name_mapping:
            node.id = self.name_mapping[node.id]
        return node


class BinOpModifier(ast.NodeTransformer):
    # pylint: disable=invalid-name
    def visit_BinOp(self, node):
        # Commutative Operations
        if isinstance(node.op, (ast.Add, ast.Mult)):
            node.left, node.right = node.right, node.left

        # Associative Operations
        if isinstance(node.op, (ast.Add, ast.Mult)) and isinstance(
            node.right, ast.BinOp
        ):
            if type(node.right.op) == type(node.op):
                node.left = ast.BinOp(left=node.left, op=node.op, right=node.right.left)
                node.right = node.right.right

        if (
            isinstance(node.op, ast.Add)
            and isinstance(node.right, ast.Num)
            and node.right.n == 0
        ):
            return node.left

        if (
            isinstance(node.op, ast.Add)
            and isinstance(node.left, ast.Num)
            and node.left.n == 0
        ):
            return node.right

        if (
            isinstance(node.op, ast.Mult)
            and isinstance(node.right, ast.Num)
            and node.right.n == 1
        ):
            return node.left

        if (
            isinstance(node.op, ast.Mult)
            and isinstance(node.left, ast.Num)
            and node.left.n == 1
        ):
            return node.right

        if isinstance(node.op, ast.Sub):
            node.op = ast.Add()
            node.right = ast.UnaryOp(op=ast.USub(), operand=node.right)

        return self.generic_visit(node)
