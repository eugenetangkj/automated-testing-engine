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
    def __init__(self, type_of_transformation=1):
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


class IdentityModifier(ast.NodeTransformer):
    '''
    This class transforms a Boolean variable into its logical equivalent counterpart
    using Identity Law

    More specifically:
    1. a -> a and True
    2. a -> a or False
    '''
    def __init__(self, type_of_transformation=1):
        '''
        Parameters:
            type_of_transformation: Decides which Identity transformation to perform
                                    1 means Transformation 1, 2 means Transformation 2.
        '''
        super().__init__()
        self.type_of_transformation = type_of_transformation

    def visit_Name(self, node):
        # Decide which of the 2 Idempotent transformations to undergo
        if (self.type_of_transformation == 1):
            # Apply a -> a and True transformation
            return ast.BoolOp(op=ast.And(), values=[node, ast.Constant(value=True)])
        elif (self.type_of_transformation == 2):
            # Apply a -> a or False transformation
            return ast.BoolOp(op=ast.Or(), values=[node, ast.Constant(value=False)])
        
        # Not a valid Idempotent transformation
        return node


class UnravelTernaryModifier(ast.NodeTransformer):
    '''
    In Python, a ternary operator is of the form [true_value] if [condition] else [false_value].
    
    This is synthetic sugar for the standard if-else clause. Thus, this class unravels a ternary
    operator into the standard if-else clause.

    Primarily, this class handles the transformations of the following situations:

    1. A ternary operator is used in a return statement.
        Original: def function_x(x): return True if x > 5 else False
        New: def function_x(x):
                 if x > 5:
                     return True
                 else:
                     return False

    2. A ternary operator is directly used in an assignment statement.
    Example:
        Original: def function_x(x): c = 2 if x > 5 else 3
        New: def function_x(x):
                if x > 5:
                    c = 2
                else:
                    c = 3
                
    3. A ternary operator is used as an operand in a binop of an assignment statement.
    Example:
        Original: def function_x(x): c = 2 + (3 if x > 5 else 1)
        New: def function_x(x):
            if (x > 5):
                c = 2 + 3
            else:
                c = 2 + 1

    '''

    def visit_Assign(self, node):
        """
        Handles situations where the ternary operator is either directly used in an
        assignment statement or as an operand in a bin op in an assignment statement.

        """
        # Case 1: The ternary operator is directly used in an assignment statement
        if isinstance(node.value, ast.IfExp):
            
            # Break down the ternary operator into its 3 components
            condition = node.value.test
            true_value = node.value.body
            false_value = node.value.orelse

            # Create the new assignment statement for the truth block
            true_assignment = ast.Assign(targets=node.targets, value=true_value)
            true_assignment.lineno = node.lineno
            true_assignment.col_offset = node.col_offset

            # Create the new assignment statement for the false block
            false_assignment = ast.Assign(targets=node.targets, value=false_value)
            false_assignment.lineno = node.lineno
            false_assignment.col_offset = node.col_offset

            # Combine the truth and false blocks into a single if-else clause
            combined_if_statement = ast.If(
                test=condition,
                body=[true_assignment],
                orelse=[false_assignment]
            )

            return combined_if_statement
    
        # Case 2: The ternary operator is used as an operand in a bin op that is found
        # in an assignment statement
        elif isinstance(node.value, ast.BinOp):
            # Get the current variable that is being assigned
            current_targets = node.targets

            # Get operator for bin op
            current_operator = node.value.op

            # Check if any of the operands is a ternary
            is_left_ternary = False
            is_right_ternary = False
            left_node = self.visit(node.value.left)
            right_node = self.visit(node.value.right)
            if isinstance(left_node, ast.IfExp):
                is_left_ternary = True
            if isinstance(right_node, ast.IfExp):
                is_right_ternary = True
            
            # Case 2a: None of the operands are ternary
            if (not is_left_ternary and not is_right_ternary):
                # Just return the original node
                return node
            
            # Case 2b: Left operand is ternary, right operand is not
            if (is_left_ternary and not is_right_ternary):
                # Transform left
                condition = left_node.test
                true_value = left_node.body
                false_value = left_node.orelse

                # Create new assignment statements
                assignment_if = ast.Assign(targets=current_targets,
                                           value=ast.BinOp(left=true_value, op=current_operator, right=right_node))
                assignment_if.lineno = node.lineno
                assignment_if.col_offset = node.col_offset
                assignment_else = ast.Assign(targets=current_targets,
                                             value=ast.BinOp(left=false_value, op=current_operator, right=right_node))
                assignment_else.lineno = node.lineno
                assignment_else.col_offset = node.col_offset
                

                # Create a new If statement with equivalent semantics
                if_statement = ast.If(
                    test=condition,
                    body=[assignment_if],
                    orelse=[assignment_else]
                )
                return if_statement

            # Case 2c: Left operand is not ternary, right operand is
            if (not is_left_ternary and is_right_ternary):
                # Transform right
                condition = right_node.test
                true_value = right_node.body
                false_value = right_node.orelse

                # Create new assignment statements
                assignment_if = ast.Assign(targets=current_targets,
                                           value=ast.BinOp(left=left_node, op=current_operator, right=true_value))
                assignment_if.lineno = node.lineno
                assignment_if.col_offset = node.col_offset
                assignment_else = ast.Assign(targets=current_targets,
                                             value=ast.BinOp(left=left_node, op=current_operator, right=false_value))
                assignment_else.lineno = node.lineno
                assignment_else.col_offset = node.col_offset
                

                # Create a new If statement with equivalent semantics
                if_statement = ast.If(
                    test=condition,
                    body=[assignment_if],
                    orelse=[assignment_else]
                )
                return if_statement

            # Case 2d: Both nodes are ternary
            if (is_left_ternary and is_right_ternary):
                # Transform left
                condition_left = left_node.test
                true_value_left = left_node.body
                false_value_left = left_node.orelse

                # Transform right
                condition_right = right_node.test
                true_value_right = right_node.body
                false_value_right = right_node.orelse


                # Create Boolean conditions for 4 combinations, since we have 2 ternary operators

                # Both conditions true
                boolean_condition_one = ast.BoolOp(op=ast.And(), values=[condition_left, condition_right])
                # Left true, right false
                boolean_condition_two = ast.BoolOp(op=ast.And(),
                                                   values=[condition_left, ast.UnaryOp(op=ast.Not(),operand=condition_right)])
                # Left false, right true
                boolean_condition_three = ast.BoolOp(op=ast.And(),
                                                     values=[ast.UnaryOp(op=ast.Not(), operand=condition_left),
                                                             condition_right])
                # Both conditions false
                boolean_condition_four = ast.BoolOp(op=ast.And(),
                                                    values=[ast.UnaryOp(op=ast.Not(), operand=condition_left),
                                                            ast.UnaryOp(op=ast.Not(), operand=condition_right)])
                

                # Create assignment statements
                assignment_one = ast.Assign(targets=current_targets,
                                            value=ast.BinOp(left=true_value_left, op=current_operator, right=true_value_right))
                assignment_one.lineno = node.lineno
                assignment_one.col_offset = node.col_offset
                assignment_two = ast.Assign(targets=current_targets,
                                            value=ast.BinOp(left=true_value_left, op=current_operator, right=false_value_right))
                assignment_two.lineno = node.lineno
                assignment_two.col_offset = node.col_offset
                assignment_three = ast.Assign(targets=current_targets,
                                              value=ast.BinOp(left=false_value_left, op=current_operator, right=true_value_right))
                assignment_three.lineno = node.lineno
                assignment_three.col_offset = node.col_offset
                assignment_four = ast.Assign(targets=current_targets,
                                             value=ast.BinOp(left=false_value_left, op=current_operator, right=false_value_right))
                assignment_four.lineno = node.lineno
                assignment_four.col_offset = node.col_offset


                # Create a new if-elif statement with equivalent semantics
                if_statement = ast.If(
                    test=boolean_condition_one,
                    body=[assignment_one],
                    orelse=[ast.If(
                        test=boolean_condition_two,
                        body=[assignment_two],
                        orelse=[ast.If(
                            test=boolean_condition_three,
                            body=[assignment_three],
                            orelse=[ast.If(
                                test=boolean_condition_four,
                                body=[assignment_four],
                                orelse=[]
                                )
                            ]
                        )]
                    )]
                )
                return if_statement

        # Case 3: We do not handle other cases
        else:
            return node
    
   
    def visit_Return(self, node):
        """
        Handles situations where the ternary operator is used in a return statement

        """
        # Check if the value of the return statement is a ternary
        if isinstance(node.value, ast.IfExp):
            # Extract parts of the ternary expression
            condition = node.value.test
            true_value = node.value.body
            false_value = node.value.orelse

            # Create a new If statement with equivalent semantics
            if_statement = ast.If(
                test=condition,
                body=[ast.Return(value=true_value)],
                orelse=[ast.Return(value=false_value)]
            )

            # Return the transformed If statement
            return if_statement

        return node
