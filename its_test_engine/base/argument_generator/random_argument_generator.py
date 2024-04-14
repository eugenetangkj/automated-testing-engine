'''
Randomly generates the arguments for a function given its
function signature
'''
import random
import string
from .base_argument_generator import BaseArgumentGenerator


class RandomArgumentGenerator(BaseArgumentGenerator):
    def _generate_random_integer(self, min_value=0, max_value=1e2):
        """
        Helper function that generates a random integer in a given range

        Parameters:
            min_value: Minimum integer to consider (inclusive)
            max_value: Maximum integer to consider (inclusive)
        
        """
        return random.randint(min_value, max_value)

    def _generate_random_float(self, min_value=-1e2, max_value=1e2):
        """
        Helper function that generates a random float in a given range

        Parameters:
            min_value: Minimum float to consider (inclusive)
            max_value: Maximum float to consider (inclusive)
        
        """
        return random.uniform(min_value, max_value)

    def _generate_random_string(self, length=10):
        """
        Helper function that generates a random string given a length.
        Characters of the string are only letters or digits.

        Parameters:
            length: Length of the random string generated
        
        """
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for _ in range(length))

    def _generate_random_boolean(self):
        """
        Helper function that generates a random Boolean

        """
        return random.choice([True, False])

    def generate_arguments(
        self, function_signature: dict, code: str, no_of_arguments: int
    ):
        """
        Generate arguments based on randomisation

        Parameters:
            function_signature: Function signature of function which we are
            generating arguments for.

            code: String representing the function

            no_of_arguments: Number of sets of arguments we want to generate.
            For example, for f(a, b), no_of_arguments = 2 could mean
            generating (1, 2) and (3, 5).
        
        """
        results = []
        for _ in range(no_of_arguments):
            inputs = []
            for t in function_signature["argument_types"]:
                if t == "int":
                    inputs.append(self._generate_random_integer())
                elif t == "float":
                    inputs.append(self._generate_random_float())
                elif t == "str":
                    inputs.append(self._generate_random_string())
                elif t == "bool":
                    inputs.append(self._generate_random_boolean())
                elif t == "List[int]":
                    inputs.append([self._generate_random_integer() for _ in range(10)])
                elif t == "List[float]":
                    inputs.append([self._generate_random_float() for _ in range(10)])
                elif t == "List[str]":
                    inputs.append([self._generate_random_string() for _ in range(10)])
                elif t == "List[bool]":
                    inputs.append([self._generate_random_boolean() for _ in range(10)])

            results.append(inputs)
        return results
