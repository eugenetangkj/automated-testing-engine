"""
This module is the entry point to the test engine
"""

from src.metamorphic_relation_tester import AddCommentRelationTester
from src.metamorphic_relation_tester import AdditionAssignmentRelationTester

class TestEngine():
    """
    This class is the test engine responsible for running test cases against metamorphic relations.
    It acts as the main point of entry for the app.
    
    """

    def __init__(self):
        """
        Initialisation method for a TestEngine instance
        """

    def test_add_comment_relation(self):
        """
        Tests the add comment relation
        """
        print("Testing add comment relation...")
        AddCommentRelationTester(5).test_relation() # Generates 5 test cases for now
        print("Testing add comment relation completed.\n")

    def test_addition_assignment_relation(self):
        """
        Tests the addition assignment relation
        """
        print("Testing addition assignment relation...")
        AdditionAssignmentRelationTester(5).test_relation() # Generates 5 test cases for now
        print("Testing addition assignment relation completed.\n")



if __name__ == "__main__":
    # Main driver method that creates an instance of TestEngine
    # and runs it to execute the test cases for the relations
    test_engine = TestEngine()

    # Test relations
    test_engine.test_add_comment_relation()
    test_engine.test_addition_assignment_relation()
