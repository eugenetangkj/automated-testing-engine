import json
from its_test_engine.enums import TypeOfMetamorphicRelation, Language
from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.endpoint_tester import FeedbackErrorEndpointTester

BASE_PROGRAM = "def add(a, b): a + b"
EQUIVALENT_PROGRAM = "def add1(a, b): return a - -b"
VARIANT_PROGRAM = "def add2(a, b): return a - b"
FAIL_PROGRAM = "def add3(a, b): return a"

class MockItsApiConnection(ItsApiConnection):
    def parse_program(self, program: str):
        parser_payload = ItsApiConnection.create_parser_request_payload(self, program)
        return ItsApiConnection.call_parser_endpoint(self, parser_payload)

    def call_feedback_error_endpoint(self, request_payload: dict):
        function_name = request_payload["function"]
        if function_name == "add1":
            return []

        if function_name == "add2":
            return [
                {
                    "lineNumber": 2,
                    "oldExpr": "a - b",
                    "newExpr": "a + b",
                    "repairStrings": [
                        "Wrong expression. Change a - b to a + b;"
                    ]
                }
            ]

        if function_name == "add3":
            raise Exception("Invalid program")

def test_feedback_error_equivalent_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)
    parsed_base_program = its_api_connection.parse_program(BASE_PROGRAM)
    parsed_equivalent_program = its_api_connection.parse_program(EQUIVALENT_PROGRAM)

    feedback_error_tester = FeedbackErrorEndpointTester(its_api_connection)
    feedback_error_tester.type_of_metamorphic_relation = TypeOfMetamorphicRelation.EQUIVALENT

    test_result = feedback_error_tester.run_test(
        {"name": "add1"}, BASE_PROGRAM, EQUIVALENT_PROGRAM, parsed_base_program, parsed_equivalent_program, [1, 2]
    )

    assert test_result.success

def test_feedback_error_exception_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)
    parsed_base_program = its_api_connection.parse_program(BASE_PROGRAM)
    parsed_fail_program = its_api_connection.parse_program(FAIL_PROGRAM)

    feedback_error_tester = FeedbackErrorEndpointTester(its_api_connection)
    feedback_error_tester.type_of_metamorphic_relation = TypeOfMetamorphicRelation.VARIANT

    test_result = feedback_error_tester.run_test(
        {"name": "add3"}, BASE_PROGRAM, FAIL_PROGRAM, parsed_base_program, parsed_fail_program, [1, 2]
    )

    assert not test_result.success
