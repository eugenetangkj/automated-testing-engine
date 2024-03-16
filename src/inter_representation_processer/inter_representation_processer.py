import random;
import string;

class InterRepresentationProcesser(object):
    """
    This class breaks down the intermediate representation of a program obtained from the parser API into smaller
    parts that are needed to be put into the other ITS API calls.
    
    """


    def __init__(self):
        """
        Initialisation method for a BaseProgramGenerator instance
        """
        pass
    

    def break_down_inter_representation_c(self, inter_representation):
        """
        Breaks down the intermediate representation for a c program

        Parameters:
            inter_representation: Intermediate representation of a program to be broken down

            
        - language: c | py
        - reference_solution: string
        - student_solution: string
        - function: string (the entry function of the program)
        - inputs: IO inputs
        - args: arguments of the entry function (for e.g. "[2]") (string wrapped in '[]')
        """
    
        # Retrieves function information
        # Assume base programs have only 1 function
        function_name_output = next(iter(inter_representation["fncs"]))

        # Assumes empty inputs
        inputs_output = ""

        # Determine arguments for the single function
        parameter_data_types = []
        parameter_information = inter_representation["fncs"][function_name_output]['params']
        for parameter in parameter_information:
            parameter_name = parameter["val0"]
            parameter_type = parameter["val1"]

            # Check if item is an array
            if ("[]" in parameter_name):
                parameter_type += "[]"
            
            parameter_data_types.append(parameter_type)


        parameter_string_output = ""

        if (len(parameter_data_types) != 0):
            parameter_string_output = "["
            for parameter_data_type in parameter_data_types:
                parameter_string_output += self.__generate_random_argument_c(parameter_data_type)
                parameter_string_output += ", "


            parameter_string_output = parameter_string_output[:-2] + ']'

        return {
            "function": function_name_output,
            "inputs": inputs_output,
            "args": parameter_string_output
        }


    def __generate_random_argument_c(self, data_type):
        """
            Randomly generates an argument given a data type in c

            Parameters:
                data_type: String representing the data type

        """
        if (data_type == "int"):
            # Random int between 1 to 10
            return str(random.randint(1, 10))
        
        elif (data_type =="float" or data_type == "double"):
            # Random float or double between 1 to 10
            return str(random.uniform(1, 10))
        
        elif (data_type == "char"):
            # Random char between A to z
            return "'" + random.choice(string.ascii_letters) + "'"
        
        elif (data_type == "int[]"):
            # A list with a random number of random integers.
            # Size is between 1 to 10, and integers range between 1 to 10
            random_list_length = random.randint(1, 10)
            random_list = [random.randint(1, 10) for _ in range(random_list_length)]
            random_list_string = "{" + ", ".join(map(str, random_list)) + "}"
            return random_list_string
        
        elif (data_type == "float[]" or data_type == "double[]"):
            # A list with a random number of random floats.
            # Size is between 1 to 10, and floats range between 1 to 10
            random_list_length = random.randint(1, 10)
            random_list = [random.uniform(1, 10) for _ in range(random_list_length)]
            random_list_string = "{" + ", ".join(map(str, random_list)) + "}"
            return random_list_string
        
        else:
            # A character array in c is just a string
            # Randomly generate a string with a random size of between 1 to 10
            # Characters can only be upper or lower case letters
            possible_characters = string.ascii_letters
            random_string = ''.join(random.choice(possible_characters) for _ in range(random.randint(1, 10)))
            return "\"" + random_string + "\""
    
