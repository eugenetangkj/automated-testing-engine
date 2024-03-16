from src.metamorphic_relation_tester import AddCommentRelationTester, AdditionAssignmentRelationTester
from src.metamorphic_program_modifier import AdditionAssignmentProgramModifier

class TestEngine(object):
    """
    This class is the test engine responsible for running test cases against metamorphic relations.
    It acts as the main point of entry for the app.
    
    Attributes:
        PATH_OF_ERROR_FILE (str): Path of file that contains the errors detected

    """

    def __init__(self):
        """
        Initialisation method for a TestEngine instance
        """
        
   
        
if __name__ == "__main__":
    # Main driver method that creates an instance of TestEngine
    # and runs it to execute the test cases for the relations
    test_engine = TestEngine()

    
    # print("Testing add comment relation...")
    # AddCommentRelationTester(5).test_relation() # Generates 5 test cases for now
    # print("Testing add comment relation completed.\n")

    print("Testing addition assignment relation...")
    AdditionAssignmentRelationTester(3).test_relation() # Generates 5 test cases for now
    print("Testing addition assignment relation completed.\n")

    # test_string = "int increment_by_value(int n) { int value = 2; n += value; return n; }"
    # print(test_string)
    # print("\n###\n")
    # print(AdditionAssignmentProgramModifier().modify_program("c", test_string))


    

