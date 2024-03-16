from .metamorphic_relation_tester import MetamorphicRelationTester
from ..metamorphic_program_modifier import AddCommentProgramModifier
from ..its_api_connection import ItsApiConnection
from ..inter_representation_processer import InterRepresentationProcesser
from ..helpers.type_of_metamorphic_relation import TypeOfMetamorphicRelation
from ..helpers.metamorphic_relation_enum import MetamorphicRelationEnum
from ..helpers.metamorphic_result_writer import MetamorphicResultWriter
from ..api_output_comparator import ApiOutputComparator
import json

class AddCommentRelationTester(MetamorphicRelationTester):
    """
    This class breaks down the intermediate representation of a program obtained from the parser API into smaller
    parts that are needed to be put into the other ITS API calls.
    
    """

    METAMORPHIC_RELATION_ENUM = MetamorphicRelationEnum.ADD_COMMENT
    TYPE_OF_RELATION = TypeOfMetamorphicRelation.EQUIVALENT


    def __init__(self, number_of_test_cases):
        """
        Initialisation method for a BaseProgramGenerator instance

        Parameters:
            number_of_test_cases: Number of test cases to generate for testing this relation
        """
        super().__init__(number_of_test_cases)
        self.add_comment_program_modifier = AddCommentProgramModifier()
        self.its_api_connection = ItsApiConnection()
        self.inter_representation_processer = InterRepresentationProcesser()
        self.api_output_comparator = ApiOutputComparator()
        self.metamorphic_result_writer = MetamorphicResultWriter()
        

    
    def test_relation(self):
        """
            Test the relation with c and py programs

        """
        # Get number of test cases for each language
        number_of_c_test_cases = self.get_number_of_c_test_cases()
        number_of_py_test_cases = self.get_number_of_py_test_cases()


        # Process cases for each language
        self.test_relation_c(number_of_c_test_cases)
        self.test_relation_py(number_of_py_test_cases)


    def test_relation_c(self, number_of_test_cases):
        """
            Test the relation with c 

        """
        # Part A: Handle c programs
        for i in range(number_of_test_cases):

            # Step 1a: Generate a random base program
            # base_program_string = self.openai_base_program_generator.generate_test_case('py', '')
            base_program_string = "int factorial(int n) {\n\tint result = 1;\n\twhile (n > 1) {\n\t\tresult *= n;\n\t\tn--;\n\t}\n\treturn result;\n}"
       
    
            # Step 2a: Modify the base program
            modified_program_string = self.add_comment_program_modifier.modify_program("c", base_program_string)

        
            # Step 3a: Put the base and modified programs into parser endpoint to get intermediate representation
            base_program_intermediate_representation_dict = self.its_api_connection.call_parser_endpoint("c", base_program_string)
            modified_program_intermediate_representation_dict = self.its_api_connection.call_parser_endpoint("c", modified_program_string)
        

            # Step 4a: Extract information from intermediate representation
            program_information = self.inter_representation_processer.break_down_inter_representation_c(base_program_intermediate_representation_dict)


            # Step 5a: Write to error localizer API
            output_error_localizer = self.its_api_connection.call_errorlocalizer_endpoint(
                "c",
                json.dumps(base_program_intermediate_representation_dict, indent=4),
                json.dumps(modified_program_intermediate_representation_dict, indent=4),
                program_information["function"],
                program_information["inputs"],
                program_information["args"]
            )

        
            # Step 6a: Write to feedback fix API
            output_feedback_fix = self.its_api_connection.call_feedback_fix_endpoint(
                "c",
                json.dumps(base_program_intermediate_representation_dict, indent=4),
                json.dumps(modified_program_intermediate_representation_dict, indent=4),
                program_information["function"],
                program_information["inputs"],
                program_information["args"]
            )

            # Step 7a: Write to feedback error API
            output_feedback_error = self.its_api_connection.call_feedback_error_endpoint(
                "c",
                json.dumps(base_program_intermediate_representation_dict, indent=4),
                json.dumps(modified_program_intermediate_representation_dict, indent=4),
                program_information["function"],
                program_information["inputs"],
                program_information["args"]
            )

            # Step 8a: Write to repair API
            output_repair = self.its_api_connection.call_feedback_error_endpoint(
                "c",
                json.dumps(base_program_intermediate_representation_dict, indent=4),
                json.dumps(modified_program_intermediate_representation_dict, indent=4),
                program_information["function"],
                program_information["inputs"],
                program_information["args"]
            )

            # Step 9a: Determine status of test case
            did_error_localizer_pass = self.api_output_comparator.check_error_localizer_output(output_error_localizer, self.TYPE_OF_RELATION)
            did_feedback_fix_pass = self.api_output_comparator.check_feedback_fix_output(output_feedback_fix, self.TYPE_OF_RELATION)
            did_feedback_error_pass = self.api_output_comparator.check_feedback_error_output(output_feedback_error, self.TYPE_OF_RELATION)
            did_repair_pass = self.api_output_comparator.check_repair_output(output_repair, self.TYPE_OF_RELATION)
            status = "PASS" if did_error_localizer_pass and did_feedback_fix_pass and did_feedback_error_pass and did_repair_pass else "FAIL"
                                                                             

            # Step 9a: Write to file
            self.metamorphic_result_writer.write_results_to_file(
                self.METAMORPHIC_RELATION_ENUM,
                base_program_string,
                modified_program_string,
                json.dumps(output_error_localizer, indent=4),
                json.dumps(output_feedback_fix, indent=4),
                json.dumps(output_feedback_error, indent=4),
                json.dumps(output_repair, indent=4),
                status
            )


    def test_relation_py(self, number_of_test_cases):
        """
            Test the relation with py

        """
        # Part B: Handle py programs
        for i in range(number_of_test_cases):
            pass

            

       
    
