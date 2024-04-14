"""
Analyses the output obtained from the errorlocalizer endpoint.
"""
from its_test_engine.enums import TypeOfMetamorphicRelation
from its_test_engine.its.test_result import ItsTestResult
from .endpoint_tester import EndpointTester


class ErrorLocalizerEndpointTester(EndpointTester):
    ENDPOINT = "error_localizer"

    def run_test(
        self,
        function_signature: dict,
        base_program_string: str,
        modified_program_string: str,
        parsed_base_program: str,
        parsed_modified_program: str,
        arguments: list[any],
    ) -> ItsTestResult:
        """
        Takes in input and pass it to the error localizer endpoint.
        Determines if the output is successful or not.

        Parameters:
            function_signature: Function signature for base program
            base_program_string: Program string for base program
            modified_program_string: Program string for modified program
            parsed_base_program: Parsed intermediate for base program
            parsed_modified_program: Parsed intermediate for modified program
            arguments: Arguments for the base and modified programs, to be
            entered into the error localizer endpoint.
        
        """
        function_name = function_signature["name"]
        request_payload = self.its_api_connection.create_request_payload(
            parsed_base_program,
            parsed_modified_program,
            function_name,
            "[]",
            arguments,
        )
        try:
            error_localizer_output = (
                self.its_api_connection.call_errorlocalizer_endpoint(request_payload)
            )

            passed = False

            if (
                self.type_of_metamorphic_relation
                == TypeOfMetamorphicRelation.EQUIVALENT
            ):
                passed = error_localizer_output["errorLocations"] == {}
            else:
                passed = error_localizer_output["errorLocations"] != {}

            return ItsTestResult(
                passed,
                self.ENDPOINT,
                "Success" if passed else "Error localizer endpoint failed",
                request_payload,
                error_localizer_output,
            )
        except Exception as e:
            message = e.__class__.__name__ + "\n" + str(e)
            return ItsTestResult(False, self.ENDPOINT, message, request_payload)
