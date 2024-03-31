
import json
from its_test_engine.enums import TypeOfMetamorphicRelation, Language
from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.endpoint_tester import FeedbackFixEndpointTester


BASE_PROGRAM = "def add(a, b): a + b"
PARSED_BASE_PROGRAM = "{\"importStatements\": [], \"fncs\": {\"add\": {\"name\": \"add\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'add'\"}, \"types\": {}}}}"

EQUIVALENT_PROGRAM = "def add1(a, b): return a - -b"
PARSED_EQUIVALENT_PROGRAM = "{\"importStatements\": [], \"fncs\": {\"add1\": {\"name\": \"add1\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'add1'\"}, \"types\": {}}}}"

VARIANT_PROGRAM = "def add2(a, b): return a - b"
PARSED_VARIANT_PROGRAM = "{\"importStatements\": [], \"fncs\": {\"add2\": {\"name\": \"add2\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'add2'\"}, \"types\": {}}}}"

FAIL_PROGRAM = "def add3(a, b): return b"
PARSED_FAIL_PROGRAM = "{\"importStatements\": [], \"fncs\": {\"add3\": {\"name\": \"add3\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'add3'\"}, \"types\": {}}}}"

class MockItsApiConnection(ItsApiConnection):
    def call_feedback_fix_endpoint(self, request_payload: dict):
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

def test_feedback_fix_equivalent_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    feedback_fix_tester = FeedbackFixEndpointTester(its_api_connection, TypeOfMetamorphicRelation.EQUIVALENT)

    test_result = feedback_fix_tester.run_test(
        {"name":"add1", "argument_types": ["int"], "return_type": "int"},
        BASE_PROGRAM,
        EQUIVALENT_PROGRAM,
        PARSED_BASE_PROGRAM,
        PARSED_EQUIVALENT_PROGRAM,
        []
    )
    assert test_result.success

def test_feedback_fix_variant_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    feedback_fix_tester = FeedbackFixEndpointTester(its_api_connection, TypeOfMetamorphicRelation.VARIANT)

    test_result = feedback_fix_tester.run_test(
        {"name":"add2", "argument_types": ["int"], "return_type": "int"},
        BASE_PROGRAM,
        VARIANT_PROGRAM,
        PARSED_BASE_PROGRAM,
        PARSED_VARIANT_PROGRAM,
        []
    )
    assert test_result.success

def test_feedback_fix_exception_tester():
    its_api_connection = MockItsApiConnection(Language.PYTHON)

    feedback_fix_tester = FeedbackFixEndpointTester(its_api_connection)

    test_result = feedback_fix_tester.run_test(
        {"name":"add3", "argument_types": ["int"], "return_type": "int"},
        BASE_PROGRAM,
        FAIL_PROGRAM,
        PARSED_BASE_PROGRAM,
        PARSED_FAIL_PROGRAM,
        []
    )
    assert not test_result.success
