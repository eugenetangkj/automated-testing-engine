"""
    Abstract class for base program generator
"""

from abc import ABC, abstractmethod
from typing import Tuple


class BaseProgramGenerator(ABC):
    """
    This is an abstract class from which concrete program generator classes would extend from.
    Subclasses that extend this class are responsible for generating random programs (c or py).
    These random programs generated are the base programs which will be modified to
    test the metamorphic relations.

    """

    def __init__(self):
        """
        Initialisation method for a BaseProgramGenerator instance
        """

    @abstractmethod
    def generate_test_case(self) -> Tuple[any, str]:
        """
        Abstract method to be overridden by concrete program generator classes.
        This method aims to generate a random base program written in a given language.

        Returns:
            A tuple containing the function signature and the code of the base program.
            The function signature is a dictionary with the following keys and values:
                - "name": the name of the function
                - "arguments": a list of dictionaries, each containing the following keys and values:
                    - "name": the name of the argument
                    - "type": the type of the argument
                - "return_type": the return type of the function
            The code is a string containing the code of the base program.

        """
