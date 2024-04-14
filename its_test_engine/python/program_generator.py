import ast
from its_test_engine.base.program_generator import (
    LeetCodeProgramGenerator,
    OpenAiProgramGenerator,
)


class LeetCodePythonProgramGenerator(LeetCodeProgramGenerator):
    def __init__(self):
        super().__init__(language="python")

    def _get_function_name(self, code: str):
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name

        return None


class OpenAIPythonProgramGenerator(OpenAiProgramGenerator):
    def __init__(self, constraints=None):
        super().__init__(language="python", constraints=constraints)
