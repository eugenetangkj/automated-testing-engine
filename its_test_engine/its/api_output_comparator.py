"""
    Compare API output
"""
from ..enums.type_of_metamorphic_relation import TypeOfMetamorphicRelation

class ApiOutputComparator():
    """
    This class is responsible for comparing and analysing the outputs obtained from the API.
    This allows us to determine if there is any discrepancy or potential bugs obtained from our
    metamorphic relations.
    """
    def __init__(self):
        """
        Initialisation method for an ApiOutputComparator instance
        """

    def check_error_localizer_output(self, error_localizer_output, type_of_metamorphic_relation):
        """
        Checks if error localiser is a pass for the test case or not.
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false.

        Parameters:
            error_localizer_output: Dictionary that is obtained from the error localizer API
            type_of_metamorphic_relation: The type of relation we are testing for, whether
                                          equivalent or variant

        """
        # We are testing that the base and modified programs should be equivalent
        if type_of_metamorphic_relation == TypeOfMetamorphicRelation.EQUIVALENT:
            return error_localizer_output["errorLocations"] == {}

        # We are testing that the base and modified programs should be different
        return len(error_localizer_output) != {}


    def check_feedback_fix_output(self, feedback_fix_output, type_of_metamorphic_relation):
        """
        Checks if feedback fix is a pass for the test case or not.
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false.

        Parameters:
            feedback_fix_output: Dictionary that is obtained from the feedback fix API
            type_of_metamorphic_relation: The type of relation we are testing for, whether
                                          equivalent or variant
        """
        return self.__check_feedback_output(feedback_fix_output, type_of_metamorphic_relation)


    def check_feedback_error_output(self, feedback_error_output, type_of_metamorphic_relation):
        """
        Checks if feedback error is a pass for the test case or not.
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false

        Parameters:
            feedback_error_output: Dictionary that is obtained from the feedback error API
            type_of_metamorphic_relation: The type of relation we are testing for, whether
                                          equivalent or variant

        """
        return self.__check_feedback_output(feedback_error_output, type_of_metamorphic_relation)



    def check_repair_output(self, repair_output, type_of_metamorphic_relation):
        """
        Checks if repair is a pass for the test case or not.
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false

        Parameters:
            repair_output: Dictionary that is obtained from the repair API
            type_of_metamorphic_relation: The type of relation we are testing for, whether
                                          equivalent or variant

        """
        return self.__check_feedback_output(repair_output, type_of_metamorphic_relation)


    def __check_feedback_output(self, output, type_of_metamorphic_relation):
        """
        Helper method to check for feedback fix, feedback error and repair outputs

        Parameters:
            output: Dictionary that is obtained from the feedback fix, feedback error, or repair API
            type_of_metamorphic_relation: The type of relation we are testing for, whether
                                          equivalent or variant
        """
        # We are testing that the base and modified programs should be equivalent
        if type_of_metamorphic_relation == TypeOfMetamorphicRelation.EQUIVALENT:
            return len(output) == 0

        # We are testing that the base and modified programs should be different
        return len(output) != 0