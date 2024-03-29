import json
from its_test_engine.its.test_result import ItsTestResult
from its_test_engine.its.its_api_connection import ItsApiConnection


class InterpreterTester:
    def __init__(
        self,
        its_api_connection: ItsApiConnection,
    ):
        self.its_api_connection = its_api_connection

    def run_test(
        self, function_signature: dict, parsed_program: str, inputs: list[any]
    ):
        try:
            result = self.its_api_connection.call_interpreter_endpoint(
                parsed_program,
                function=function_signature["name"],
                inputs="[]",
                args=inputs,
            )
            return result, ItsTestResult(
                True, "interpreter", "Success", json.dumps(result, indent=4)
            )
        except Exception as e:
            return None, ItsTestResult(False, "interpreter", str(e), None)
