'''
    Responsible for writing of test case results to a file
'''
from .metamorphic_relation_enum import MetamorphicRelationEnum

class MetamorphicResultWriter():
    """
    This class handles the writing of the results of testing against the metamorprhic relations
    
    """

    PATH_OF_RESULT_FILES = {
        MetamorphicRelationEnum.ADD_COMMENT: "././results/add_comment.txt",
        MetamorphicRelationEnum.ADDITION_ASSIGNMENT: "././results/addition_assignment.txt"
    }



    def __init__(self):
        """
        Initialisation method for a MetamorphicResultWriter
        """

    def write_results_to_file(self, metamorphic_relation_enum, base_program_string,
                                modified_program_string, error_localizer_api_output,
                                feedback_fix_api_output, feedback_error_api_output,
                                repair_api_output, status):
        """
        This method is responsible for writing the test case result to a file in a
        specified format.

        Parameters:
            metamorphic_relation_enum: Which relation we are testing for
            base_program_string: Base program
            modified_program_string: Modified program
            error_localizer_api_output: Output from error localizer API
            feedback_fix_api_output: Output from feedback fix API
            feedback_error_api_output: Output from feedback error API
            repair_api_output: Output from repair API
            status: Whether test case pass or not
        """

        with open(self.PATH_OF_RESULT_FILES[metamorphic_relation_enum], "a",
          encoding="utf-8") as file:

            # Append base program
            file.write("Base Program:\n")
            file.write(base_program_string)
            file.write("\n\n")

            # Apend modified program
            file.write("Modified Program:\n")
            file.write(modified_program_string)
            file.write("\n\n")

            # Append error localizer api output
            file.write("Error Localizer API Output:\n")
            file.write(error_localizer_api_output)
            file.write("\n\n")

            # Append feedback fix api output
            file.write("Feedback Fix API Output:\n")
            file.write(feedback_fix_api_output)
            file.write("\n\n")

            # Append feedback error api output
            file.write("Feedback Error API Output:\n")
            file.write(feedback_error_api_output)
            file.write("\n\n")

            # Append feedback error api output
            file.write("Repair API Output:\n")
            file.write(repair_api_output)
            file.write("\n\n")

            # Append status
            file.write("Status:\n")
            file.write(status)
            file.write("\n\n\n########\n\n\n")
