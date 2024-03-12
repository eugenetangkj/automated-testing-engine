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

    def call_parser_endpoint(self, language, source_code):
        """Returns the response of the call to the parser endpoint of the ITS API"""
        parser_url = self.BASE_API_URL + "parser"
        print(parser_url)
        params = {"language": language, "source_code": source_code}
        response = requests.post(parser_url, json=params)
        print(response.json())
        return response.json()
