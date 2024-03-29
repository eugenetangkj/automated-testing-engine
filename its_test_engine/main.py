"""
    Entry point of application
"""
from its_test_engine.python.program_generator import LeetCodePythonProgramGenerator
from its_test_engine.base.program_generator import OpenAiProgramGenerator
from its_test_engine.python.modifier import VariableRenamer, BinOpModifier
from its_test_engine.base.input_generator.random_input_generator import (
    RandomInputGenerator,
)
from its_test_engine.utils import mutate_code
from its_test_engine.its.api_tester import ApiTester
from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.api_output_comparator import ApiOutputComparator
from its_test_engine.enums.type_of_metamorphic_relation import TypeOfMetamorphicRelation
from its_test_engine.its.result_writer import ResultWriter
from its_test_engine.its.error_localizer_endpoint_tester import ErrorLocalizerEndpointTester
from its_test_engine.its.feedback_fix_endpoint_tester import FeedbackFixEndpointTester
from its_test_engine.its.feedback_error_endpoint_tester import FeedbackErrorEndpointTester
from its_test_engine.its.repair_endpoint_tester import RepairEndpointTester


def run_python():
    # Transformers
    transformers = [VariableRenamer(), BinOpModifier()]
    # API tester
    # Prepare API tester
    api_tester = ApiTester(
        its_api_connection=ItsApiConnection(),
        input_generator=RandomInputGenerator(),
        error_localizer_endpoint_tester=ErrorLocalizerEndpointTester(ApiOutputComparator(), ItsApiConnection(), TypeOfMetamorphicRelation.EQUIVALENT),
        feedback_fix_endpoint_tester=FeedbackFixEndpointTester(ApiOutputComparator(), ItsApiConnection(), TypeOfMetamorphicRelation.EQUIVALENT),
        feedback_error_endpoint_tester=FeedbackErrorEndpointTester(ApiOutputComparator(), ItsApiConnection(), TypeOfMetamorphicRelation.EQUIVALENT),
        repair_endpoint_tester=RepairEndpointTester(ApiOutputComparator(), ItsApiConnection(), TypeOfMetamorphicRelation.EQUIVALENT)
    )


    # OpenAI program generator
    try:
        # Mutate code
        open_ai_program_generator = OpenAiProgramGenerator("py", "None")
        code, function_signature = open_ai_program_generator.generate_test_case()
        modified_code = mutate_code(code, transformers)
        # Test each modified code, one at a time with base program
        for index, modified_program in enumerate(modified_code):
            # Obtain test result
            test_result = api_tester.test_program(
                base_program_string=code,
                modified_program_string=modified_program,
                function_signature=function_signature,
                language="py"
            )

            # Save test result to file
            ResultWriter().write_results_to_file(test_result)
            print("Test case completed")

    except Exception as e :
        # Got exception, so ignore test case
        print("Test case ignored: " + str(e))


    # Python leetcode program generator
    try:
        # Mutate code
        function_signature = None
        while function_signature is None:
            program_generator = LeetCodePythonProgramGenerator()
            function_signature, code = program_generator.generate_test_case()
        modified_code = mutate_code(code, transformers)
        # Test each modified code, one at a time with base program
        for index, modified_program in enumerate(modified_code):
            # Obtain test result
            test_result = api_tester.test_program(
                base_program_string=code,
                modified_program_string=modified_program,
                function_signature=function_signature,
                language="py"
            )

            # Save test result to file
            ResultWriter().write_results_to_file(test_result)
            print("Test case completed")

    except Exception as e :
        # Got exception, so ignore test case
        print("Test case ignored: " + str(e))



if __name__ == "__main__":
    run_python()
