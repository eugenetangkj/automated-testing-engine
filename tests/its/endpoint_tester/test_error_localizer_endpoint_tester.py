import json
from its_test_engine.enums import Language
from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.endpoint_tester import ErrorLocalizerEndpointTester

BASE_PROGRAM = "def add(a, b): return a + b"
PROGRAM_TO_GIVE_SUCCESSFUL = "def add1(a, b): return a + b"
PROGRAM_TO_GIVE_UNSUCCESSFUL = "def add2(a, b): return b"


class MockItsApiConnection(ItsApiConnection):
    def get_parsed_output_for_test(self, source_code):
        payload = self.create_parser_request_payload(source_code)
        return json.dumps(self.call_parser_endpoint(payload))

    def call_errorlocalizer_endpoint(self, request_payload: dict):
        student_solution = request_payload["student_solution"]
        expected = json.dumps(self.get_parsed_output_for_test(PROGRAM_TO_GIVE_UNSUCCESSFUL))
        if student_solution == expected:
            raise Exception("Give unsuccessful test result")
        return {"errorLocations": {}}
    

def test_error_localizer_endpoint_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    error_localizer_tester = ErrorLocalizerEndpointTester(its_api_connection)

    parsed_base = its_api_connection.get_parsed_output_for_test(BASE_PROGRAM)
    parsed_successful = its_api_connection.get_parsed_output_for_test(PROGRAM_TO_GIVE_SUCCESSFUL)
    parsed_unsuccessful = its_api_connection.get_parsed_output_for_test(PROGRAM_TO_GIVE_UNSUCCESSFUL)

    test_result = error_localizer_tester.run_test(
        {"name":"add", "argument_types": ["int"], "return_type": "int"}, 
        BASE_PROGRAM, 
        PROGRAM_TO_GIVE_SUCCESSFUL, 
        parsed_base, 
        parsed_successful, 
        []
    )
    assert test_result.success

    test_result = error_localizer_tester.run_test(
        {"name":"add1", "argument_types": ["int"], "return_type": "int"},
        BASE_PROGRAM, 
        PROGRAM_TO_GIVE_UNSUCCESSFUL, 
        parsed_base,
        parsed_unsuccessful,
        []
    )
    assert not test_result.success
    