"""
Randomly generate arguments using PyGuin for maximum branch coverage.
Referenced https://pynguin.readthedocs.io/en/latest/user/intro.html for documentation.
"""

import random
import os
import ast
import subprocess


def add_print_to_functions(code):
    """
    Tester function to check if PyGuin is working as expected.

    Parameters:
        code: Base program string
    """
    # Parse the code into an AST
    tree = ast.parse(code)

    # Create a NodeTransformer to modify the AST
    class PrintTransformer(ast.NodeTransformer):
        # pylint: disable=invalid-name
        def visit_FunctionDef(self, node):
            # Get the list of argument names
            arg_names = [arg.arg for arg in node.args.args]

            # Create a print statement to display the argument values
            print_node = ast.Expr(
                value=ast.Call(
                    func=ast.Name(id="print", ctx=ast.Load()),
                    args=[
                        ast.Str(s="__arguments__"),
                        ast.List(
                            elts=[
                                ast.Name(id=name, ctx=ast.Load()) for name in arg_names
                            ],
                        ),
                    ],
                    keywords=[],
                )
            )

            # Insert the print statement at the beginning of the function body
            node.body.insert(0, print_node)

            self.generic_visit(node)
            return node

    # Create an instance of the PrintTransformer
    transformer = PrintTransformer()

    # Transform the AST
    modified_tree = transformer.visit(tree)

    # Convert the modified AST back to code
    modified_code = ast.unparse(modified_tree)

    return modified_code


class PynGuinArgumentGenerator:
    
    def __init__(self, code: str):
        """
        Initialises a PynGuinArgumentGenerator instance.

        Parameters:
            code: Base program string to generate arguments for
        """
        self.code = code
        folder_path = os.path.join("/tmp", str(random.randint(0, 1000000)))
        os.makedirs(folder_path)

        # write code to file
        code_path = os.path.join(folder_path, "example.py")
        open(code_path, "w").write(code)

        self.code_path = code_path
        self.folder_path = folder_path

    def generate_arguments(self):
        """
        Generates arguments to maximise coverage.
        """

        try:
            result = subprocess.check_output(
                [
                    "pynguin",
                    f"--project-path={self.folder_path}",
                    "--module-name=example",
                    f"--output-path={self.folder_path}",
                    "--algorithm=MOSA",
                    "--maximum-search-time=10",
                    "--seed=202403013213",
                    # Ref: https://github.com/se2p/pynguin/issues/37
                    "--none-weight=0.1",
                    "--any-weight=0.9",
                ],
                timeout=12,
            )
        except subprocess.CalledProcessError as e:
            print(e)
            return []
        except subprocess.TimeoutExpired as e:
            print(e)
            return []

        if not os.path.exists(os.path.join(self.folder_path, "test_example.py")):
            return []

        modified_code = add_print_to_functions(self.code)

        # Rename the old file
        os.rename(self.code_path, os.path.join(self.folder_path, "example2.py"))

        modified_code_path = os.path.join(self.folder_path, "example.py")
        open(modified_code_path, "w").write(modified_code)

        output_path = os.path.join(self.folder_path, "test_example.py")
        result = subprocess.run(
            ["pytest", "-s", output_path], stdout=subprocess.PIPE, check=True
        )

        # Replace back the original code
        # os.rename(os.path.join(self.folder_path, "example2.py"), self.code_path)

        # Parse the arguments
        arguments = []

        for line in result.stdout.decode().split("\n"):
            if "__arguments__" in line:
                try:
                    argument = eval(line.split("__arguments__ ")[1])
                    arguments.append(argument)
                except Exception as e:
                    print(e)

        return arguments
