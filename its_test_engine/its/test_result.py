"""
    This class represents a test result object obtained from the tester class
"""

import os
import hashlib
from datetime import datetime
from its_test_engine.enums import Language


class ItsTestSuite:
    def __init__(
        self,
        language: Language,
        base_program_string: str,
        inputs: list[any],
    ):
        self.inputs = inputs
        self.language = language
        self.base_program_string = base_program_string.strip("\n")
        self.time = datetime.now()

        self.test_cases = []
        self.parser_result = None
        self.interpreter_result = None

    def set_parser_result(self, parser_result):
        self.parser_result = parser_result

    def set_interpreter_result(self, interpreter_result):
        self.interpreter_result = interpreter_result

    def add_test_case(self, test_case):
        self.test_cases.append(test_case)

    def is_success(self):
        for test_case in self.test_cases:
            if not test_case.is_success():
                return False

        if self.parser_result is not None and not self.parser_result.success:
            return False

        if self.interpreter_result is not None and not self.interpreter_result.success:
            return False

        return True


class ItsTestCase:
    def __init__(self, modified_program):
        self.modified_program = modified_program
        self.results = []

    def add_result(self, result):
        self.results.append(result)

    def is_success(self):
        for result in self.results:
            if not result.success:
                return False

        return True


class ItsTestResult:
    def __init__(self, success, endpoint, message, actual_output):
        self.success = success
        self.endpoint = endpoint
        self.message = message
        self.actual_output = actual_output


class ItsTestSuitesMarkdownWriter:

    def __init__(self, test_result_dir):
        self._test_result_dir = test_result_dir
        self._test_results = []

    def write(self, test_suites: list[ItsTestSuite]):
        # Create directory if not exists
        folder_path = os.path.join(self._test_result_dir)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for index, test_suite in enumerate(test_suites):
            h = hashlib.new("sha256")
            h.update(test_suite.base_program_string.encode())
            hash_value = h.hexdigest()

            test_num = f"{index+1:02d}"
            file_name = f"{hash_value[:8]}_test_{test_num}_{'pass' if test_suite.is_success() else 'fail'}.md"
            file_path = os.path.join(folder_path, file_name)

            markdown = f"# Test {test_num}\n\n"
            markdown += f"Time: {test_suite.time}\n\n"
            markdown += "### Base Program\n\n"
            markdown += f"```{test_suite.language.value}\n{test_suite.base_program_string}\n```\n\n"
            markdown += "### Input\n\n"
            markdown += f"```json\n{test_suite.inputs}\n```\n\n"

            if test_suite.parser_result:
                markdown += f"<details>\n"
                markdown += f"<summary>"
                markdown += "Parser Result: "
                markdown += f"{'Passed ✅' if test_suite.parser_result.success else 'Failed ❌'}"
                markdown += "</summary>\n\n"
                markdown += (
                    f"Message: \n```\n{test_suite.parser_result.message}\n```\n\n"
                )
                markdown += f"Actual Output: \n```json\n{test_suite.parser_result.actual_output}\n```\n\n"
                markdown += "</details>\n\n"

            if test_suite.interpreter_result:
                markdown += f"<details>\n"
                markdown += f"<summary>"
                markdown += "Interpreter Result: "
                markdown += f"{'Passed ✅' if test_suite.interpreter_result.success else 'Failed ❌'}"
                markdown += "</summary>\n\n"
                markdown += (
                    f"Message: \n```\n{test_suite.interpreter_result.message}\n```\n\n"
                )
                markdown += f"Actual Output: \n```json\n{test_suite.interpreter_result.actual_output}\n```\n\n"
                markdown += "</details>\n\n"

            for index, test_case in enumerate(test_suite.test_cases):
                markdown += f"## Test Case {index + 1}\n\n"

                markdown += "### Modified Program\n\n"
                markdown += f"```{test_suite.language.value}\n{test_case.modified_program}\n```\n\n"

                for result in test_case.results:
                    markdown += "<details>\n"

                    markdown += f"<summary>"
                    markdown += f"{result.endpoint} endpoint: "
                    markdown += f"{'passed ✅' if result.success else 'failed ❌'}"
                    markdown += "</summary>\n\n"

                    markdown += f"Message: \n```\n{result.message}\n```\n\n"
                    if result.actual_output:
                        markdown += (
                            f"Actual Output: \n```json\n{result.actual_output}\n```\n\n"
                        )
                    else:
                        markdown += "Actual Output: None\n\n"

                    markdown += "</details>\n\n"

            with open(file_path, "w") as file:
                file.write(markdown)
