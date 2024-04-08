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

    def visit_BoolOp(self, node):
        # Apply the idempotent transformation to each operand of the BoolOp
        transformed_operands = []
        for value in node.values:
            transformed_operands.append(self._apply_idempotent_law(value))
        
        # Return a new BoolOp node with transformed operands
        return ast.BoolOp(op=node.op, values=transformed_operands)

    def _apply_idempotent_law(self, node):
        # Apply the idempotent transformation to a single node
        if isinstance(node, ast.Name):
            if self.type_of_transformation == 1:
                return ast.BoolOp(op=ast.And(), values=[node, node])
            elif self.type_of_transformation == 2:
                return ast.BoolOp(op=ast.Or(), values=[node, node])
        
        # Not a case to handle
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


    def visit_BoolOp(self, node):
        # Apply the idempotent transformation to each operand of the BoolOp
        transformed_operands = []
        for value in node.values:
            transformed_operands.append(self._apply_idempotent_law(value))
        
        # Return a new BoolOp node with transformed operands
        return ast.BoolOp(op=node.op, values=transformed_operands)

    def _apply_idempotent_law(self, node):
        # Apply the idempotent transformation to a single node
        if isinstance(node, ast.Name):
            if self.type_of_transformation == 1:
                # Apply a -> a and True transformation
                return ast.BoolOp(op=ast.And(), values=[node, ast.Constant(value=True)])
            elif self.type_of_transformation == 2:
                # Apply a -> a or False transformation
                return ast.BoolOp(op=ast.Or(), values=[node, ast.Constant(value=False)])
        
        # Not a case to handle
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


class ForRangeToWhileLoopModifier(ast.NodeTransformer):
    """
    This class transforms a for ... in range(...) loop into a while loop that has
    the same semantics. It uses the documentation of the range(...) in Python to
    determine how to break down the start, stop and step values.

    Example: Both programs equivalently increment i by 3 every iteration
        Base:
            for i in range(0, 6, 2):
                i = i + 1
                call_func()
        Modified:
            i = 0
            while i < 6:
                i = i + 1
                call_func()
                i = i + 2
    """
    def visit_For(self, node):
        # We want to detect if the range() function is used as the iterator in a for loop
        is_iterator_a_function_call = isinstance(node.iter, ast.Call)
        is_iterator_a_simple_function = isinstance(node.iter.func, ast.Name)
        is_iterator_range_function = node.iter.func.id == "range"

        if (is_iterator_a_function_call and
            is_iterator_a_simple_function and
            is_iterator_range_function):
            # The current for loop indeed uses the range() function as an iterator

            # Get the loop variable
            loop_variable = node.target

            # Decompose the arguments used in the range function
            arguments_of_range_function = node.iter.args
            # Case 1: Only 1 argument
            if (len(arguments_of_range_function) == 1):
                start_value = ast.Constant(n = 0) # Default start = 0
                stop_value = arguments_of_range_function[0]
                step_value = ast.Constant(n = 1) # Default step = 1
            # Case 2: 2 arguments
            elif (len(arguments_of_range_function) == 2):
                start_value = arguments_of_range_function[0]
                stop_value = arguments_of_range_function[1]
                step_value = ast.Constant(n = 1) # Default step = 1
            # Case 3: 3 arguments
            elif (len(arguments_of_range_function) == 3):
                start_value = arguments_of_range_function[0]
                stop_value = arguments_of_range_function[1]
                step_value = arguments_of_range_function[2]
            

            # We need to create an initialisation statement to initialise the
            # variable in the while loop, since the initialisation statement
            # was not required in the for loop
            initialisation_statement = ast.Assign(
                targets=[loop_variable],
                value=start_value
            )
            initialisation_statement.lineno = node.lineno
            initialisation_statement.col_offset = node.col_offset


            # Determine operator to use in the while loop, depending on arguments in range()
            if isinstance(step_value, ast.UnaryOp):
                while_loop_operator = ast.Gt() if isinstance(step_value.op, ast.USub) else ast.Lt()
            elif isinstance(step_value, ast.Constant):
                while_loop_operator = ast.Gt() if step_value.value < 0 else ast.Lt()

            
            # Create the new while loop
            new_while_loop = ast.While(
                test=ast.Compare(
                    left=loop_variable,
                    ops=[while_loop_operator],
                    comparators=[stop_value]
                ),
                body=[],
                orelse=[]
            )

            # Add body of for loop into while loop
            new_while_loop.body.extend(node.body)

            # Add increment statement at the end of the body of the
            # while loop to simulate changing of the loop variable,
            # which was done internally within the range() function.
            loop_variable_assignment_statement = ast.Assign(
                targets=[loop_variable],
                value=ast.BinOp(
                    left=loop_variable,
                    op=ast.Add(), # Includes handling of negative step values
                    right=step_value
                )
            )
            loop_variable_assignment_statement.lineno = node.lineno
            while_loop_operator.col_offset = node.col_offset
            new_while_loop.body.append(loop_variable_assignment_statement)
            

            # Return the combination of the initialisation statement and new while loop
            return [initialisation_statement, new_while_loop]

        else:
            # Cases we do not handle
            return node


