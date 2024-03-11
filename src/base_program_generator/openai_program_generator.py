from .base_program_generator import BaseProgramGenerator
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv() # Loads environment variables for OpenAI API key

class OpenAiProgramGenerator(BaseProgramGenerator):
    """
    This class generates a random program using the OpenAI LLM. More information can be found at
    https://platform.openai.com/docs/api-reference?lang=python.
    
    """
    OPENAI_CLIENT = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


    # Prompt constants
    # Adapted from https://community.openai.com/t/convert-few-shot-example-to-api-code/325614/2
    SYSTEM_PROMPT = "You are a generator of random functions. " + \
        "You will be given a language from the ###Language: section " + \
        "and constraints from the ###Constraints: section. " + \
        "Generate a simple function in the language while adhering to the constraints. " + \
        "The output is 1 single string, using \\n for newlines and \\t for tabs. " + \
        "Here are some examples:\n\n"
    
    
    
    SAMPLE_PYTHON_PROGRAMS = "###Language: Py\n" + \
        "###Constraints: None\n" + \
        "###Output: def add_numbers(a, b):\\n\\treturn a + b\n" + \
        "---\n" + \
        "###Language: Py\n" + \
        "###Constraints: Have 1 while loop\n" + \
        "###Output: def factorial(n):\\n\\tresult = 1\\n\\twhile n > 1:\\n\\t\\tresult *= n\\n\\t\\tn -= 1\\n\\treturn result\n" + \
        "---\n" + \
        "###Language: Py\n" + \
        "###Constraints: Have 1 for loop\n" + \
        "###Output: def sum_of_numbers(n):\\n\\tsum_result = 0\\n\\tfor i in range(1, n+1):\\n\\t\\tsum_result += i\\n\\treturn sum_result\n" + \
        "---\n" + \
        "###Language: Py\n" + \
        "###Constraints: Use an import statement\n" + \
        "###Output: import math\\n\\ndef calculate_square_root(n):\\n\\treturn math.sqrt(n)"


    # TODO: Update if confirm Python programs work
    SAMPLE_C_PROGRAMS = ""

     
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

        # Calls the chat completion API to generate the base program
        user_prompt = self.__generate_user_prompt(language, constraints)
        response = self.OPENAI_CLIENT.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt }
            ]
        )

        return response





    def __generate_user_prompt(self, language, constraints):
        """

        Prompt engineers a user prompt to be passed into the OpenAI model

        Parameters:
            language: A string indicating the language in which the base program is written in.
            constraints: A string indicating some constraints and guidelines to generate the base program with.
        """

        return "Hello"


    def test_string(self):
        return self.SYSTEM_PROMPT + self.SAMPLE_PYTHON_PROGRAMS





