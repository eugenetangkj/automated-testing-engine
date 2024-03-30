"""
    This class represents a test result object obtained from the tester class
"""

import os
import json
import hashlib
from datetime import datetime
from its_test_engine.enums import Language


class ItsTestSuite:
    steps = {
        "parser": 1,
        "interpreter": 2,
        "error_localizer": 3,
        "feedback_error": 4,
        "feedback_fix": 5,
        "repair": 6,
    }

    def __init__(
        self,
        language: Language,
        endpoint: str,
        base_program_string: str,
    ):
        assert endpoint in self.steps, f"Invalid endpoint: {endpoint}"
        self.step = self.steps[endpoint]
        self.endpoint = endpoint
        self.language = language
        self.base_program_string = base_program_string.strip("\n")
        self.time = datetime.now()

        self.test_cases = []

    def add_test_case(self, test_case):
        self.test_cases.append(test_case)

    def is_success(self):
        for test_case in self.test_cases:
            if not test_case.is_success():
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
    def __init__(
        self,
        success,
        endpoint,
        message,
        request_payload=None,
        actual_output=None,
    ):
        self.success = success
        self.endpoint = endpoint
        self.message = message
        self.actual_output = (
            json.dumps(actual_output, indent=4) if actual_output else None
        )
        self.request_body = (
            json.dumps(request_payload, indent=4) if request_payload else None
        )


class ItsTestSuitesMarkdownWriter:

    def __init__(self, test_result_dir):
        self._test_result_dir = test_result_dir
        self._test_results = []

        folder_path = os.path.join(self._test_result_dir)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def write(self, test_suite: ItsTestSuite):
        folder_path = os.path.join(self._test_result_dir)

        h = hashlib.new("sha256")
        h.update(test_suite.base_program_string.encode())
        hash_value = h.hexdigest()

        file_name = f"{hash_value[:8]}_{test_suite.step}_{test_suite.endpoint}"
        file_name += f"_{'pass' if test_suite.is_success() else 'fail'}.md"
        file_path = os.path.join(folder_path, file_name)

        markdown = "# Test Report\n\n"
        markdown += f"Time: {test_suite.time}\n\n"
        markdown += "### Base Program\n\n"
        markdown += (
            f"```{test_suite.language.value}\n{test_suite.base_program_string}\n```\n\n"
        )

        for index, test_case in enumerate(test_suite.test_cases):
            markdown += f"## Test Case {index + 1}\n\n"

            markdown += "### Modified Program\n\n"
            markdown += (
                f"```{test_suite.language.value}\n{test_case.modified_program}\n```\n\n"
            )

            for result in test_case.results:
                markdown += "<details>\n"

                markdown += "<summary>"
                markdown += f"{result.endpoint} endpoint: "
                markdown += f"{'passed ✅' if result.success else 'failed ❌'}"
                markdown += "</summary>\n\n"

                markdown += f"Message: \n```\n{result.message}\n```\n\n"

                if result.request_body:
                    markdown += (
                        f"Request Body: \n```json\n{result.request_body}\n```\n\n"
                    )
                else:
                    markdown += "Request Body: None\n\n"

                if result.actual_output:
                    markdown += (
                        f"Actual Output: \n```json\n{result.actual_output}\n```\n\n"
                    )
                else:
                    markdown += "Actual Output: None\n\n"

                markdown += "</details>\n\n"

        with open(file_path, "w") as file:
            file.write(markdown)

    def bulk_write(self, test_suites: list[ItsTestSuite]):
        # Create directory if not exists
        folder_path = os.path.join(self._test_result_dir)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        for test_suite in test_suites:
            self.write(test_suite)
