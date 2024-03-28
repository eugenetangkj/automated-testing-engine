import os
import re
import json
import random
from its_test_engine.base.program_generator.base_program_generator import (
    BaseProgramGenerator,
)


class LeetCodeProgramGenerator(BaseProgramGenerator):

    types_mapping = {
        "int": "int",
        "float": "float",
        "double": "float",
        "string": "str",
        "char": "str",
        "int[]": "List[int]",
        "float[]": "List[float]",
        "double[]": "List[float]",
        "string[]": "List[str]",
        "char[]": "List[str]",
        "List<String>": "List[str]",
        "List<Integer>": "List[int]",
        "List<Float>": "List[float]",
        "List<Double>": "List[float]",
    }

    def __init__(self, language: str):
        super().__init__()
        self.language = language
        self.file = open(
            os.path.join(
                os.path.dirname(__file__),
                "../../../datasets/" "leetcode-solutions.jsonl",
            ),
            "r",
        )
        self.lines = self.file.readlines()
        self.file.close()

        self.question_ids = set()

    def get_function_signatures(self, question):
        java_solution = question["answer"]["java"]

        function_signature_regex = r"public\s+([^\s]+)\s+([^\(]+)\(([^)]+)\)"

        match = re.search(function_signature_regex, java_solution)

        fs = {
            "arguments": [],
            "return_type": None,
        }

        if match:
            return_type = match.group(1)
            function_name = match.group(2)
            arguments = match.group(3)

            if return_type not in self.types_mapping:
                return None

            return_type = self.types_mapping[return_type]

            for arg in arguments.split(","):
                arg_type, arg_name = arg.strip().split(" ")
                if arg_type not in self.types_mapping:
                    return None

                fs["arguments"].append(self.types_mapping[arg_type])

            fs["return_type"] = return_type
            return fs
        return None

    def _get_function_name(self, code: str):
        #Assumes Python for now
        start_index = code.index('def') + 3
        end_index = code.index('(')

        # Extract the substring between 'def' and '('
        function_name = code[start_index:end_index].strip()
        return function_name


    def generate_test_case(self):
        # open leetcode-solutions.jsonl file and read random line
        line = random.randint(0, len(self.lines) - 1)
        while line in self.question_ids:
            line = random.randint(0, len(self.lines) - 1)

        question = self.lines[line]
        question = json.loads(question)

        while self.get_function_signatures(question) is None:
            line = random.randint(0, len(self.lines) - 1)
            question = self.lines[line]
            question = json.loads(question)

        func = question["answer"][self.language]

        func = func.replace("```" + self.language, "").replace("```", "")

        print(func)

        signature = self.get_function_signatures(question)

        signature["name"] = self._get_function_name(func)

        return signature, func
