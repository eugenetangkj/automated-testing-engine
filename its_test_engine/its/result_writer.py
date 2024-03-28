'''
    Responsible for writing of test case results to a file
'''
from .test_result import TestResult

class ResultWriter():
    """
    This class handles the writing of the results of testing against the metamorprhic relations
    
    """

    PATH_OF_RESULT_FILE = "././results/results.txt"



    def __init__(self):
        """
        Initialisation method for a result writer instance
        """

    def write_results_to_file(self, test_result: TestResult):
        """
        This method is responsible for writing the test case result to a file in a
        specified format.

        Parameters:
            test_result: The test result object containing information about the test result
        """

        with open(self.PATH_OF_RESULT_FILE, "a", encoding="utf-8") as file:

            # Append base program
            file.write("Base Program:\n")
            file.write(test_result.base_program_string)
            file.write("\n\n")

            # Append modified program
            file.write("Modified Program:\n")
            file.write(test_result.modified_program_string)
            file.write("\n\n")

            # Append inputs, if any
            if test_result.inputs is not None:
                file.write("Inputs:\n")
                file.write(test_result.inputs)
                file.write("\n\n")

            # Append status
            file.write("Status:\n")
            file.write(test_result.status)
            file.write("\n\n")

            if test_result.problematic_output is not None:
                # Append problematic output, if any
                file.write("Problematic Output:\n")
                file.write(test_result.problematic_output)
                file.write("\n\n")

            if test_result.exception_message is not None:
                # Append exceptions, if any
                file.write("Exceptions:\n")
                file.write(test_result.status)

            # Append delimiter between test cases
            file.write("\n\n\n########\n\n\n")
