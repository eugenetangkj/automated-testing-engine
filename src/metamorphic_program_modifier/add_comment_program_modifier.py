
from .metamorphic_program_modifier import MetamorphicProgramModifier;

class AddCommentProgramModifier(MetamorphicProgramModifier):
    """
    This class modifies a base program based on the add comment metamorphic relation, which states that
    adding comments to a program should not affect its semantics.

    """


    def __init__(self):
        """
        Initialisation method for a AddCommentProgramModifier instance
        """
        pass
    
    ## Insert other methods of AddCommentProgramModifier here
    def add_comment(self, original_program, comment):
        modified_program = original_program + "\n# " + comment
        return modified_program
    
    def modify_program(self, language, original_program):
        """
        Modifies the base program by adding comments to it.
        
        Args:
            language (str): The programming language of the program.
            original_program (str): The original program.
            
        Returns:
            str: The modified program with comments
        """
        if language not in ["Python", "Java", "C"]:
            raise ValueError("Unsupported programming language: {}".format(language))
        modified_program = self.add_comment(original_program, "This is a comment added by the AddCommentProgramModifier.")
        return modified_program
