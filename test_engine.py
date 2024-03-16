from src.its_api_connection import ItsApiConnection
from src.metamorphic_program_modifier import MetamorphicProgramModifier, AddCommentProgramModifier
from src.base_program_generator import BaseProgramGenerator, CsmithProgramGenerator, OpenAiProgramGenerator
from src.api_output_comparator import ApiOutputComparator
from src.inter_representation_processer import InterRepresentationProcesser
import json

class TestEngine(object):
    """
    This class is the test engine responsible for running test cases against metamorphic relations
    and writing potential bugs to a data file. It acts as the main point of entry for the app.
    
    Attributes:
        PATH_OF_ERROR_FILE (str): Path of file that contains the errors detected
        its_api_connection (ItsApiConnection): To connect to the ITS API
        csmith_base_program_generator (CsmithProgramGenerator): To generate random C base programs
        openai_base_program_generator (OpenAiProgramGenerator): To generate random C and Python base programs

    """

    PATH_OF_ERROR_FILE = "" # To be updated again

    def __init__(self):
        """
        Initialisation method for a TestEngine instance
        """
        self.its_api_connection = ItsApiConnection()
        self.csmith_base_program_generator = CsmithProgramGenerator()
        self.openai_base_program_generator = OpenAiProgramGenerator()
        self.api_output_comparator = ApiOutputComparator()
        self.inter_representation_processer = InterRepresentationProcesser()
    
    ## Insert other methods of TestEngine here
    #TODO: Handle different languages
    def test_add_comment_relation(self):
        # Prepares the program modifier
        add_comment_program_modifier = AddCommentProgramModifier()




        # Step 1: Generate a random base program
        # base_program_string = self.openai_base_program_generator.generate_test_case('py', '')
        base_program_string = "int power(int base, int exponent) {\n\tint result = 1;\n\twhile (exponent > 0) {\n\t\tresult *= base;\n\t\texponent--;\n\t}\n\treturn result;\n}"

        # Step 2: Modify the base program
        modified_program_string = add_comment_program_modifier.modify_program("c", base_program_string)

        
        # Step 3: Put the base and modified programs into parser end point to get intermediate representation
        base_program_intermediate_representation_dict = self.its_api_connection.call_parser_endpoint("c", base_program_string)
        modified_program_intermediate_representation_dict = self.its_api_connection.call_parser_endpoint("c", modified_program_string)
        

        # Step 4: Extract information from intermediate representation
        program_information = self.inter_representation_processer.break_down_inter_representation_c(base_program_intermediate_representation_dict)

      
        
        # Step 5: Write to feedback fix API to check for discrepencies
        output = self.its_api_connection.call_feedback_fix_endpoint(
            "c",
            json.dumps(base_program_intermediate_representation_dict, indent=4),
            json.dumps(modified_program_intermediate_representation_dict, indent=4),
            program_information["function"],
            program_information["inputs"],
            "[2], [3]"
        )


        print(output)
       
        











        # Uncomment this to try the openai base program generator
        # print(self.openai_base_program_generator.generate_test_case('py', '1 while loop'))


        
if __name__ == "__main__":
    # Main driver method that creates an instance of TestEngine
    # and runs it to execute the test cases
    test_engine = TestEngine()

    test_engine.test_add_comment_relation()
