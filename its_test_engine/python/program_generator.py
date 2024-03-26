import os
import re
import ast
import json
import random
from its_test_engine.base.program_generator.leetcode_program_generator import (
    LeetCodeProgramGenerator,
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
