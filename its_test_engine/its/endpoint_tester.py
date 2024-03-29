"""
    Abstract class for end point tester
"""

from abc import ABC, abstractmethod
from .api_output_comparator import ApiOutputComparator
from .its_api_connection import ItsApiConnection
from ..enums.type_of_metamorphic_relation import TypeOfMetamorphicRelation


class EndpointTester(ABC):
    """
    This is an abstract class from which concrete end point testers inherit from. This is
    because the error localizer, feedback fix, feedback error and repair endpoints work rather
    similarly, taking in similar inputs and having similar outputs for the API endpoints.

    """

    def __init__(self, api_output_comparator: ApiOutputComparator,
                 its_api_connection: ItsApiConnection,
                 type_of_metamorphic_relation: TypeOfMetamorphicRelation
                 ):
        """
        Initialisation method for a EndpointTester instance
        """
        self.api_output_comparator = api_output_comparator
        self.its_api_connection = its_api_connection
        self.type_of_metamorphic_relation = type_of_metamorphic_relation

    @abstractmethod
    def test_endpoint(self,
                      base_program_string: str,
                      modified_program_string: str,
                      base_program_intermediate: dict,
                      modified_program_intermediate: dict,
                      language: dict,
                      function_name: str,
                      function_arguments_processed:str):
        """
        Abstract method to be overridden by concrete endpoint tester classes.
        This method aims to generate an test result instance that represents the
        outcome of testing a test case with the endpoint.

        Returns:
           A TestResult instance containing the information regarding the outcome
           of testing the test case with the endpoint, if not successful. If successful,
           return None.
        """

        # self, base_program_string, modified_program_string, base_program_intermediate,
        #               modified_program_intermediate, language, function_name,
        #               function_arguments_processed

    @abstractmethod
    def check_status_of_result(self, api_result: dict):
        """
        Abstract method to be overridden by concrete endpoint tester classes.
        This method determines if a result is considered success or failure depending on
        type of metamorphic relation being tested.

        Parameters:
            api_result: Dictionary output from API
        """
