from its_test_engine.enums import Language
from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.endpoint_tester import ErrorLocalizerEndpointTester


PROGRAM_TO_SUCCESS = "def add(a, b): return a + b"
PROGRAM_TO_FAIL = "def add(a, b): return b"


class MockItsApiConnection(ItsApiConnection):
    def call_errorlocalizer_endpoint(self, request_payload: dict):
        ref_solution = request_payload["reference_solution"]
        if ref_solution == PROGRAM_TO_FAIL:
            raise Exception("Invalid reference solution")
        return {"errorLocations": {}}
    

def test_error_localizer_endpoint_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    error_localizer_tester = ErrorLocalizerEndpointTester(its_api_connection)

    test_result = error_localizer_tester.run_test(
        "add", "", "", PROGRAM_TO_SUCCESS, PROGRAM_TO_SUCCESS, []
    )
    assert test_result.success

    test_result = error_localizer_tester.run_test(
        "add", "", "", PROGRAM_TO_FAIL, PROGRAM_TO_FAIL, []
    )
    assert not test_result.success
    