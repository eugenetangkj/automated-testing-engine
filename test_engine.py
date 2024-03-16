from src.metamorphic_relation_tester import AddCommentRelationTester
import logging

class TestEngine(object):
    """
    This class is the test engine responsible for running test cases against metamorphic relations.
    It acts as the main point of entry for the app.
    
    Attributes:
        PATH_OF_ERROR_FILE (str): Path of file that contains the errors detected

    """

    PATH_OF_RESULT_FILES = {
        "add_comment_relation": "results/add_comment.txt"
    }

    def __init__(self):
        """
        Initialisation method for a TestEngine instance
        """
        
   
        
if __name__ == "__main__":
    # Main driver method that creates an instance of TestEngine
    # and runs it to execute the test cases for the relations
    test_engine = TestEngine()

    
    print("Testing add comment relation...")
    AddCommentRelationTester(1).test_relation()
    print("Testing add comment relation completed.")

