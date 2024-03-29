'''
    This class is responsible for using base and modified programs to test the ITS API
'''

from json.decoder import JSONDecodeError
import json
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
                 api_output_comparator: ApiOutputComparator, ):
        """
        Initialisation method for an ItsApiConnection instance

        Parameters:
            its_api_connection: Provides access to ITS API
        """
        self.its_api_connection = its_api_connection
        self.input_generator = input_generator
        self.api_output_comparator = api_output_comparator


    def test_program(self, base_program_string: str, modified_program_string: str,
                     function_signature: dict,
                     type_of_metamorphic_relation: TypeOfMetamorphicRelation,
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
        if base_program_intermediate is None:
            return


        # STEP 2: Prepare function information for subsequent API endpoints
        function_name = function_signature["name"]
        function_arguments = function_signature["arguments"]
        # For now, take 1 set of inputs
        function_inputs = self.input_generator.generate_inputs(function_arguments, 1)[0]
        # Processes arguments to ITS API standard
        function_arguments_processed = process_arguments(function_inputs)

        print(function_name)
        print(function_arguments)
        print(function_arguments_processed)



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


        # STEP 5: Call feedback error endpoint and check whether it pass
        output_feedback_error = self._test_program_feedbackerror(
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            base_program_intermediate=base_program_intermediate,
            modified_program_intermediate=modified_program_intermediate,
            language=language,
            function_name=function_name,
            function_arguments_processed=function_arguments_processed
        )

        if output_feedback_error is None:
            return

        did_feedback_error_pass = self.api_output_comparator.check_feedback_error_output(
            feedback_error_output= output_feedback_error,
            type_of_metamorphic_relation= type_of_metamorphic_relation
        )
        if not did_feedback_error_pass:
            # Process error and return
            self._output_feedbackerror_error(
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                inputs=function_arguments_processed,
                feedback_error_output=output_feedback_error
            )
            return

        # STEP 6: Call repair endpoint and check whether it pass
        output_repair = self._test_program_repair(
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            base_program_intermediate=base_program_intermediate,
            modified_program_intermediate=modified_program_intermediate,
            language=language,
            function_name=function_name,
            function_arguments_processed=function_arguments_processed
        )

        if output_repair is None:
            return

        did_repair_pass = self.api_output_comparator.check_repair_output(
            repair_output= output_repair,
            type_of_metamorphic_relation= type_of_metamorphic_relation
        )
        if not did_repair_pass:
            # Process error and return
            self._output_repair_error(
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                inputs=function_arguments_processed,
               repair_output=output_repair
            )
            return

        # STEP 7: Return success
        test_result = TestResult(
            status=TypeOfTestResult.PASS,
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            inputs=function_arguments_processed)

        ResultWriter().write_results_to_file(test_result)
        print("Test case completed")


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
                reference_solution=json.dumps(base_program_intermediate, indent=4),
                student_solution=json.dumps(modified_program_intermediate, indent=4),
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
            return None

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
            problematic_output=json.dumps(error_localizer_output, indent=4)
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
            output_feedbackfix = self.its_api_connection.call_feedback_fix_endpoint(
                language=language,
                reference_solution=json.dumps(base_program_intermediate, indent=4),
                student_solution=json.dumps(modified_program_intermediate, indent=4),
                function=function_name,
                inputs="[]",
                args=function_arguments_processed)
            return output_feedbackfix


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
            return None

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
            problematic_output=json.dumps(feedback_fix_output, indent=4)
        )

        ResultWriter().write_results_to_file(test_result)
        print("Test case completed")
        return

    def _test_program_feedbackerror(self, base_program_string, modified_program_string,
                                    base_program_intermediate, modified_program_intermediate,
                                    language, function_name, function_arguments_processed):
        """
            Helper function for feedback error
        """
        try:
            output_feedback_error = self.its_api_connection.call_feedback_error_endpoint(
                language=language,
                reference_solution=json.dumps(base_program_intermediate, indent=4),
                student_solution=json.dumps(modified_program_intermediate, indent=4),
                function=function_name,
                inputs="[]",
                args=function_arguments_processed)
            return output_feedback_error


        except JSONDecodeError as e:
            # Exception occurred during parsing

            # Create exception instance
            exception_message = "Feedback error exception: " + str(e)
            test_result = TestResult(
                status=TypeOfTestResult.FAIL,
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                exception_message=exception_message)

            ResultWriter().write_results_to_file(test_result)
            print("Test case completed")
            return None

    def _output_feedbackerror_error(self, base_program_string, modified_program_string,
                                    inputs, feedback_error_output):
        """
            Helper to output feedback error error, indicating potential bug
        """
        test_result = TestResult(
            status=TypeOfTestResult.FAIL,
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            inputs=inputs,
            problematic_output=json.dumps(feedback_error_output, indent=4)
        )

        ResultWriter().write_results_to_file(test_result)
        print("Test case completed")
        return

    def _test_program_repair(self, base_program_string, modified_program_string,
                                     base_program_intermediate, modified_program_intermediate,
                                     language, function_name, function_arguments_processed):
        """
            Helper function for repair
        """
        try:
            output_repair = self.its_api_connection.call_repair_endpoint(
                language=language,
                reference_solution=json.dumps(base_program_intermediate, indent=4),
                student_solution=json.dumps(modified_program_intermediate, indent=4),
                function=function_name,
                inputs="[]",
                args=function_arguments_processed)
            return output_repair

        except JSONDecodeError as e:
            # Exception occurred during parsing

            # Create exception instance
            exception_message = "Repair exception: " + str(e)
            test_result = TestResult(
                status=TypeOfTestResult.FAIL,
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                exception_message=exception_message)

            ResultWriter().write_results_to_file(test_result)
            print("Test case completed")
            return None

    def _output_repair_error(self, base_program_string, modified_program_string,
                                    inputs, repair_output):
        """
            Helper to output repair error, indicating potential bug
        """
        test_result = TestResult(
            status=TypeOfTestResult.FAIL,
            base_program_string=base_program_string,
            modified_program_string=modified_program_string,
            inputs=inputs,
            problematic_output=json.dumps(repair_output, indent=4)
        )

        ResultWriter().write_results_to_file(test_result)
        print("Test case completed")
        return
