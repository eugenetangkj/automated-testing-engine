"""
Analyses the output obtained from the interpreter endpoint
"""
from its_test_engine.its.test_result import ItsTestResult
from its_test_engine.its.its_api_connection import ItsApiConnection


class InterpreterTester:
    def __init__(
        self,
        its_api_connection: ItsApiConnection,
    ):
        """
            Initialises an InterpreterTester instance.

            Parameters:
                its_api_connection: To make connection with ITS API
        """
        self.its_api_connection = its_api_connection

    def run_test(
        self, function_signature: dict, parsed_program: str, arguments: list[any]
    ):
        """
        Takes in input and pass it to the interpreter endpoint.
        Determines if the output is successful or not.

        Parameters:
            function_signature: Function signature of the function input
            parsed_program: Parsed intermediate of the function input
            arguments: Arguments to be passed into the interpreter endpoint

        """
        request_payload = self.its_api_connection.create_interpreter_request_payload(
            parsed_program, function_signature["name"], [], arguments
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
