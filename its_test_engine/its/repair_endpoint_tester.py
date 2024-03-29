"""
    Tester for the repair endpoint
"""

import json
from json.decoder import JSONDecodeError
from .test_result import TestResult
from .api_output_comparator import ApiOutputComparator
from .endpoint_tester import EndpointTester
from .its_api_connection import ItsApiConnection
from ..enums.type_of_metamorphic_relation import TypeOfMetamorphicRelation
from ..enums.type_of_test_result import TypeOfTestResult



class RepairEndpointTester(EndpointTester):
    """
    This is a concrete class that is responsible for testing the repair endpoint

    """

    def __init__(self, api_output_comparator: ApiOutputComparator,
                 its_api_connection: ItsApiConnection,
                 type_of_metamorphic_relation: TypeOfMetamorphicRelation):
        """
        Initialisation method for a RepairEndpoint instance
        """
        self.api_output_comparator = api_output_comparator
        self.its_api_connection = its_api_connection
        self.type_of_metamorphic_relation = type_of_metamorphic_relation
        super().__init__(api_output_comparator, its_api_connection, type_of_metamorphic_relation)


    def test_endpoint(self, base_program_string, modified_program_string, base_program_intermediate,
                      modified_program_intermediate, language, function_name,
                      function_arguments_processed) -> TestResult:
        """
        Tests the endpoint and returns a test result encapsulating the outcome

        Returns:
           A TestResult instance containing the information regarding the outcome
           of testing the test case with the repair endpoint if an error
           was detected, else returns None if all pass
        """
        try:
            # Make API call
            output_repair = self.its_api_connection.call_repair_endpoint(
                language=language,
                reference_solution=json.dumps(base_program_intermediate, indent=4),
                student_solution=json.dumps(modified_program_intermediate, indent=4),
                function=function_name,
                inputs="[]",
                args=function_arguments_processed)

            # API call is successful. Check if test case pass or not
            did_repair_pass = self.check_status_of_result(output_repair)
            if not did_repair_pass:
                # Test case did not pass
                test_result = TestResult(
                    status=TypeOfTestResult.FAIL,
                    base_program_string=base_program_string,
                    modified_program_string=modified_program_string,
                    inputs=function_arguments_processed,
                    problematic_output=json.dumps(output_repair, indent=4)
                )
                return test_result
            else:
                # Test case pass
                return None

        except JSONDecodeError as e:
            # Exception occurred during parsing

            # Create exception instance
            exception_message = "Repair exception: " + str(e)
            test_result = TestResult(
                status=TypeOfTestResult.FAIL,
                base_program_string=base_program_string,
                modified_program_string=modified_program_string,
                inputs=function_arguments_processed,
                exception_message=exception_message)
            return test_result


    def check_status_of_result(self, api_result: dict):
        """
        Determines if the feedback error output is considered to be successful or not.
        It uses the API output comparator
        Returns true if pass, else return false

        """
        did_repair_pass = self.api_output_comparator.check_repair_output(
            repair_output= api_result,
            type_of_metamorphic_relation= self.type_of_metamorphic_relation
        )
        return did_repair_pass
