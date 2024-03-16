"""
    Abstract class for base program generator
"""
from abc import abstractmethod

class BaseProgramGenerator(object):
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
    def generate_test_case(self, language, constraints):
        """
        Abstract method to be overridden by concrete program generator classes.
        This method aims to generate a random base program written in a given language with
        specific constraints to guide the creation of the base program.

        Parameters:
            language: A string indicating the language in which the base program is written in.
            constraints: A string indicating some constraints and guidelines to generate the base
                         program with.

        """
