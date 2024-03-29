'''
    This class is responsible for using base and modified programs to test the ITS API
'''

from json.decoder import JSONDecodeError
from ..enums.type_of_test_result import TypeOfTestResult
from .its_api_connection import ItsApiConnection
from .test_result import TestResult
from ..base.input_generator import BaseInputGenerator
from ..utils import process_arguments
from .error_localizer_endpoint_tester import ErrorLocalizerEndpointTester
from .feedback_fix_endpoint_tester import FeedbackFixEndpointTester
from .feedback_error_endpoint_tester import FeedbackErrorEndpointTester
from .repair_endpoint_tester import RepairEndpointTester


class ApiTester(object):
    """
    This class is responsible for testing the ITS API using the base and modified programs

    """


    def __init__(self,
                 its_api_connection: ItsApiConnection,
                 input_generator: BaseInputGenerator,
                 error_localizer_endpoint_tester: ErrorLocalizerEndpointTester,
                 feedback_fix_endpoint_tester: FeedbackFixEndpointTester,
                 feedback_error_endpoint_tester: FeedbackErrorEndpointTester,
                 repair_endpoint_tester: RepairEndpointTester):
        """
        Initialisation method for an ItsApiConnection instance

        """
        self.its_api_connection = its_api_connection
        self.input_generator = input_generator
        self.error_localizer_endpoint_tester = error_localizer_endpoint_tester
        self.feedback_fix_endpoint_tester = feedback_fix_endpoint_tester
        self.feedback_error_endpoint_tester = feedback_error_endpoint_tester
        self.repair_endpoint_tester = repair_endpoint_tester


    def test_program(self, base_program_string: str, modified_program_string: str,
                     function_signature: dict,
                     language: str):
        """
        Tests the given program and determines if test case passed or not.
        Returns a test result object that we can further process.

        Parameters:
            base_program_string: Program string of base program
            modified_program_string: Program string of modified program
            function_signature: Function signature of base program, which should apply
                                to modified program
            type: Determines if we are testing programs to be semantically
                                          equivalent or not
            language: Language of program that we are testing
        """

        # STEP 1: Put base and modified programs into parser endpoint to get
        # intermediate representations
        base_program_intermediate, modified_program_intermediate = self._test_program_parser(
            base_program_string,
            modified_program_string,
            language
        )
        if isinstance(base_program_intermediate, TestResult):
            # Cannot parse
            return base_program_intermediate

        # Successfully parsed
        # STEP 2: Prepare function information for subsequent API endpoints
        function_name = function_signature["name"]
        function_arguments = function_signature["arguments"]
        # For now, take 1 set of inputs
        function_inputs = self.input_generator.generate_inputs(function_arguments, 1)[0]
        # Processes arguments to ITS API standard
        function_arguments_processed = process_arguments(function_inputs)

        # STEP 3: Call error localizer endpoint and check whether it pass
        test_result_error_localizer = self.error_localizer_endpoint_tester.test_endpoint(
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            base_program_intermediate=base_program_intermediate,
            modified_program_intermediate=modified_program_intermediate,
            language=language,
            function_name=function_name,
            function_arguments_processed=function_arguments_processed
        )

        if test_result_error_localizer is not None:
            # Got error or never pass error localizer test
            return test_result_error_localizer


        # STEP 4: Call feedback fix endpoint and check whether it pass
        test_result_feedback_fix = self.feedback_fix_endpoint_tester.test_endpoint(
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            base_program_intermediate=base_program_intermediate,
            modified_program_intermediate=modified_program_intermediate,
            language=language,
            function_name=function_name,
            function_arguments_processed=function_arguments_processed
        )
        if test_result_feedback_fix is not None:
            # Got error or never pass feedback fix test
            return test_result_feedback_fix


        # STEP 5: Call feedback error endpoint and check whether it pass
        test_result_feedback_error = self.feedback_error_endpoint_tester.test_endpoint(
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            base_program_intermediate=base_program_intermediate,
            modified_program_intermediate=modified_program_intermediate,
            language=language,
            function_name=function_name,
            function_arguments_processed=function_arguments_processed
        )
        if test_result_feedback_error is not None:
            # Got error or never pass feedback error test
            return test_result_feedback_error

        # STEP 6: Call repair endpoint and check whether it pass
        test_result_repair = self.repair_endpoint_tester.test_endpoint(
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            base_program_intermediate=base_program_intermediate,
            modified_program_intermediate=modified_program_intermediate,
            language=language,
            function_name=function_name,
            function_arguments_processed=function_arguments_processed
        )
        if test_result_repair is not None:
            # Got error or never pass repair test
            return test_result_feedback_error

        # STEP 7: Reach here means all successful. Return successful test result
        # STEP 7: Return success
        successful_test_result = TestResult(
            status=TypeOfTestResult.PASS,
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            inputs=function_arguments_processed)
        return successful_test_result


    def _test_program_parser(self, base_program_string, modified_program_string, language):
        """
            Helper function for parser

            Returns test result object if not successful, else return program intermediates
        """
        try:
            base_program_intermediate = self.its_api_connection.call_parser_endpoint(language, base_program_string)
            modified_program_intermediate = self.its_api_connection.call_parser_endpoint(language, modified_program_string)
            return base_program_intermediate, modified_program_intermediate
        except JSONDecodeError as e:
            # Exception occurred during parsing

            # Create exception instance
            exception_message = "Parser exception: " + str(e)
            test_result = TestResult(
                status=TypeOfTestResult.FAIL,
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                exception_message=exception_message)
            return test_result, test_result
