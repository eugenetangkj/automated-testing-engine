from .metamorphic_relation_tester import MetamorphicRelationTester
from ..metamorphic_program_modifier import AddCommentProgramModifier
from ..its_api_connection import ItsApiConnection
from ..inter_representation_processer import InterRepresentationProcesser
from ..helpers.type_of_metamorphic_relation import TypeOfMetamorphicRelation
from ..helpers.metamorphic_relation_enum import MetamorphicRelationEnum
from ..helpers.metamorphic_result_writer import MetamorphicResultWriter
from ..api_output_comparator import ApiOutputComparator
from ..base_program_generator import OpenAiProgramGenerator
import json
import random

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
        self.openai_base_program_generator = OpenAiProgramGenerator()
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
        self.__test_relation_c(number_of_c_test_cases)
        self.__test_relation_py(number_of_py_test_cases)



    def __test_relation_c(self, number_of_test_cases):
        """
            Test the relation with c 

        """
        # Part A: Handle c programs
        for i in range(number_of_test_cases):

            try:

                # Step 1a: Generate a random base program
                base_program_string = self.openai_base_program_generator.generate_test_case('c', '')["program"]
                self.__process_relation_c(base_program_string)


                print("Test case " + str(i) + " done.")
            
            except:
                # Step 1a: Randomly pick a c program
                with open('././datafiles/random_c_programs.json', 'r') as file:
                    data = json.load(file)
                    base_program_string = random.choice(data)
                self.__process_relation_c(base_program_string)

                print("Test case " + str(i) + " done. (Random pool)")



    def __test_relation_py(self, number_of_test_cases):
        """
            Test the relation with py

            Parameters:
                number_of_test_cases: Number of test cases to test this relation with

        """
        # Part B: Handle py programs
        for i in range(number_of_test_cases):

            try:
                # Step 1b: Generate a random base program
                base_program = self.openai_base_program_generator.generate_test_case('py', '')
                base_program_string = base_program["program"]
                base_program_data_type = base_program["data_type"]
                self.__process_relation_py(base_program_string, base_program_data_type)
                
                print("Test case " + str(i + self.number_of_test_cases - number_of_test_cases) + " done.")
            
            except:
                # Step 1b: Randomly pick from a safe pool of Python programs
                with open('././datafiles/random_py_programs.json') as file:
                    random_py_programs = json.load(file)
                
                random_index = random.randrange(len(random_py_programs))

                with open('././datafiles/random_py_datatypes.json') as file:
                    random_data_types = json.load(file)

                base_program_string = random_py_programs[random_index]
                base_program_data_type = random_data_types[random_index]

                self.__process_relation_py(base_program_string, base_program_data_type)


                print("Test case " + str(i + self.number_of_test_cases - number_of_test_cases) + " done. (Random pool)")



    def __process_relation_c(self, base_program_string):
        '''
        Helper function for processing relation for c programs

        '''
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
                                                                        

        # Step 10a: Write to file
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


    def __process_relation_py(self, base_program_string, base_program_data_type):
        '''
        Helper function for processing relation for py programs

        '''
         # Step 2b: Modify the base program
        modified_program_string = self.add_comment_program_modifier.modify_program("py", base_program_string)

        
        # Step 3b: Put the base and modified programs into parser endpoint to get intermediate representation
        base_program_intermediate_representation_dict = self.its_api_connection.call_parser_endpoint("py", base_program_string)
        modified_program_intermediate_representation_dict = self.its_api_connection.call_parser_endpoint("py", modified_program_string)


        # Step 4b: Extract information from intermediate representation
        program_information = self.inter_representation_processer.break_down_inter_representation_py(base_program_intermediate_representation_dict, base_program_data_type)


        # Step 5b: Write to error localizer API
        output_error_localizer = self.its_api_connection.call_errorlocalizer_endpoint(
            "py",
            json.dumps(base_program_intermediate_representation_dict, indent=4),
            json.dumps(modified_program_intermediate_representation_dict, indent=4),
            program_information["function"],
            program_information["inputs"],
            program_information["args"]
        )

        # Step 6b: Write to feedback fix API
        output_feedback_fix = self.its_api_connection.call_feedback_fix_endpoint(
            "py",
            json.dumps(base_program_intermediate_representation_dict, indent=4),
            json.dumps(modified_program_intermediate_representation_dict, indent=4),
            program_information["function"],
            program_information["inputs"],
            program_information["args"]
        )

        # Step 7b: Write to feedback error API
        output_feedback_error = self.its_api_connection.call_feedback_error_endpoint(
            "py",
            json.dumps(base_program_intermediate_representation_dict, indent=4),
            json.dumps(modified_program_intermediate_representation_dict, indent=4),
            program_information["function"],
            program_information["inputs"],
            program_information["args"]
        )

        # Step 8b: Write to repair API
        output_repair = self.its_api_connection.call_feedback_error_endpoint(
            "py",
            json.dumps(base_program_intermediate_representation_dict, indent=4),
            json.dumps(modified_program_intermediate_representation_dict, indent=4),
            program_information["function"],
            program_information["inputs"],
            program_information["args"]
        )

        # Step 9b: Determine status of test case
        did_error_localizer_pass = self.api_output_comparator.check_error_localizer_output(output_error_localizer, self.TYPE_OF_RELATION)
        did_feedback_fix_pass = self.api_output_comparator.check_feedback_fix_output(output_feedback_fix, self.TYPE_OF_RELATION)
        did_feedback_error_pass = self.api_output_comparator.check_feedback_error_output(output_feedback_error, self.TYPE_OF_RELATION)
        did_repair_pass = self.api_output_comparator.check_repair_output(output_repair, self.TYPE_OF_RELATION)
        status = "PASS" if did_error_localizer_pass and did_feedback_fix_pass and did_feedback_error_pass and did_repair_pass else "FAIL"
                                                                        

        # Step 10b: Write to file
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

        
        

            

       
    
