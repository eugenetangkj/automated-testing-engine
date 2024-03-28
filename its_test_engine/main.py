"""
    Entry point of application
"""
from its_test_engine.python.program_generator import LeetCodeProgramGenerator
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


def run_python():
    transformers = [VariableRenamer(), BinOpModifier()]
    api_tester = ApiTester(ItsApiConnection(), RandomInputGenerator(), ApiOutputComparator())

    # TODO: Handle try-catch block because mutation might not work
    open_ai_program_generator = OpenAiProgramGenerator("py", "None")
    code, function_signature = open_ai_program_generator.generate_test_case()
    modified_code = mutate_code(code, transformers)


    # program_generator = LeetCodeProgramGenerator("python")
    # function_signature, code = program_generator.generate_test_case()
    # mutated_codes = mutate_code(code, transformers)

    for index, modified_program in enumerate(modified_code):
        api_tester.test_program(
            base_program_string=code,
            modified_program_string=modified_program,
            function_signature=function_signature,
            type_of_metamorphic_relation= TypeOfMetamorphicRelation.EQUIVALENT,
            language="py"
        )

if __name__ == "__main__":
    run_python()
