import json
from its_test_engine.enums import TypeOfMetamorphicRelation, Language
from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.endpoint_tester import RepairEndpointTester

BASE_PROGRAM = "def add(a, b): return a + b"
PARSED_BASE_PROGRAM = '{"importStatements": [], "fncs": {"add": {"name": "add", "rettype": "*", "initloc": 1, "endloc": 0, "params": [{"val0": "a", "val1": "*", "valueArray": ["a", "*"], "valueList": ["a", "*"]}, {"val0": "b", "val1": "*", "valueArray": ["b", "*"], "valueList": ["b", "*"]}], "locexprs": {"1": []}, "loctrans": {"1": {}}, "locdescs": {"1": "around the beginning of function \'add\'"}, "types": {}}}}'

SUCCESS_PROGRAM = "def add1(a, b): return a - -b"
PARSED_SUCCESS_PROGRAM = "{\"importStatements\": [], \"fncs\": {\"add1\": {\"name\": \"add1\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'add1'\"}, \"types\": {}}}}"

FAIL_PROGRAM = "def add2(a, b): return b"
PARSED_FAIL_PROGRAM = "{\"importStatements\": [], \"fncs\": {\"add3\": {\"name\": \"add3\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'add3'\"}, \"types\": {}}}}"


class MockItsApiConnection(ItsApiConnection):
    def call_repair_endpoint(self, request_payload: dict):
        function_name = request_payload["function"]
        unsuccessful = json.dumps(PARSED_FAIL_PROGRAM)
        if function_name == unsuccessful:
            raise Exception("Unsuccessful test result")
        return {"totalCost": 0.0, "localRepairs": {}}

def test_repair_equivalent_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    repair_tester = RepairEndpointTester(its_api_connection, TypeOfMetamorphicRelation.EQUIVALENT)

    test_result = repair_tester.run_test(
        {"name":"add1", "argument_types": ["int"], "return_type": "int"},
        BASE_PROGRAM,
        SUCCESS_PROGRAM,
        PARSED_BASE_PROGRAM,
        PARSED_SUCCESS_PROGRAM,
        [],
    )
    assert test_result.success

def test_repair_variant_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    repair_tester = RepairEndpointTester(its_api_connection, TypeOfMetamorphicRelation.VARIANT)

    test_result = repair_tester.run_test(
        {"name":"add2", "argument_types": ["int"], "return_type": "int"},
        BASE_PROGRAM,
        FAIL_PROGRAM,
        PARSED_BASE_PROGRAM,
        PARSED_FAIL_PROGRAM,
        [],
    )

    assert not test_result.success
