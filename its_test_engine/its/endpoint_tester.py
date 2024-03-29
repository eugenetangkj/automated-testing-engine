"""
    Abstract class for end point tester
"""

from abc import ABC, abstractmethod
from .api_output_comparator import ApiOutputComparator
from .its_api_connection import ItsApiConnection
from ..enums.type_of_metamorphic_relation import TypeOfMetamorphicRelation
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
    def check_status_of_result(self, api_result: dict):
        """
        Abstract method to be overridden by concrete endpoint tester classes.
        This method determines if a result is considered success or failure depending on
        type of metamorphic relation being tested.

        Parameters:
            api_result: Dictionary output from API
        """
