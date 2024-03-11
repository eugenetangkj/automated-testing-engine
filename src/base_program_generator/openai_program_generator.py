from .base_program_generator import BaseProgramGenerator
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # Loads environment variables for OpenAI API key

class OpenAiProgramGenerator(BaseProgramGenerator):
    """
    This class generates a random program using the OpenAI LLM. More information can be found at
    https://platform.openai.com/docs/api-reference?lang=python.
    
    """

    def __init__(self):
        """
        Initialisation method for a OpenAiProgramGenerator instance
        """
        pass
    

    def generate_test_case(self, language, constraints):
        """
        Generates a random base program written in a given language with
        specific constraints to guide the creation of the base program.

        Parameters:
            language: A string indicating the language in which the base program is written in.
            constraints: A string indicating some constraints and guidelines to generate the base program with.

        """

        # TODO: Implement logic for generating test case
        pass




