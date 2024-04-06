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


class DeMorganModifier(ast.NodeTransformer):
    '''
    This class transforms a Boolean expression into its logical equivalent counterpart
    using De Morgan's Law.

    More specifically:
    1. (a or b) -> ~(~a and ~b)
    2. (a and b) -> ~(~a or ~b)
    3. (~a or b) -> ~(a and ~b)
    4. (a or ~b) -> ~(~a and b)
    5. (~a and b) -> ~(a or ~b)
    6. (a and ~b) -> ~(~a or b)
    7. (~a or ~b) -> ~(a and b)
    8. (~a and ~b) -> ~(a or b)
    '''

    def visit_BoolOp(self, node):
        if isinstance(node.op, (ast.And, ast.Or)):
            # Rewrite Boolean expressions
            return self._rewrite_boolean_expression(node)
        return node

    def _rewrite_boolean_expression(self, node):
        # Get new boolean operator
        new_boolean_operator = ast.Or() if (isinstance(node.op, ast.And)) else ast.And()

        # Negate each of the original operands
        negated_operands = []
        for value in node.values:
            # Negate the current operand

            # Check what form is the current operand
            if isinstance(value, ast.UnaryOp) and isinstance(value.op, ast.Not):
                # Case 1: Current operand is already a NOT expression.
                # We simply remove the NOT expression.
                new_operand = value.operand
                negated_operands.append(new_operand)
            else:
                # Case 2: Current operand is not a NOT expression.
                # We negate the operand.
                new_operand = ast.UnaryOp(op=ast.Not(), operand=value)
                negated_operands.append(new_operand)

        # Return final expression
        return ast.UnaryOp(op=ast.Not(),
                           operand=ast.BoolOp(op=new_boolean_operator, values=negated_operands))

class IdempotentModifier(ast.NodeTransformer):
    '''
    This class transforms a Boolean variable into its logical equivalent counterpart
    using Idempotent Law.

    More specifically:
    1. a -> a and a
    2. a -> a or a
    '''
    def __init__(self, type_of_transformation):
        '''
        Parameters:
            type_of_transformation: Decides which Idempotent transformation to perform
                                    1 means Transformation 1, 2 means Transformation 2.
        '''
        super().__init__()
        self.type_of_transformation = type_of_transformation

    def visit_Name(self, node):
        # Decide which of the 2 Idempotent transformations to undergo
        if (self.type_of_transformation == 1):
            # Apply a -> a and a transformation
            return ast.BoolOp(op=ast.And(), values=[node, node])
        elif (self.type_of_transformation == 2):
            # Apply a -> a or a transformation
            return ast.BoolOp(op=ast.Or(), values=[node, node])
        
        # Not a valid Idempotent transformation
        return node