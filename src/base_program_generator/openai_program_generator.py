from .base_program_generator import BaseProgramGenerator
from dotenv import load_dotenv
from openai import OpenAI
import os
import httpx
import json
import random
import re

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
    SYSTEM_PROMPT_C = "Create a totally random c function given constraints. " + \
        "The function takes either 0 or 1 argument, whose type must be a NUMBER. " + \
        "Just return the function in a single line without the prefix ###Function. " + \
        "Examples:\n"


    SYSTEM_PROMPT_PY =  "Create a totally random py function given constraints. " + \
        "The function takes either 0 or 1 argument, whose type must be int, float or none if there is no argument." + \
        "Return the function in a single line " + \
        "and return the type of the argument in the next line." + \
        "Examples:\n"
    
    
    # Few-shot learning for Python
    SAMPLE_PY_PROGRAMS = "###Constraints: None\n" + \
        "###Function: def generate_random_number():\n\timport random\n\treturn random.randint(1, 100)" + \
        "###Type: none\n" + \
        "---\n" + \
        "###Constraints: Have 1 while loop\n" + \
        "###Function: def sum_of_digits(n):\n\ttotal = 0\n\twhile n > 0:\n\t\ttotal += int(n % 10)\n\t\tn //= 10\n\treturn total\n" + \
        "###Type: float"

    
    # Few-shot learning for C
    SAMPLE_C_PROGRAMS = "###Constraints: Have 1 for loop\n" + \
        "###Function: #include <stdio.h>\n\nint sum_of_squares(int n) {\n\tint sum = 0;\n\tfor (int i = 1; i <= n; i++) {\n\t\tsum += i * i;\n\t}\n\treturn sum;\n}\n" + \
        "---\n" + \
        "###Constraints: Use 2 include statements\n" + \
        "###Function: #include <stdio.h>\n#include <math.h>\n\nfloat calculate_square_root(float num) {\n\treturn sqrt(num);\n}"
    


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
            user_prompt = self.__generate_user_prompt(constraints)
            system_prompt = self.SYSTEM_PROMPT_C + self.SAMPLE_C_PROGRAMS if (language == 'c') else self.SYSTEM_PROMPT_PY + self.SAMPLE_PY_PROGRAMS

            output = system_prompt
            response = self.OPENAI_CLIENT.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt },
                    {"role": "user", "content": user_prompt }
                ],
                temperature=1, # We want more randomness in generating these base programs
            )

            # Extract output from API
            program_string = response.choices[0].message.content
            output = self.__process_newlines_and_tabs(program_string)

            if (language == 'py'):
                output = self.__process_data(output)
            else:
                output = {
                    "program": output,
                    "data_type": ""
                }
            return output
        
        except httpx.TimeoutException:
            # OpenAI API takes too long to create a test case. We just fetch one randomly from the pre-generated list.
            # However, for now, this means that we cannot take into consideration the constraints.
            return self.__get_random_program_from_file(language)



    def __generate_user_prompt(self, constraints):
        """
        Prompt engineers a user prompt to be passed into the OpenAI model

        Parameters:
            constraints: A string indicating some constraints and guidelines to generate the base program with.
        
        """

        return f"###Constraints: { constraints }"
        

    def __process_newlines_and_tabs(self, raw_program_string):
        """
        Transforms newlines and tabs into \n and \t respectively, as required for the ITS API input.
        Also removes filler content that is sometimes returned by OpenAI's API

        Note that OpenAi's output returns 4 whitespace characters in lieu of tabs.
        
        """

        # Python programs
        if (raw_program_string.startswith("```py\n") and raw_program_string.endswith("\n```")):
            processed_program_string = raw_program_string[6:-4].replace('\n', '\n').replace('    ', '\t')
            return processed_program_string
        
        # C programs
        elif (raw_program_string.startswith("```c\n") and raw_program_string.endswith("\n```")):
            processed_program_string = raw_program_string[5:-4].replace('\n', '\n').replace('    ', '\t')
            return processed_program_string
        else:
            # Input is as intended
            processed_program_string = raw_program_string.replace('\n', '\n').replace('    ', '\t')
            return processed_program_string


    def __process_data(self, output):
        """
        Removes the labels from the raw input

        Parameters:
            output: The program to be processed
        
        """
        # Obtained from ChatGPT
        function_pattern = re.compile(r'###Function: (.+?)###Type:', re.DOTALL)
        type_pattern = re.compile(r'###Type: (.+)', re.DOTALL)
        function_match = function_pattern.search(output)
        type_match = type_pattern.search(output)

        raw_program = function_match.group(1).strip()
        data_type = type_match.group(1).strip()

        return {
            "program": raw_program,
            "data_type": data_type
        }


    def __get_random_program_from_file(self, language):
        """
        Retrieves a random program string from a file of pre-generated programs

        Parameters:
        language: Language of program to retrieve, either c or python

        """
        if (language == 'c'):
            with open('././datafiles/random_py_programs.json', 'r') as file:
                    data = json.load(file)
                    base_program_string = random.choice(data)
            
            return {
                    "program": base_program_string,
                    "data_type": ""
            }

        else:
            with open('././datafiles/random_py_programs.json') as file:
                    random_py_programs = json.load(file)
                
            random_index = random.randrange(len(random_py_programs))

            with open('././datafiles/random_py_datatypes.json') as file:
                random_data_types = json.load(file)

            base_program_string = random_py_programs[random_index]
            base_program_data_type = random_data_types[random_index]

            return {
                "program": base_program_string,
                "data_type": base_program_data_type
            }

