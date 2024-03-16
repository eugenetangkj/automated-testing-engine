from helpers.type_of_metamorphic_relation import TypeOfMetamorphicRelation

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
    
    

    def check_feedback_fix_output(self, feedback_fix_output, type_of_metamorphic_relation):
        """
        Returns success or failure depending on the type of metamorphic relation that we
        are testing

        Parameters:
            feedback_fix_output: Dictionary that is obtained from the feedback fix API
            type_of_metamorphic_relation: The type of relation we are testing for, whether equivalent or variant

        """
        
        # We are testing that the base and modified programs should be equivalent
        if (type_of_metamorphic_relation == TypeOfMetamorphicRelation.EQUIVALENT):
            return "PASS" if (len(feedback_fix_output) == 0) else "FAIL"

        # We are testing that the base and modified programs should be different
        else:
            return "PASS" if (len(feedback_fix_output) != 0) else "FAIL"



