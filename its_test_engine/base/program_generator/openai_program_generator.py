"""
    Generates a random program using OpenAI LLM, gpt-3.5-turbo
"""

import json
import random
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
        "Create a totally random and creative py function given constraints. " +\
        "The function takes arguments of only pure numeric types int, float or double. and it cannot have import statements. " +\
        "Return the function and the argument types in the format of a JSON. Examples:\n"
    )

    # Few-shot learning for Python
    SAMPLE_PY_PROGRAMS = (
        "###Constraints: Have 1 while loop\n" +\
        "###Output: " +\
        '''{"function": "def countdown(n):\n\twhile n >= 0:\n\t\tprint(n)\n\t\tn -= 1", "arguments": ["int"]}''' +\
        "\n\n"
        "###Constraints: None\n" +\
        "###Output: " +\
        '''{"function": "def sum_of_two_digits(x, y):\n\treturn x + y", "arguments": ["int", "int"]}'''
    )


    def __init__(self):
        """
        Initialisation method for a OpenAiProgramGenerator instance
        """

    def generate_test_case(self, language, constraints):
        """
        Generates a random base program written in a given language with
        specific constraints to guide the creation of the base program.

        Parameters:
            language: A string indicating the language in which the base program is written in.
            constraints: A string indicating some constraints and guidelines to generate the
                         base program with.

        """

        # Calls the chat completion API to generate the base program
        try:
            # Generate user prompt
            user_prompt = self.__generate_user_prompt(constraints)

            # Prepare system prompt
            if language == "py":
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
            base_program_string, arguments = json_object["function"], json_object["arguments"]

            return base_program_string, arguments



        except httpx.TimeoutException:
            # OpenAI API takes too long to create a test case. We just fetch one randomly
            # from the pre-generated list. However, for now, this means that we cannot take
            # into consideration the constraints.
            return self.__get_random_program_from_file(language)

    def __generate_user_prompt(self, constraints):
        """
        Prompt engineers a user prompt to be passed into the OpenAI model

        Parameters:
            constraints: A string indicating some constraints and guidelines to generate
                        the base program with.

        """

        return f"###Constraints: { constraints }"


        """
        Converts the raw JSON string from OpenAI API into a JSON, and extract the function and arguments type.

        Parameters:
            raw_json: Raw JSON string obtained from chat completions API
        """
        # Convert raw string into a JSON object
        print(raw_json)
        # program_json = json.loads(raw_json)
        # base_program_string = program_json['function']
        # arguments = program_json['arguments']
        # return base_program_string, arguments
        return 1, 1

    def __get_random_program_from_file(self, language):
        """
        Retrieves a random program string from a file of pre-generated programs

        Parameters:
        language: Language of program to retrieve, either c or python

        """
        if language == "c":
            with open(
                "././datafiles/random_py_programs.json", "r", encoding="utf-8"
            ) as file:
                data = json.load(file)
                base_program_string = random.choice(data)

            return {"program": base_program_string, "data_type": ""}

        else:
            with open(
                "././datafiles/random_py_programs.json", "r", encoding="utf-8"
            ) as file:
                random_py_programs = json.load(file)

            random_index = random.randrange(len(random_py_programs))

            with open(
                "././datafiles/random_py_datatypes.json", "r", encoding="utf-8"
            ) as file:
                random_data_types = json.load(file)

            base_program_string = random_py_programs[random_index]
            base_program_data_type = random_data_types[random_index]

            return {"program": base_program_string, "data_type": base_program_data_type}
