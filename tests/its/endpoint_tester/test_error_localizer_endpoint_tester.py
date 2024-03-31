import json
from its_test_engine.enums import Language
from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.endpoint_tester import ErrorLocalizerEndpointTester

BASE_PROGRAM = "def add(a, b): return a + b"
PARSED_BASE_PROGRAM = "{\"importStatements\": [], \"fncs\": {\"add\": {\"name\": \"add\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'add'\"}, \"types\": {}}}}"

PROGRAM_TO_GIVE_SUCCESSFUL = "def add1(a, b): return a + b"
PARSED_PROGRAM_TO_GIVE_SUCCESSFUL = "{\"importStatements\": [], \"fncs\": {\"add1\": {\"name\": \"add1\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'add'\"}, \"types\": {}}}}"

PROGRAM_TO_GIVE_UNSUCCESSFUL = "def add2(a, b): return b"
PARSED_PROGRAM_TO_GIVE_UNSUCCESSFUL = "{\"importStatements\": [], \"fncs\": {\"add2\": {\"name\": \"add2\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'add2'\"}, \"types\": {}}}}"



class MockItsApiConnection(ItsApiConnection):
    def call_errorlocalizer_endpoint(self, request_payload: dict):
        student_solution = request_payload["student_solution"]
        expected = json.dumps(PARSED_PROGRAM_TO_GIVE_UNSUCCESSFUL)
        if student_solution == expected:
            raise Exception("Give unsuccessful test result")
        return {"errorLocations": {}}
    

def test_error_localizer_endpoint_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    error_localizer_tester = ErrorLocalizerEndpointTester(its_api_connection)

    test_result = error_localizer_tester.run_test(
        {"name":"add", "argument_types": ["int"], "return_type": "int"}, 
        BASE_PROGRAM, 
        PROGRAM_TO_GIVE_SUCCESSFUL, 
        PARSED_BASE_PROGRAM, 
        PARSED_PROGRAM_TO_GIVE_SUCCESSFUL, 
        []
    )
    assert test_result.success

    test_result = error_localizer_tester.run_test(
        {"name":"add1", "argument_types": ["int"], "return_type": "int"},
        BASE_PROGRAM, 
        PROGRAM_TO_GIVE_UNSUCCESSFUL, 
        PARSED_BASE_PROGRAM,
        PARSED_PROGRAM_TO_GIVE_UNSUCCESSFUL,
        []
    )
    assert not test_result.success
    