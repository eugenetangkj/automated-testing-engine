'''
    Unravels the += addition assignment operator
'''

from .metamorphic_program_modifier import MetamorphicProgramModifier

class AdditionAssignmentProgramModifier(MetamorphicProgramModifier):
    """
    This class modifies a base program based on the addition symbol metamorphic relation, which states that
    translating i += x to i = i + x in a program should not affect its semantics.

    """

    def __init__(self):
        """
        Initialisation method for a TestIncrementProgramModifier instance
        """

    def convert_addition_assignment(self, original_program):
        lines = original_program.split('\n')
        modified_lines = []
        for line in lines:  # find all instances in program
            if '+=' in line:
                var_name = line.split('+=')[0].strip().split()[-1]
                before_var = self.find_substring_before_target(line.split('+=')[0], var_name)
                increment_val = line.split('+=')[1].strip() # remove additional spaces

                modified_lines.append(f"{before_var}{var_name} = {var_name.strip()} + {increment_val}")
            else:
                modified_lines.append(line)
        return '\n'.join(modified_lines)
    
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
        modified_program = self.convert_addition_assignment(original_program)
        return modified_program
    

    # Obtained from ChatGPT
    def find_substring_before_target(self, s, target):
        index_of_target = s.rfind(target)  # Find the last occurrence of the target string
        if index_of_target != -1:
            return s[:index_of_target]  # Return substring before the target string
        return s  # Return the original string if the target is not found