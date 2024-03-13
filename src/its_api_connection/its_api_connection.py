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
    
    ## Insert other methods of ItsApiConnection here

    def __make_api_call(self, url, params):
        return requests.post(url, json=params)

    def __package_params(self, language, source_code):
        return {"language": language, "source_code": source_code}

    def call_parser_endpoint(self, language, source_code):
        """Returns the response of the call to the parser endpoint of the ITS API"""
        parser_url = self.BASE_API_URL + "parser"
        params = self.__package_params(language, source_code)
        response = self.__make_api_call(parser_url, params)
        return response.json()

