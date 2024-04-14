"""
    Abstract class for base argument generator
"""

from abc import ABC, abstractmethod


class BaseArgumentGenerator(ABC):
    """
    This is an abstract class from which concrete argument generator classes would
    extend from.
    """

    def __init__(self):
        """
        Initialisation method for a BaseArgumentGenerator instance
        """

    @abstractmethod
    def generate_arguments(
        self, function_signature: dict, code: str, no_of_arguments: int
    ):
        """
        Abstract method to be overridden by concrete argument generator classes.
        This method aims to generate possible arguments for a function given
        its function signature

        Parameters:
            function_signature: A dictionary containing the function signature
            code: The code snippet for the function
            no_of_arguments: Number of sets of arguments to be generated
        """