from abc import ABC, abstractmethod
import math

class MetamorphicRelationTester(object):
    """
    This is an abstract class from which concrete metamorphic relation testers will inherit from.
    
    """

    def __init__(self, number_of_test_cases):
        """
        Initialisation method for a MetamorphicRelationTester instance

        Parameters:
            number_of_test_cases: Number of test cases to generate for testing this relation
        """
        self.number_of_test_cases = number_of_test_cases
    
    @abstractmethod
    def test_relation(self):
        """
        Abstract method to be overridden by concrete metamorphic relation tester classes.
        This method aims to generate programs to test for the relation

        """
        pass


    def get_number_of_c_test_cases(self):
        """
            Obtains the number of c test cases by dividing by 2, rounding up
        """
        return math.ceil(self.number_of_test_cases / 2)
    

    def get_number_of_py_test_cases(self):
        """
            Obtains the number of py test cases by dividing by 2, rounding down
        """
        return math.floor(self.number_of_test_cases / 2)
    



