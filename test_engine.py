from src.its_api_connection import ItsApiConnection
from src.metamorphic_program_modifier import MetamorphicProgramModifier, AddCommentProgramModifier
from src.base_program_generator import BaseProgramGenerator, CsmithProgramGenerator, OpenAiProgramGenerator
from src.api_output_comparator import ApiOutputComparator

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
    
    ## Insert other methods of TestEngine here
    def test_add_comment_relation(self):
        # Prepares the program modifier
        add_comment_program_modifier = AddCommentProgramModifier()




        # Generate a random base program
        # base_program_string = self.openai_base_program_generator.generate_test_case('py', '')
        base_program_string = "def list_sum(lst):\\n\\tsum = 0\\n\\tfor num in lst:\\n\\t\\tsum += num\\n\\treturn sum"

        print(base_program_string)
        
        # Modify the base program
        modified_program_string = add_comment_program_modifier.modify_program('py', base_program_string)

        print(modified_program_string)

        # Uncomment this to try the openai base program generator
        # print(self.openai_base_program_generator.generate_test_case('py', '1 while loop'))


        
if __name__ == "__main__":
    # Main driver method that creates an instance of TestEngine
    # and runs it to execute the test cases
    test_engine = TestEngine()

    test_engine.test_add_comment_relation()
