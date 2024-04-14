'''
Generates a base program by randomly picking from a set of LeetCode solutions.

It uses the leetcode dataset by Eric Hartford and RobyBerty on https://www.kaggle.com/datasets/erichartford/leetcode-solutions.
The license for the dataset is GNU Lesser General Public License.
'''

import os
import re
import json
import random
from .base_program_generator import BaseProgramGenerator


class LeetCodeProgramGenerator(BaseProgramGenerator):

    types_mapping = {
        "int": "int",
        "float": "float",
        "double": "float",
        # "String": "str", disabled because the inputs need to be in specific format
        "boolean": "bool",
        "List<Integer>": "List[int]",
        # "List<String>": "List[str]", disabled because the inputs need to be in specific format
        "List<Float>": "List[float]",
        "List<Double>": "List[float]",
        "List<Boolean>": "List[bool]",
        "int[]": "List[int]",
        "float[]": "List[float]",
        "double[]": "List[float]",
        # "String[]": "List[str]", disabled because the inputs need to be in specific format
        "boolean[]": "List[bool]",
    }

    def __init__(self, language: str):
        """
        Initialises a LeetCodeProgramGenerator instance.

        Parameters:
            language: Language of the base program that we wish to generate for
        
        """
        super().__init__()
        self.language = language
        self.file = open(
            os.path.join(
                os.path.dirname(__file__),
                "../../../datasets/",
                "leetcode-solutions.jsonl",
            ),
            "r",
        )
        self.lines = self.file.readlines()
        self.file.close()

        self.question_ids = set()

    def get_function_signatures(self, question):
        """
        Helper function that retrieves the function signature of a function. It works by accessing
        the Java version of the same function, which is available in the dataset.

        Parameters:
            question: The question that contains the Java and Python solution that we wish
            to obtain the function signature of.

        """
        java_solution = question["answer"]["java"]

        function_signature_regex = r"public\s+([^\s]+)\s+([^\(]+)\(([^)]+)\)"

        match = re.search(function_signature_regex, java_solution)

        fs = {
            "argument_types": [],
            "return_type": None,
        }

        if match:
            return_type = match.group(1)
            arguments = match.group(3)

            if return_type not in self.types_mapping:
                return None

            return_type = self.types_mapping[return_type]

            for arg in arguments.split(","):
                arg_type, _ = arg.strip().split(" ")
                if arg_type not in self.types_mapping:
                    return None

                fs["argument_types"].append(self.types_mapping[arg_type])

            fs["return_type"] = return_type
            return fs
        return None


    def _get_function_name(self, code: str):
        """
        Helper function that retrieves the name of a function given a string containing
        a Python function.

        Parameters:
            code: String containing the Python function
        """
        # Assumes Python for now
        start_index = code.index("def") + 3
        end_index = code.index("(")

        # Extract the substring between 'def' and '('
        function_name = code[start_index:end_index].strip()
        return function_name


    def generate_test_case(self):
        """
        Randomly selects a Python function from the Leetcode dataset, returning
        its function signature and program string
        
        """
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

        signature = self.get_function_signatures(question)

        signature["name"] = self._get_function_name(func)

        return signature, func
