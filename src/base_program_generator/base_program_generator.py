class BaseProgramGenerator(object):
    """
    This is an abstract class from which concrete program generator classes would extend from. Subclasses that extend
    this class are responsible for generating a list of random programs (either in C or Python). These random programs
    generated are the base programs, as later on, they will be modified upon to test the metamorphic relations.
    
    """

    def __init__(self):
        """
        Initialisation method for a BaseProgramGenerator instance
        """
        pass
    
    ## Insert other methods of BaseProgramGenerator here
