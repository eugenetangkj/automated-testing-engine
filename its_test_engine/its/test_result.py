"""
    This contains the classes responsible for encapsulating information about
    test cases and for writing test cases to Markdown files.
"""

import os
import json
import hashlib
from datetime import datetime
from its_test_engine.enums import Language
import pytz


class ItsTestSuite:
    """
    Represents a set of test cases
    """
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
        """
        Initialises a ItsTestSuite instance.

        Parameters:
            language: Language of program that we are testing
            endpoint: Which endpoint is the test case for
            base_program_string: Program string of base program
        """
        assert endpoint in self.steps, f"Invalid endpoint: {endpoint}"
        self.step = self.steps[endpoint]
        self.endpoint = endpoint
        self.language = language
        self.base_program_string = base_program_string.strip("\n")

        # Convert time to Singapore timezone
        utc_time = datetime.now(datetime.UTC)
        singapore_timezone = pytz.timezone('Asia/Singapore')
        now_sgt = utc_time.replace(tzinfo=pytz.utc).astimezone(singapore_timezone)

        self.time = now_sgt

        self.test_cases = []

    def add_test_case(self, test_case):
        """
        Adds a test case to this test suite.

        Parameters:
            test_case: Test case to add
        """
        self.test_cases.append(test_case)

    def is_success(self):
        """
        Determines if the entire test suite is successful or not. Not successful
        if any 1 of the test cases in the test suite is not successful.

        """
        for test_case in self.test_cases:
            if not test_case.is_success():
                return False

        return True


class ItsTestCase:
    """
    Represents 1 test case
    """
    def __init__(self, modified_program):
        """
        Initialises an ItsTestCase instance.

        Parameters:
            modified_program: Program string of modified program
        """
        self.modified_program = modified_program
        self.results = []

    def add_result(self, result):
        """
        Add a result to this test case

        Parameters:
            result: Result to be added
        """
        self.results.append(result)

    def is_success(self):
        """
        Determines if the test case is successful or not. If any 1
        of the results within the test case is not successful,
        the test case is considered not successful.
        """
        for result in self.results:
            if not result.success:
                return False

        return True


class ItsTestResult:
    """
    Represents a test result when testing against one specific endpoint.
    """
    def __init__(
        self,
        success,
        endpoint,
        message,
        request_payload=None,
        actual_output=None,
    ):
        """
        Initialises an ItsTestResult instance.

        success: Status of test result, whether pass or not
        endpoint: Which endpoint we are testing against
        message: Message from endpoint tester
        request_payload: Input to the API endpoint
        actual_output: Output from the API endpoint
        """
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
    """
    This class is responsible for writing the results of a test suite
    to Markdown files.
    """

    def __init__(self, test_result_dir):
        """
        Initialises an ItsTestSuitesMarkdownWriter.

        Parameters:
            test_result_dir: The location to write the results to
        """
        self._test_result_dir = test_result_dir
        self._test_results = []

        folder_path = os.path.join(self._test_result_dir)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def write(self, test_suite: ItsTestSuite):
        """
        Writes an ITS test suite to a Markdown file.

        Parameters:
            test_suite: The test suite to be written
        """
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

                if result.request_body:
                    markdown += (
                        f"Request Body: \n```json\n{result.request_body}\n```\n\n"
                    )
                else:
                    markdown += "Request Body: None\n\n"

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

    def bulk_write(self, test_suites: list[ItsTestSuite]):
        """
        Helper function that can write multiple test suites to different files

        Parameters:
            test_suites: List of test suites to be written to files
        """
        for test_suite in test_suites:
            self.write(test_suite)
