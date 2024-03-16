'''
    Adds comments to each line in the program
'''
from .metamorphic_program_modifier import MetamorphicProgramModifier

class AddCommentProgramModifier(MetamorphicProgramModifier):
    """
    This class modifies a base program based on the add comment metamorphic relation,
    which states that adding comments to a program should not affect its semantics.

    """
    DEFAULT_COMMENT_C = "\n//Default comment"
    DEFAULT_COMMENT_PY = "\n#Default Comment"

    def __init__(self):
        """
        Initialisation method for a AddCommentProgramModifier instance
        """

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
            raise ValueError(f"Unsupported programming language: {language}")

        comment_to_add = self.DEFAULT_COMMENT_C if (language == "c") else self.DEFAULT_COMMENT_PY
        modified_program = self.__add_comment(original_program, comment_to_add)

        return modified_program



    def __add_comment(self, original_program, comment):
        # Split the program into lines
        lines = original_program.split('\n')
        # Add a comment to each line
        commented_lines = [f"{line.rstrip()}{comment}" for line in lines]
        modified_program = '\n'.join(commented_lines)
        return modified_program
