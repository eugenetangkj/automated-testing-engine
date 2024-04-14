"""
Analyses the output obtained from the parser endpoint.
"""
from its_test_engine.its.test_result import ItsTestResult
from its_test_engine.its.its_api_connection import ItsApiConnection


class ParserTester:
    def __init__(
        self,
        its_api_connection: ItsApiConnection,
    ):
        """
            Initialises a ParserTester instance.

            Parameters:
                its_api_connection: To make connection with ITS API
        """
        self.its_api_connection = its_api_connection

    def run_test(self, program: str):
        """
        Takes in input and pass it to the parser endpoint
        Determines if the output is successful or not.

        Parameters:
            program: Program string to be parsed

        """
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
