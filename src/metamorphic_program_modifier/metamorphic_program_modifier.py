
class MetamorphicProgramModifier(object):
    """
    This is an abstract class from which concrete program modifier classes would extend from. There are different
    metamorphic relations that we would test, and each of these relations mandates a different way of modifying base
    programs in order to test those relations.

    Attributes:
        BASE_API_URL (str): The base URL to connect to the ITS API
    """

    BASE_API_URL = "https://its.comp.nus.edu.sg/cs3213/"
    
    
    def __init__(self):
        """
        Initialisation method for a MetamorphicProgramModifier instance
        """
        pass
    
    ## Insert other methods of MetamorphicProgramModifier here

