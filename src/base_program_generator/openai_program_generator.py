from .base_program_generator import BaseProgramGenerator
from dotenv import load_dotenv
from openai import OpenAI
import os
import httpx
import json
import random

load_dotenv() # Loads environment variables for OpenAI API key

class OpenAiProgramGenerator(BaseProgramGenerator):
    """
    This class generates a random program using the OpenAI LLM. More information can be found at
    https://platform.openai.com/docs/api-reference?lang=python.
    
    """

    # OpenAI client instance
    # Adapted from https://community.openai.com/t/setting-request-timeout-in-openai-v1-2-2/492772
    OPENAI_CLIENT = OpenAI(api_key=os.environ.get("CS3213_OPENAI_API_KEY"), timeout=httpx.Timeout(20.0))


    # Prompt constants
    # Adapted from https://community.openai.com/t/convert-few-shot-example-to-api-code/325614/2
    SYSTEM_PROMPT = "Create a totally random function given a language and constraints. " + \
        "Just return the function in a single line without the prefix ###Function, using \\n for newlines and \\t for tabs. " + \
        "Examples:\n"
    
    # Few-shot learning for Python
    SAMPLE_PY_PROGRAMS = "###Language: py\n" + \
        "###Constraints: None\n" + \
        "###Function: def add_numbers(a, b):\\n\\treturn a + b\n" + \
        "---\n" + \
        "###Language: py\n" + \
        "###Constraints: Have 1 while loop\n" + \
        "###Function: def factorial(n):\\n\\tresult = 1\\n\\twhile n > 1:\\n\\t\\tresult *= n\\n\\t\\tn -= 1\\n\\treturn result"

    
    # Few-shot learning for C
    SAMPLE_C_PROGRAMS = "###Language: c\n" + \
        "###Constraints: Have 1 for loop\n" + \
        "###Output: #include <stdio.h>\\n\\nint sum_of_squares(int n) {\\n\\tint sum = 0;\\n\\tfor (int i = 1; i <= n; i++) {\\n\\t\\tsum += i * i;\\n\\t}\\n\\treturn sum;\\n}\n" + \
        "---\n" + \
        "###Language: c\n" + \
        "###Constraints: Use 2 include statements\n" + \
        "###Output: #include <stdio.h>\\n#include <math.h>\\n\\nfloat calculate_square_root(float num) {\\n\\treturn sqrt(num);\\n}"
    

    # File path of pre-generated random C programs
    PATH_PREGENERATED_C_PROGRAMS = "src\\base_program_generator\\random_c_programs.json"

    # File path of pre-generated random Python programs
    PATH_PREGENERATED_PY_PROGRAMS = "src\\base_program_generator\\random_py_programs.json"


 
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
        try:
            user_prompt = self.__generate_user_prompt(language, constraints)
            response = self.OPENAI_CLIENT.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT + (self.SAMPLE_PY_PROGRAMS if (language == 'py') else self.SAMPLE_C_PROGRAMS)},
                    {"role": "user", "content": user_prompt }
                ],
                temperature=1.5, # We want more randomness in generating these base programs
            )

            # Extract output from API
            program_string = response.choices[0].message.content
            output = self.__process_newlines_and_tabs(program_string)

            return output
        
        except httpx.TimeoutException:
            # OpenAI API takes too long to create a test case. We just fetch one randomly from the pre-generated list.
            # However, for now, this means that we cannot take into consideration the constraints.
            return self.__get_random_program_from_file(language)



    def __generate_user_prompt(self, language, constraints):
        """
        Prompt engineers a user prompt to be passed into the OpenAI model

        Parameters:
            language: A string indicating the language in which the base program is written in.
            constraints: A string indicating some constraints and guidelines to generate the base program with.
        
        """

        return f"###Language: { language }\n" + \
            f"###Constraints: { constraints }"
        

    def __process_newlines_and_tabs(self, raw_program_string):
        """
        Transforms newlines and tabs into \\n and \\t respectively, as required for the ITS API input.
        Also removes filler content that is sometimes returned by OpenAI's API

        Note that OpenAi's output returns 4 whitespace characters in lieu of tabs.
        
        """

        # Python programs
        if (raw_program_string.startswith("```py\n") and raw_program_string.endswith("\n```")):
            processed_program_string = raw_program_string[6:-4].replace('\n', '\\n').replace('    ', '\\t')
            return processed_program_string
        
        # C programs
        elif (raw_program_string.startswith("```c\n") and raw_program_string.endswith("\n```")):
            processed_program_string = raw_program_string[5:-4].replace('\n', '\\n').replace('    ', '\\t')
            return processed_program_string
        else:
            # Input is as intended
            processed_program_string = raw_program_string.replace('\n', '\\n').replace('    ', '\\t')
            return processed_program_string


    def __get_random_program_from_file(self, language):
        """
        Retrieves a random program string from a file of pre-generated programs

        Parameters:
        language: Language of program to retrieve, either c or python

        """

        # Retrieve correct file path
        file_path = self.PATH_PREGENERATED_C_PROGRAMS if (language == 'c') else self.PATH_PREGENERATED_PY_PROGRAMS

        # Fetch program from file
        with open(file_path, 'r') as file:
            data = json.load(file)
            if (data):
                return random.choice(data)
            else:
                return 'No program!'
