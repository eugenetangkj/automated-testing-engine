from its_test_engine.enums import Language
from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.endpoint_tester import ParserTester


PROGRAM_TO_SUCCESS = "def add(a, b): return a + b"
PROGRAM_TO_FAIL = "def add(a, b): return a"


class MockItsApiConnection(ItsApiConnection):
    def call_parser_endpoint(self, payload: dict):
        program = payload["source_code"]
        if program == PROGRAM_TO_FAIL:
            raise Exception("Invalid program")
        return {"importStatements": [], "fncs": {}}


def test_parser_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    parser_tester = ParserTester(its_api_connection)

    parsed_program, test_result = parser_tester.run_test(PROGRAM_TO_SUCCESS)
    assert parsed_program == {"importStatements": [], "fncs": {}}
    assert test_result.success

    parsed_program, test_result = parser_tester.run_test(PROGRAM_TO_FAIL)
    assert parsed_program is None
    assert not test_result.success
