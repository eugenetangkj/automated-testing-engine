from its_test_engine.enums import Language
from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.endpoint_tester import InterpreterTester


PROGRAM_TO_SUCCESS = "def add(a, b): return a + b"
PROGRAM_TO_FAIL = "def add2(a, b): return a"
PROGRAM_TO_FAIL2 = "def add3(a, b): return b"


class MockItsApiConnection(ItsApiConnection):
    def call_interpreter_endpoint(self, payload: dict):
        function = payload["function"]
        if function == "add2":
            raise Exception("Invalid program")
        if function == "add3":
            return None
        return {"entries": [{"functionName": function}]}


def test_parser_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    interpreter_tester = InterpreterTester(its_api_connection)

    interpreter_output, test_result = interpreter_tester.run_test(
        {"name": "add"}, PROGRAM_TO_SUCCESS, [1, 2]
    )
    assert interpreter_output == {"entries": [{"functionName": "add"}]}
    assert test_result.success

    interpreter_output, test_result = interpreter_tester.run_test(
        {"name": "add2"}, PROGRAM_TO_FAIL, [1, 2]
    )
    assert interpreter_output is None
    assert not test_result.success

    interpreter_output, test_result = interpreter_tester.run_test(
        {"name": "add3"}, PROGRAM_TO_FAIL2, [1, 2]
    )

    assert interpreter_output is None
    assert not test_result.success