class ExtraArgumentReassignmentModifier(ast.NodeTransformer):
    """
    This class reassigns the arguments of a function to itself multiple
    times at the start of the function. The number of times the assignment
    is done per argument can be set in the __init__ method, with default value
    of 5 times per argument.

    Example:
        Base:
            def main(x, y):
                sum = x + y
                return sum
        Modified:
            def main(x, y):
                x = x
                x = x
                x = x
                x = x
                x = x
                y = y
                y = y
                y = y
                y = y
                y = y
                sum = x + y
                return sum
    """
    def __init__(self, number_of_repeats=5):
        '''
        Parameters:
            number_of_repeats: Number of times each argument is assigned
        '''
        super().__init__()
        self.number_of_repeats = number_of_repeats


    def visit_FunctionDef(self, node):
        # Obtain arguments of function
        arguments = node.args.args

        # Create assignment statements for arguments
        argument_assignment_statements = []
        for argument in arguments:
            for i in range(self.number_of_repeats):
                # Create new assignment statement
                new_assignment_statement = ast.Assign(
                    targets=[ast.Name(id=argument.arg, ctx = ast.Store())],
                    value=ast.Name(id=argument.arg, ctx=ast.Load())
                ) 
                new_assignment_statement.lineno = node.lineno

                # Add new assignment statement to list
                argument_assignment_statements.append(
                    new_assignment_statement
                )
        
        # Add all the assignment statements to the start of the function
        node.body = argument_assignment_statements + node.body
        return node


class SwapArgumentsModifier(ast.NodeTransformer):
    """
    This class swaps the arguments internally within a function and
    replaces the arguments with the function body accordingly.

    Example:
        Base:
            def main(a, b, c):
                output = c - b + a
                return output
        Modified:
            def main(a, b, c):
                (a, b, c) = (c, b, a)
                output = a - b + c
                return output
    """

    def visit_FunctionDef(self, node):
        # Get the names of the arguments in the function
        names_of_arguments = [argument.arg for argument in node.args.args]
        number_of_arguments = len(names_of_arguments)
        
        # Create the tuple assignment statement to swap the values of the arguments
        tuple_original = ast.Tuple(
            elts=[ast.Name(id=names_of_arguments[i], ctx=ast.Store()) for i in range(number_of_arguments)],
            ctx=ast.Store())
        tuple_reversed = ast.Tuple(
            elts=[ast.Name(id=names_of_arguments[-i - 1], ctx=ast.Load()) for i in range(number_of_arguments)],
            ctx=ast.Load())
        tuple_assignment_statement = ast.Assign(
            targets=[tuple_original],
            value=tuple_reversed
        )
        tuple_assignment_statement.lineno = node.lineno
        
        # Insert the new assignment statement at the beginning of the function body
        node.body.insert(0, tuple_assignment_statement)
        
        # Store the original argument names and their swapped names
        # Need for retrieval when swapping variables later on
        self.argument_names_original = names_of_arguments
        self.argument_names_reversed = [names_of_arguments[- i - 1] for i in range(number_of_arguments)]
        
        # Visit the function to replace variables
        self.generic_visit(node)
        
        return node

    def visit_Name(self, node):
        # Replace arguments with the new mapped arguments
        if isinstance(node.ctx, ast.Load) and node.id in self.argument_names_original:
            # The current name is one of the arguments that we have to do swapping

            # Get new argument information
            index_in_original_tuple = self.argument_names_original.index(node.id)
            id_of_new_argument = self.argument_names_reversed[index_in_original_tuple]

            # Create new node for the mapped argument
            new_name_node = ast.Name(id=id_of_new_argument, ctx=node.ctx)
            return ast.copy_location(new_name_node, node)
        
        return node

    def visit_Assign(self, node):
        # We do not want to replace the variables in the newly inserted tuple statement
        # If we visit it, we ignore it and not perform any swapping
        if isinstance(node.targets[0], ast.Tuple):
            return node
        
        # Not the original tuple, visit as per normal
        else:
            return self.generic_visit(node)


class WrapInIfTrueModifier(ast.NodeTransformer):
    """
    This class wraps the body of a function inside an If: True
    block.

    Example:
        Base:
            def main(a, b, c):
                sum = a + b + c
                return sum
        Modified:
            def main(a, b, c):
                if True:
                    sum = a + b + c
                    return sum
                
    """

    def visit_FunctionDef(self, node):
        # Create the new if block
        new_if_block = ast.If(
            test=ast.Constant(value=True),
            body=node.body,
            orelse=[]
        )

        # Assign this new if block as body of function
        node.body = [new_if_block]

        # Return output
        return node


