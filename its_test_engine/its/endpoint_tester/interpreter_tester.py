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
        request_payload = self.its_api_connection.create_interpreter_request_payload(
            parsed_program, function_signature["name"], [], inputs
        )
        try:
            result = self.its_api_connection.call_interpreter_endpoint(request_payload)

            if result is None or "entries" not in result:
                return None, ItsTestResult(
                    False,
                    "interpreter",
                    "No entries in result",
                    request_payload,
                    result,
                )

            return result, ItsTestResult(
                True, "interpreter", "Success", request_payload, result
            )
        except Exception as e:
            return None, ItsTestResult(False, "interpreter", str(e), request_payload)
