"""
    Tester for the error localizer endpoint
"""

import json
from json.decoder import JSONDecodeError
from .test_result import TestResult
from .api_output_comparator import ApiOutputComparator
from .endpoint_tester import EndpointTester
from .its_api_connection import ItsApiConnection
from ..enums.type_of_metamorphic_relation import TypeOfMetamorphicRelation
from ..enums.type_of_test_result import TypeOfTestResult



class ErrorLocalizerEndpointTester(EndpointTester):
    """
    This is a concrete class that is responsible for testing the error localizer endpoint

    """

    def __init__(self, api_output_comparator: ApiOutputComparator,
                 its_api_connection: ItsApiConnection,
                 type_of_metamorphic_relation: TypeOfMetamorphicRelation):
        """
        Initialisation method for a EndpointTester instance
        """
        self.api_output_comparator = api_output_comparator
        self.its_api_connection = its_api_connection
        self.type_of_metamorphic_relation = type_of_metamorphic_relation
        super().__init__(api_output_comparator, its_api_connection, type_of_metamorphic_relation)

# base_program_string, modified_program_string,
#                                      base_program_intermediate, modified_program_intermediate,
#                                      language, function_name, function_arguments_processed

    def test_endpoint(self, base_program_string, modified_program_string, base_program_intermediate,
                      modified_program_intermediate, language, function_name,
                      function_arguments_processed) -> TestResult:
        """
        Tests the endpoint and returns a test result encapsulating the outcome

        Returns:
           A TestResult instance containing the information regarding the outcome
           of testing the test case with the error localizer endpoint if an error
           was detected, else returns None if all pass
        """
        try:
            # Make API call
            output_error_localizer = self.its_api_connection.call_errorlocalizer_endpoint(
                language=language,
                reference_solution=json.dumps(base_program_intermediate, indent=4),
                student_solution=json.dumps(modified_program_intermediate, indent=4),
                function=function_name,
                inputs="[]",
                args=function_arguments_processed)

            # API call is successful. Check if test case pass or not
            did_error_localizer_pass = self.check_status_of_result(output_error_localizer)
            if not did_error_localizer_pass:
                # Test case did not pass
                test_result = TestResult(
                    status=TypeOfTestResult.FAIL,
                    base_program_string=base_program_string,
                    modified_program_string=modified_program_string,
                    inputs=function_arguments_processed,
                    problematic_output=json.dumps(output_error_localizer, indent=4)
                )
                return test_result
            else:
                # Test case pass
                return None

        except JSONDecodeError as e:
            # Exception occurred during parsing

            # Create exception instance
            exception_message = "Error localizer exception: " + str(e)
            test_result = TestResult(
                status=TypeOfTestResult.FAIL,
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                inputs=function_arguments_processed,
                exception_message=exception_message)
            return test_result


    def check_status_of_result(self, api_result: dict):
        """
        Abstract method to be overridden by concrete endpoint tester classes.
        This method determines if a result is considered success or failure depending on
        type of metamorphic relation being tested.

        Returns true if pass, else return false
        """
        did_error_localizer_pass = self.api_output_comparator.check_error_localizer_output(
            error_localizer_output= api_result,
            type_of_metamorphic_relation= self.type_of_metamorphic_relation
        )
        return did_error_localizer_pass
