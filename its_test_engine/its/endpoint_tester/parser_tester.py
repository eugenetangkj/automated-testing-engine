from its_test_engine.its.test_result import ItsTestResult
from its_test_engine.its.its_api_connection import ItsApiConnection


class ParserTester:
    def __init__(
        self,
        its_api_connection: ItsApiConnection,
    ):
        self.its_api_connection = its_api_connection

    def run_test(self, program: str):
        request_payload = self.its_api_connection.create_parser_request_payload(program)
        try:
            parsed_program = self.its_api_connection.call_parser_endpoint(
                request_payload
            )
            return parsed_program, ItsTestResult(
                True,
                "parser",
                "Success",
                request_payload,
                parsed_program,
            )
        except Exception as e:
            return None, ItsTestResult(False, "parser", str(e), request_payload)
