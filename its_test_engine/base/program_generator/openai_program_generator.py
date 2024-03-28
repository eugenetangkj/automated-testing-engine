"""
    Generates a random program using OpenAI LLM, gpt-3.5-turbo
"""

import json
import os
import httpx
from dotenv import load_dotenv
from openai import OpenAI
from its_test_engine.base.program_generator.base_program_generator import (
    BaseProgramGenerator,
)


load_dotenv()  # Loads environment variables for OpenAI API key


class OpenAiProgramGenerator(BaseProgramGenerator):
    """
    This class generates a random program using the OpenAI LLM. More information can be found at
    https://platform.openai.com/docs/api-reference?lang=python.

    """

    # OpenAI client instance
    # Adapted from https://community.openai.com/t/setting-request-timeout-in-openai-v1-2-2/492772
    OPENAI_CLIENT = OpenAI(
        api_key=os.environ.get("CS3213_OPENAI_API_KEY"), timeout=httpx.Timeout(20.0)
    )

    SYSTEM_PROMPT_PY = (
        "Create a totally random py function given constraints. Be creative! " +\
        "The function takes arguments of only pure numeric types int, float or double. and it cannot have import statements. " +\
        "Return the function, name of function, the argument types and return type in the format of a JSON. Examples:\n"
    )

    # Few-shot learning for Python
    SAMPLE_PY_PROGRAMS = (
        "###Constraints: Have 1 while loop\n" +\
        "###Output: " +\
        '''{"function": "def countdown(n):\n\twhile n >= 0:\n\t\tprint(n)\n\t\tn -= 1", "name": "countdown", "arguments": ["int"], "return_type": "none"}''' +\
        "\n\n"
        "###Constraints: None\n" +\
        "###Output: " +\
        '''{"function": "def sum_of_two_digits(x, y):\n\treturn x + y", "name": "sum_of_two_digits", "arguments": ["int", "int"], "return_type": "int"}'''
    )


    def __init__(self, language: str, constraints: str):
        """
        Initialisation method for a OpenAiProgramGenerator instance

        Parameters:
            language: A string indicating the language in which the base program is written in.
            constraints: A string indicating some constraints and guidelines to generate the
                         base program with.
        """
        super().__init__()
        self.language = language
        self.constraints = constraints


    def generate_test_case(self):
        """
        Generates a random base program written in a given language with
        specific constraints to guide the creation of the base program.

        """

        # Calls the chat completion API to generate the base program
        try:
            # Generate user prompt
            user_prompt = self.__generate_user_prompt(self.constraints)

            # Prepare system prompt
            if self.language == "py":
                system_prompt = self.SYSTEM_PROMPT_PY + self.SAMPLE_PY_PROGRAMS
            else:
                system_prompt = "" # TODO: Update system prompt for C programs

            # Call OpenAI API
            response = self.OPENAI_CLIENT.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=1.5,  # We want more randomness in generating these base programs
                response_format={ "type": "json_object" } # We want to get a JSON object
            )

            # Extract output from API
            json_string = response.choices[0].message.content
            json_object = json.loads(json_string)
            base_program_string = json_object["function"]
            function_name = json_object["name"]
            arguments = json_object["arguments"]
            return_type = json_object["return_type"]

            # Pack outputs together into a tuple
            output = (base_program_string, {
                "name": function_name,
                "arguments": arguments,
                "return_type": return_type,
            })

            return output

        except httpx.TimeoutException:
            # OpenAI API takes too long to create a test case. We just move on.
            return None

        except json.decoder.JSONDecodeError as decode_error:
            # OpenAI API gives invalid output. We just move on.
            print(decode_error)
            return None

    def __generate_user_prompt(self, constraints):
        """
        Prompt engineers a user prompt to be passed into the OpenAI model

        Parameters:
            constraints: A string indicating some constraints and guidelines to generate
                        the base program with.

        """

        return f"###Constraints: { constraints }"
