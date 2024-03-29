import json
from its_test_engine.its.test_result import ItsTestResult
from its_test_engine.its.its_api_connection import ItsApiConnection


class ParserTester:
    def __init__(
        self,
        its_api_connection: ItsApiConnection,
    ):
        self.its_api_connection = its_api_connection

    def run_test(self, program: str):
        try:
            parsed_program = self.its_api_connection.call_parser_endpoint(program)
            return parsed_program, ItsTestResult(
                True, "parser", "Success", json.dumps(parsed_program, indent=4)
            )
        except Exception as e:
            return None, ItsTestResult(False, "parser", str(e), None)
