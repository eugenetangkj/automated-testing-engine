from .metamorphic_relation_enum import MetamorphicRelationEnum

class MetamorphicResultWriter(object):
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
        pass


    def write_results_to_file(self, metamorphic_relation_enum, base_program_string,
                                modified_program_string, error_localizer_api_output,
                                feedback_fix_api_output, feedback_error_api_output,
                                repair_api_output, status):
        
        with open(self.PATH_OF_RESULT_FILES[metamorphic_relation_enum], "a") as file:
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