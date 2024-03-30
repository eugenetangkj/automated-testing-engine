from its_test_engine.enums import TypeOfMetamorphicRelation
from its_test_engine.its.test_result import ItsTestResult
from .endpoint_tester import EndpointTester


class FeedbackErrorEndpointTester(EndpointTester):
    endpoint = "feedback_error"

    def run_test(
        self,
        function_signature: str,
        base_program_string: str,
        modified_program_string: str,
        parsed_base_program: str,
        parsed_modified_program: str,
        arguments: list[any],
    ) -> ItsTestResult:
        function_name = function_signature["name"]
        request_payload = self.its_api_connection.create_request_payload(
            parsed_base_program,
            parsed_modified_program,
            function_name,
            "[]",
            arguments,
        )
        try:
            feedback_error_output = (
                self.its_api_connection.call_feedback_error_endpoint(request_payload)
            )

            passed = False

            if (
                self.type_of_metamorphic_relation
                == TypeOfMetamorphicRelation.EQUIVALENT
            ):
                passed = len(feedback_error_output) == 0
            else:
                passed = len(feedback_error_output) != 0

            return ItsTestResult(
                passed,
                self.endpoint,
                "Success" if passed else "Feedback error endpoint failed",
                request_payload,
                feedback_error_output,
            )
        except Exception as e:
            message = e.__class__.__name__ + "\n" + str(e)
            return ItsTestResult(False, self.endpoint, message, request_payload)
