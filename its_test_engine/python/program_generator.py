"""
Subclasses that extend concrete base program generators, specially for Python programs
"""
import ast
from its_test_engine.base.program_generator import (
    LeetCodeProgramGenerator,
    OpenAiProgramGenerator,
)


class LeetCodePythonProgramGenerator(LeetCodeProgramGenerator):
    """
    LeetCodeProgramGenerator that generates Python programs
    """
    def __init__(self):
        """
        Initialises a LeetCodePythonProgramGenerator
        """
        super().__init__(language="python")

    def _get_function_name(self, code: str):
        """
        Helper function that obtains function name for a function

        Parameters:
            code: Program string for a Python program
        """
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name

        return None


class OpenAIPythonProgramGenerator(OpenAiProgramGenerator):
    """
    OpenAIProgramGenerator that generates Python programs
    """
    def __init__(self, constraints=None):
        """
        Initialises an OpenAIPythonProgramGenerator

        Parameters:
            constraints: Constraints to guide the model in producing
            a base program
        """
        super().__init__(language="python", constraints=constraints)
