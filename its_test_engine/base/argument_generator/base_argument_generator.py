"""
    Abstract class for base input generator
"""

from abc import ABC, abstractmethod


class BaseArgumentGenerator(ABC):
    """
    This is an abstract class from which concrete input generator classes would extend from.
    """

    def __init__(self):
        """
        Initialisation method for a BaseArgumentGenerator instance
        """

    @abstractmethod
    def generate_arguments(
        self, function_signature: dict, code: str, no_of_inputs: int
    ):
        """
        Abstract method to be overridden by concrete program generator classes.
        This method aims to generate a random base program written in a given language with
        specific constraints to guide the creation of the base program.

        Parameters:
            function_signature: A dictionary containing the function signature
            code: The code snippet to be tested
            no_of_inputs: Number of inputs to be generated

        """