class WrapInTryBlockModifier(ast.NodeTransformer):
    """
    This class wraps the body of a function inside a Try
    block, and includes an Except block that should not run,
    but returns 1 for the sake of program completeness.

    The condition is that the wrapped function should never
    throw an exception, for it be semantically equivalent to
    the base program.

    Example:
        Base:
            def main(a, b, c):
                sum = a + b + c
                return sum
        Modified:
            def main(a, b, c):
                try:
                    sum = a + b + c
                    return sum
                except:
                    return 1
                
    """

    def visit_FunctionDef(self, node):
        # Create a placeholder Except block with default return statement returning 1
        new_return_statement = ast.Return(
            value=ast.Constant(value=1)
        )

        # Create an Except block with the return statement
        new_except_block = ast.ExceptHandler(
            type=None,
            name=None,
            body=[new_return_statement]
        )

        # Create a Try block with the function wrapped in it
        new_try_block = ast.Try(
            body=node.body,
            handlers=[new_except_block],
            orelse=[],
            finalbody=[]
        )

        # Update the existing function
        node.body = [new_try_block]

        return node


class WrapInExceptBlockModifier(ast.NodeTransformer):
    """
    This class wraps the body of a function inside an Except
    block, and includes a Try block that raises an exception so
    the control flow goes to the Except block.

    Example:
        Base:
            def main(a, b, c):
                sum = a + b + c
                return sum
        Modified:
            def main(a, b, c):
                try:
                    raise Exception
                except:
                    sum = a + b + c
                    return sum       
    """

    def visit_FunctionDef(self, node):
       # Create a new Except block with the body of the original function
       new_except_block = ast.ExceptHandler(
           type=None,
           name=None,
           body=node.body
       )
       
       # Create a new Try block that raises an exception
       # Add the new Except block as the except handler for this Try block
       new_raise_exception_statement = ast.Raise(
           exc=ast.Name(id="Exception", ctx=ast.Load())
       )
       new_try_block = ast.Try(
           body=[new_raise_exception_statement],
           handlers=[new_except_block],
           orelse=[],
           finalbody=[]
       )

       # Return updated node
       node.body = [new_try_block]
       return node
    

class ReverseListModifier(ast.NodeTransformer):
    """
    This class reverses lists defined within functions and for list
    accesses, it retrieves the correct items by using an updated
    index.

    Note that it only works if all the indices of lists found in
    the function are either integer constants or single variables.
    For example, lst[2] or lst[x], but not lst[x + 2].

    Example:
        Base:
            def func():
                curr_list = [1, 2, 3, 4, 5]
                result = curr_list[0] + curr_list[1] + curr_list[2]
                return result

        Modified:
            def func():
                curr_list = [5, 4, 3, 2, 1]
                result = curr_list[4] + curr_list[3] + curr_list[2]
                return result
    """

    def __init__(self):
        '''
            Creates a dictionary to keep track of list variables and their
            associated lengths.
            
        '''
        super().__init__()
        self.list_lengths = {}


    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Name):
            # Retrieve the name of the Name node
            target_name = node.targets[0].id

            # Check if the assigned value is a list
            if isinstance(node.value, ast.List):
                # Set an attribute to keep track of the current list variable name
                self.current_list_name = target_name

        # Visit the assignment statement
        self.generic_visit(node)
        return node


    def visit_List(self, node):
        # For list variables, we store the list name and the length of the list
        # in the dictionary as we need it to update the indices later
        self.list_lengths[self.current_list_name] = len(node.elts)

        # Reverse the list
        node.elts = node.elts[::-1]

        # Return reversed list
        return node
    

    def visit_Subscript(self, node):
        # Get the name of the collection that this subscript is associated with
        parent_node = node.value

        # Check that this subscript is associated with a list that has its length
        # stored in the dictionary
        if (parent_node.id in self.list_lengths):
            # Update the value of the subscript
            length_of_list = self.list_lengths[parent_node.id]

            if (isinstance(node.slice, ast.Name)):
               # Index is a single variable

               # Get new index node
               constant_node = ast.Constant(value=length_of_list - 1)
               negated_original_node = ast.UnaryOp(
                   op=ast.USub(),
                   operand=node.slice
                )
               new_index_node = ast.BinOp(
                   left=negated_original_node,
                   op=ast.Add(),
                   right=constant_node
               )
               
               # Create new subscript node
               new_subscript_node = ast.Subscript(
                   value=parent_node,
                   slice=ast.Index(value=new_index_node),
                   ctx=node.ctx
               )

               return new_subscript_node
               
            elif (isinstance(node.slice, ast.Constant)):
                # Index is a constant integer

                # Get new index node
                constant_node = ast.Constant(
                    value=length_of_list - node.slice.value - 1
                )

                # Create new subscript node
                new_subscript_node = ast.Subscript(
                   value=parent_node,
                   slice=constant_node,
                   ctx=node.ctx
                )

                return new_subscript_node
        
        # Return the updated node
        return node
