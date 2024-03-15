
from .metamorphic_program_modifier import MetamorphicProgramModifier;

class AddCommentProgramModifier(MetamorphicProgramModifier):
    """
    This class modifies a base program based on the add comment metamorphic relation, which states that
    adding comments to a program should not affect its semantics.

    """
    DEFAULT_COMMENT = "This is the default comment added by the AddCommentProgramModifier."

    def __init__(self):
        """
        Initialisation method for a AddCommentProgramModifier instance
        """
        pass
    
    ## Insert other methods of AddCommentProgramModifier here
    def add_comment(self, original_program, comment):
        lines = original_program.split('\n') # Split the program into lines
        commented_lines = [f"{line.rstrip()} {comment}" for line in lines] # add a comment to each line
        modified_program = '\n'.join(commented_lines)
        return modified_program
    
    def modify_program(self, language, original_program):
        """
        Modifies the base program by adding a comment to the end of each line.
        
        Args:
            language (str): The programming language of the program.
            original_program (str): The original program.
            
        Returns:
            str: The modified program with comments
        """
        if language not in ["py", "c"]:
            raise ValueError("Unsupported programming language: {}".format(language))
        modified_program = self.add_comment(original_program, self.DEFAULT_COMMENT)
        return modified_program
