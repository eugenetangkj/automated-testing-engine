from its_test_engine.enums import TypeOfMetamorphicRelation
from its_test_engine.its.test_result import ItsTestResult
from its_test_engine.its.endpoint_tester import FeedbackErrorEndpointTester


class MockItsApiConnection:
    def create_request_payload(self, *args, **kwargs):
        return {
            "parsed_base_program": "parsed_base_program",
            "parsed_modified_program": "parsed_modified_program",
            "function_name": "function_name",
            "metamorphic_relation": "[]",
            "arguments": [1, 2]
        }

    def call_feedback_error_endpoint(self, payload: dict):
        if payload["parsed_base_program"] == "valid" and payload["parsed_modified_program"] == "valid":
            return []
        else:
            raise Exception("Invalid program")


def test_feedback_error_endpoint_tester():
    # Create an instance of MockItsApiConnection
    its_api_connection = MockItsApiConnection()

    # Create an instance of FeedbackErrorEndpointTester with the mock connection
    endpoint_tester = FeedbackErrorEndpointTester(its_api_connection)

    # Define test parameters
    function_signature = {"name": "add"}
    base_program_string = "valid"
    modified_program_string = "valid"
    parsed_base_program = "parsed_base_program"
    parsed_modified_program = "parsed_modified_program"
    arguments = [1, 2]

    # Run the test
    test_result = endpoint_tester.run_test(
        function_signature,
        base_program_string,
        modified_program_string,
        parsed_base_program,
        parsed_modified_program,
        arguments,
    )

    # Assert the test result
    assert test_result.success

    # Repeat the test with invalid program strings
    base_program_string = "invalid"
    modified_program_string = "invalid"

    test_result = endpoint_tester.run_test(
        function_signature,
        base_program_string,
        modified_program_string,
        parsed_base_program,
        parsed_modified_program,
        arguments,
    )

    # Assert the test result
    assert not test_result.success
