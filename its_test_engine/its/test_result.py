'''
    This class represents a test result object obtained from the tester class
'''


class TestResult(object):
    """
    This class is encapsulates the data of a test result object obtained from the tester class

    """


    def __init__(self, status, base_program_string, modified_program_string, inputs=None,
                problematic_output=None, exception_message=None,):
        """
        Initialises a test result instance

        Parameters:
            status: 'PASS' or 'FAIL', representing success status of a test case
            base_program_string: Base program string used for the test case
            modified_program_string: Modified program string used for the test case
            inputs: Inputs given for the base and modified programs

            problematic_output: Ouput from ITS API that indicates a potential bug
            exception_message: Any exceptions that occurred during the testing of the test case
        """
        self.status = status
        self.base_program_string = base_program_string
        self.modified_program_string = modified_program_string
        self.inputs = inputs
        self.problematic_output = problematic_output
        self.exception_message = exception_message
