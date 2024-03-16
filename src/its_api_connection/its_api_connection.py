import requests

class ItsApiConnection(object):
    """
    This class is responsible for making the API calls to the respective endpoints available
    on the ITS API. It is the main way through which the automated test engine interacts
    with the ITS API.

    Attributes:
        BASE_API_URL (str): The base URL to connect to the ITS API
    """

    BASE_API_URL = "https://its.comp.nus.edu.sg/cs3213/"

    def __init__(self):
        """
        Initialisation method for an ItsApiConnection instance
        """
        pass

    def __make_api_call(self, url, params):
        return requests.post(url, json=params)

    def __package_params(self, params, endpoint):
        """
        Takes in an array of parameters and packages these parameters according to the specified
        ITS API endpoint.
        The errorlocalizer, feedback_fix, feedback_error and repair services take in the same
        parameters.
        """
        if endpoint == "parser":
            return {"language": params[0], "source_code": params[1]}

        if endpoint == "interpreter":
            return {"language": params[0], "program_model": params[1],
                    "function": params[2], "inputs": params[3], "args": params[4]}

        if endpoint == "structural_alignment":
            return {"reference_solution": params[0], "student_solution": params[1]}

        if endpoint in ["errorlocalizer", "feedback_fix", "feedback_error", "repair"]:
            return {"language": params[0], "reference_solution": params[1],
                    "student_solution": params[2], "function": params[3], "inputs": params[4],
                    "args": params[5]}

    def call_parser_endpoint(self, language, source_code):
        """
        Returns the response of the call to the parser service endpoint of the ITS API
        """
        parser_url = self.BASE_API_URL + "parser"
        param_arr = [language, source_code]
        params = self.__package_params(param_arr, "parser")
        response = self.__make_api_call(parser_url, params)
        return response.json()

    def call_interpreter_endpoint(self, language, program_model, function, inputs, args):
        """
        Returns the response of the call to the interpreter service endpoint of the ITS API
        """
        interpreter_url = self.BASE_API_URL + "interpreter"
        param_arr = [language, program_model, function, inputs, args]
        params = self.__package_params(param_arr, "interpreter")
        response = self.__make_api_call(interpreter_url, params)
        return response.json()

    def call_alignment_structural_endpoint(self, reference_solution, student_solution):
        """
        Returns the response of the call to the structural alignment service endpoint of the ITS API
        """
        alighnment_structural_url = self.BASE_API_URL + "alignment_structural"
        param_arr = [reference_solution, student_solution]
        params = self.__package_params(param_arr, "alignment structural")
        response = self.__make_api_call(alighnment_structural_url, params)
        return response.json()

    def call_feedback_fix_endpoint(self, language, reference_solution, student_solution, function,
                                   inputs, args):
        """
        Returns the response of the call to the feedback fix service endpoint of the ITS API
        """
        feedback_fix_url = self.BASE_API_URL + "feedback_fix"
        param_arr = [language, reference_solution, student_solution, function, inputs, args]
        params = self.__package_params(param_arr, "feedback_fix")
        response = self.__make_api_call(feedback_fix_url, params)
        return response.json()
