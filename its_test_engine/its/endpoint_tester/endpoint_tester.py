"""
    Abstract class for end point tester
"""

from abc import ABC, abstractmethod
from its_test_engine.enums import TypeOfMetamorphicRelation, Language
from its_test_engine.its.its_api_connection import ItsApiConnection


class EndpointTester(ABC):
    """
    This is an abstract class from which concrete end point testers inherit from. This is
    because the error localizer, feedback fix, feedback error and repair endpoints work rather
    similarly, taking in similar inputs and having similar outputs for the API endpoints.

    """

    def __init__(
        self,
        its_api_connection: ItsApiConnection,
        type_of_metamorphic_relation: TypeOfMetamorphicRelation = TypeOfMetamorphicRelation.EQUIVALENT,
    ):
        """
        Initialisation method for a EndpointTester instance
        """
        self.its_api_connection = its_api_connection
        self.type_of_metamorphic_relation = type_of_metamorphic_relation

    @abstractmethod
    def run_test(
        self,
        function_signature: str,
        base_program_string: str,
        modified_program_string: str,
        parsed_base_program: str,
        parsed_modified_program: str,
        arguments: list[any],
    ):
        """
        Abstract method to be overridden by concrete endpoint tester classes.
        This method aims to generate an test result instance that represents the
        outcome of testing a test case with the endpoint.

        Returns:
           A TestResult instance containing the information regarding the outcome
           of testing the test case with the endpoint, if not successful. If successful,
           return None.
        """
