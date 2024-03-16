from ..helpers.type_of_metamorphic_relation import TypeOfMetamorphicRelation

class ApiOutputComparator(object):
    """
    This class is responsible for comparing and analysing the outputs obtained from the API.
    This allows us to determine if there is any discrepancy or potential bugs obtained from our
    metamorphic relations.
    
    """

    def __init__(self):
        """
        Initialisation method for an ApiOutputComparator instance
        """
        pass
    
    
    def check_error_localizer_output(self, error_localizer_output, type_of_metamorphic_relation):
        """
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false

        Parameters:
            feedback_fix_output: Dictionary that is obtained from the error localizer API
            type_of_metamorphic_relation: The type of relation we are testing for, whether equivalent or variant

        """
        # We are testing that the base and modified programs should be equivalent
        if (type_of_metamorphic_relation == TypeOfMetamorphicRelation.EQUIVALENT):
            return True if (error_localizer_output["errorLocations"] == {}) else False

        # We are testing that the base and modified programs should be different
        else:
            return True if (len(error_localizer_output) != {}) else False


    def check_feedback_fix_output(self, feedback_fix_output, type_of_metamorphic_relation):
        """
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false

        Parameters:
            feedback_fix_output: Dictionary that is obtained from the feedback fix API
            type_of_metamorphic_relation: The type of relation we are testing for, whether equivalent or variant

        """
        
        return self.__check_feedback_output__(feedback_fix_output, type_of_metamorphic_relation)
        

    
    def check_feedback_fix_output(self, feedback_fix_output, type_of_metamorphic_relation):
        """
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false

        Parameters:
            feedback_fix_output: Dictionary that is obtained from the feedback fix API
            type_of_metamorphic_relation: The type of relation we are testing for, whether equivalent or variant

        """
        return self.__check_feedback_output__(feedback_fix_output, type_of_metamorphic_relation)

    
    def check_feedback_error_output(self, feedback_error_output, type_of_metamorphic_relation):
        """
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false

        Parameters:
            feedback_fix_output: Dictionary that is obtained from the feedback error API
            type_of_metamorphic_relation: The type of relation we are testing for, whether equivalent or variant

        """
        return self.__check_feedback_output__(feedback_error_output, type_of_metamorphic_relation)

    
    def check_repair_output(self, repair_output, type_of_metamorphic_relation):
        """
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false

        Parameters:
            feedback_fix_output: Dictionary that is obtained from the repair API
            type_of_metamorphic_relation: The type of relation we are testing for, whether equivalent or variant

        """
        return self.__check_feedback_output__(repair_output, type_of_metamorphic_relation)
        

    def __check_feedback_output__(self, output, type_of_metamorphic_relation):
        """
        Success or failure is depending on the type of metamorphic relation that we
        are testing. If successful, return true. Else, return false

        Parameters:
            output: Dictionary that is obtained from the feedback fix, feedback error, or repair API
            type_of_metamorphic_relation: The type of relation we are testing for, whether equivalent or variant

        """
        # We are testing that the base and modified programs should be equivalent
        if (type_of_metamorphic_relation == TypeOfMetamorphicRelation.EQUIVALENT):
            return True if (len(output) == 0) else False

        # We are testing that the base and modified programs should be different
        else:
            return True if (len(output) != 0) else False



