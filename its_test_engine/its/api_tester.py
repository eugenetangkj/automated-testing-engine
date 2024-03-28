'''
    This class is responsible for using base and modified programs to test the ITS API
'''

from json.decoder import JSONDecodeError
from ..enums.type_of_metamorphic_relation import TypeOfMetamorphicRelation
from ..enums.type_of_test_result import TypeOfTestResult
from .its_api_connection import ItsApiConnection
from .test_result import TestResult
from .result_writer import ResultWriter
from ..base.input_generator import BaseInputGenerator
from .api_output_comparator import ApiOutputComparator
from ..utils import process_arguments


class ApiTester(object):
    """
    This class is responsible for testing the ITS API using the base and modified programs

    """


    def __init__(self, its_api_connection: ItsApiConnection, input_generator: BaseInputGenerator,
                 api_output_comparator: ApiOutputComparator):
        """
        Initialisation method for an ItsApiConnection instance

        Parameters:
            its_api_connection: Provides access to ITS API
        """
        self.its_api_connection = its_api_connection
        self.input_generator = input_generator
        self.api_output_comparator = api_output_comparator


    def test_program(self, base_program_string: str, modified_program_string: str, function_signature: dict,
                    type_of_metamorphic_relation: TypeOfMetamorphicRelation, language: str):
        """
        Tests the given program and determines if test case passed or not

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
        if base_program_intermediate is None:
            return


        # STEP 2: Prepare function information for subsequent API endpoints
        function_name = function_signature["name"]
        function_arguments = function_signature["arguments"]
        function_inputs = self.input_generator.generate_inputs(function_arguments,
                                                               len(function_arguments))
        # Processes arguments to ITS API standard
        function_arguments_processed = process_arguments(function_inputs)

        # STEP 3: Call error localizer endpoint and check whether it pass
        output_error_localizer = self._test_program_errorlocalizer(
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            base_program_intermediate=base_program_intermediate,
            modified_program_intermediate=modified_program_intermediate,
            language=language,
            function_name=function_name,
            function_arguments_processed=function_arguments_processed
        )

        if output_error_localizer is None:
            return

        did_error_localizer_pass = self.api_output_comparator.check_error_localizer_output(
            error_localizer_output= output_error_localizer,
            type_of_metamorphic_relation= type_of_metamorphic_relation
        )
        if not did_error_localizer_pass:
            # Process error and return
            self._output_errorlocalizer_error(
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                inputs=function_arguments_processed,
                error_localizer_output=output_error_localizer
            )
            return


        # STEP 4: Call feedback fix endpoint and check whether it pass
        output_feedback_fix = self._test_program_feedbackfix(
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            base_program_intermediate=base_program_intermediate,
            modified_program_intermediate=modified_program_intermediate,
            language=language,
            function_name=function_name,
            function_arguments_processed=function_arguments_processed
        )

        if output_feedback_fix is None:
            return

        did_feedback_fix_pass = self.api_output_comparator.check_feedback_fix_output(
            feedback_fix_output= output_feedback_fix,
            type_of_metamorphic_relation= type_of_metamorphic_relation
        )
        if not did_feedback_fix_pass:
            # Process error and return
            self._output_feedbackfix_error(
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                inputs=function_arguments_processed,
                feedback_fix_output=output_feedback_fix
            )
            return
    












    def _test_program_parser(self, base_program_string, modified_program_string, language):
        """
            Helper function for parser
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

            ResultWriter().write_results_to_file(test_result)
            print("Test case completed")
            return None, None

    def _test_program_errorlocalizer(self, base_program_string, modified_program_string,
                                     base_program_intermediate, modified_program_intermediate,
                                     language, function_name, function_arguments_processed):
        """
            Helper function for error localizer
        """
        try:
            output_error_localizer = self.its_api_connection.call_errorlocalizer_endpoint(
                language=language,
                reference_solution=base_program_intermediate,
                student_solution=modified_program_intermediate,
                function=function_name,
                inputs="[]",
                args=function_arguments_processed)
            return output_error_localizer


        except JSONDecodeError as e:
            # Exception occurred during parsing

            # Create exception instance
            exception_message = "Error localizer exception: " + str(e)
            test_result = TestResult(
                status=TypeOfTestResult.FAIL,
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                exception_message=exception_message)

            ResultWriter().write_results_to_file(test_result)
            print("Test case completed")
            return None, None

    def _output_errorlocalizer_error(self, base_program_string, modified_program_string,
                                      inputs, error_localizer_output):
        """
            Helper to output error localizer error, indicating potential bug
        """
        test_result = TestResult(
            status=TypeOfTestResult.FAIL,
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            inputs=inputs,
            problematic_output=error_localizer_output
        )

        ResultWriter().write_results_to_file(test_result)
        print("Test case completed")
        return

    def _test_program_feedbackfix(self, base_program_string, modified_program_string,
                                    base_program_intermediate, modified_program_intermediate,
                                    language, function_name, function_arguments_processed):
        """
            Helper function for feedback fix
        """
        try:
            output_error_localizer = self.its_api_connection.call_feedback_fix_endpoint(
                language=language,
                reference_solution=base_program_intermediate,
                student_solution=modified_program_intermediate,
                function=function_name,
                inputs="[]",
                args=function_arguments_processed)
            return output_error_localizer


        except JSONDecodeError as e:
            # Exception occurred during parsing

            # Create exception instance
            exception_message = "Feedback fix exception: " + str(e)
            test_result = TestResult(
                status=TypeOfTestResult.FAIL,
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                exception_message=exception_message)

            ResultWriter().write_results_to_file(test_result)
            print("Test case completed")
            return None, None

    def _output_feedbackfix_error(self, base_program_string, modified_program_string,
                                    inputs, feedback_fix_output):
        """
            Helper to output feedback fix error, indicating potential bug
        """
        test_result = TestResult(
            status=TypeOfTestResult.FAIL,
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            inputs=inputs,
            problematic_output=feedback_fix_output
        )

        ResultWriter().write_results_to_file(test_result)
        print("Test case completed")
        return
