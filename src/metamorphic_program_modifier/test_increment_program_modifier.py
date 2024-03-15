from .metamorphic_program_modifier import MetamorphicProgramModifier;

class TestIncrementProgramModifier(MetamorphicProgramModifier):
    """
    This class modifies a base program based on the addition symbol metamorphic relation, which states that
    translating i += x to i = i + x in a program should not affect its semantics.

    """

    def __init__(self):
        """
        Initialisation method for a TestIncrementProgramModifier instance
        """
        pass
    
    def test_increment(self, original_program, comment):
      modified_program = str(original_program).replace(" += ", " = i + ")
      return modified_program
    
    def modify_program(self, language, original_program):
        """
        Modifies the base program by replacing all instances of i += x with i = i + x.
        
        Args:
            language (str): The programming language of the program.
            original_program (str): The original program.
            
        Returns:
            str: The modified program with comments
        """
        if language not in ["py", "c"]:
            raise ValueError("Unsupported programming language: {}".format(language))
        modified_program = self.test_increment(original_program)
        return modified_program
