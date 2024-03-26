"""
    Abstract class for base input generator
"""

from abc import ABC, abstractmethod
from typing import List


class BaseInputGenerator(ABC):
    """
    This is an abstract class from which concrete input generator classes would extend from.
    """

    def __init__(self):
        """
        Initialisation method for a BaseInputGenerator instance
        """

    @abstractmethod
    def generate_inputs(self, arguments_types: list[str], no_of_inputs: int):
        """
        Abstract method to be overridden by concrete program generator classes.
        This method aims to generate a random base program written in a given language with
        specific constraints to guide the creation of the base program.

        Parameters:
            arguments_types: A list of strings indicating the types of the arguments of the function.
                For example, ["int", "int"] indicates that the function has two arguments of type int.

        """
