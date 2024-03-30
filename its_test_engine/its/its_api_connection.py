"""
    This class is responsible for connecting to the ITS API
"""

import json
import requests
from its_test_engine.enums import Language


class ItsApiConnection:
    """
    This class is responsible for making the API calls to the respective endpoints available
    on the ITS API. It is the main way through which the automated test engine interacts
    with the ITS API.

    Attributes:
        BASE_API_URL (str): The base URL to connect to the ITS API
    """

    BASE_API_URL = "https://its.comp.nus.edu.sg/cs3213/"

    def __init__(self, langauge: Language):
        """
        Initialisation method for an ItsApiConnection instance
        """
        self.language = langauge

    def __make_api_call(self, url, params):
        retry = 0
        response = None
        while retry < 3:
            try:
                response = requests.post(url, json=params, timeout=10)
                break
            except requests.exceptions.Timeout:
                print("Timeout error. Retrying...")
                retry += 1
                continue

        if response is None or response.status_code != 200:
            # Raise an exception if the status code is not 200
            # pylint: disable=broad-exception-raised
            raise Exception(
                f"Error in making API call to {url}. (Retry {retry} times)\n"
                + f"Status code: {response.status_code if response is not None else 'Timeout'}.\n"
                + f"Response: {response.text if response is not None else 'Timeout'}"
            )

        return response

    def __package_params(self, params, endpoint):
        """
        Takes in an array of parameters and packages these parameters according to the specified
        ITS API endpoint.
        The errorlocalizer, feedback_fix, feedback_error and repair services take in the same
        parameters.

        Parameters:
            params: List of parameters to be packed
            endpoint: The API endpoint to call to
        """
        if endpoint == "parser":
            return {"language": params[0], "source_code": params[1]}

        if endpoint == "interpreter":
            return {
                "language": params[0],
                "program_model": params[1],
                "function": params[2],
                "inputs": params[3],
                "args": params[4],
            }

        if endpoint == "alignment_structural":
            return {"reference_solution": params[0], "student_solution": params[1]}

        if endpoint == "alignment_variable":
            return {
                "reference_solution": params[0],
                "student_solution": params[1],
                "structural_alignment": params[2],
            }

        if endpoint in ["errorlocalizer", "feedback_fix", "feedback_error", "repair"]:
            return {
                "language": params[0],
                "reference_solution": params[1],
                "student_solution": params[2],
                "function": params[3],
                "inputs": params[4],
                "args": params[5],
            }

        return {}

    def create_parser_request_payload(self, source_code):
        """
        Returns the payload for the parser service endpoint of the ITS API
        """
        return {"language": self.language.value, "source_code": source_code}

    def call_parser_endpoint(self, payload):
        """
        Returns the response of the call to the parser service endpoint of the ITS API
        """
        parser_url = self.BASE_API_URL + "parser"
        response = self.__make_api_call(parser_url, payload)
        return response.json()

    def create_interpreter_request_payload(
        self, program_model: str, function: str, inputs: list, args: list
    ):
        """
        Returns the payload for the interpreter service endpoint of the ITS API
        """
        return {
            "language": self.language.value,
            "program_model": json.dumps(program_model),
            "function": function,
            "inputs": json.dumps(inputs),
            "args": json.dumps(args),
        }

    def call_interpreter_endpoint(self, payload):
        """
        Returns the response of the call to the interpreter service endpoint of the ITS API
        """
        interpreter_url = self.BASE_API_URL + "interpreter"
        response = self.__make_api_call(interpreter_url, payload)
        return response.json()

    def call_alignment_structural_endpoint(self, reference_solution, student_solution):
        """
        Returns the response of the call to the structural alignment service endpoint of the ITS API
        """
        alignment_structural_url = self.BASE_API_URL + "alignment_structural"
        param_arr = [reference_solution, student_solution]
        params = self.__package_params(param_arr, "alignment_structural")
        response = self.__make_api_call(alignment_structural_url, params)
        return response.json()

    def call_alignment_variable_endpoint(
        self, reference_solution, student_solution, structural_alignment
    ):
        """
        Returns the response of the call to the variable assignment service endpoint of the ITS API
        """
        alignment_variable_url = self.BASE_API_URL + "alignment_variable"
        param_arr = [reference_solution, student_solution, structural_alignment]
        params = self.__package_params(param_arr, "alignment_variable")
        response = self.__make_api_call(alignment_variable_url, params)
        return response.json()

    def create_request_payload(
        self, reference_solution, student_solution, function, inputs, args
    ):
        return {
            "language": self.language.value,
            "reference_solution": json.dumps(reference_solution),
            "student_solution": json.dumps(student_solution),
            "function": function,
            "inputs": inputs,
            "args": json.dumps(args),
        }

    def call_errorlocalizer_endpoint(self, request_payload):
        """
        Returns the response of the call to the error localizer service endpoint of the ITS API
        """
        errorlocalizer_url = self.BASE_API_URL + "errorlocalizer"
        response = self.__make_api_call(errorlocalizer_url, request_payload)
        return response.json()

    def call_feedback_fix_endpoint(self, request_payload):
        """
        Returns the response of the call to the feedback fix endpoint of the
        feedback service in the ITS API
        """
        feedback_fix_url = self.BASE_API_URL + "feedback_fix"
        response = self.__make_api_call(feedback_fix_url, request_payload)

        return response.json()

    def call_feedback_error_endpoint(self, request_payload):
        """
        Returns the response of the call to the feedback error endpoint of the feedback service
        in the ITS API
        """
        feedback_error_url = self.BASE_API_URL + "feedback_error"
        response = self.__make_api_call(feedback_error_url, request_payload)
        return response.json()

    def call_repair_endpoint(self, request_payload):
        """
        Returns the response of the call to the repair service endpoint of the ITS API
        """
        repair_url = self.BASE_API_URL + "repair"
        response = self.__make_api_call(repair_url, request_payload)

        return response.json()
