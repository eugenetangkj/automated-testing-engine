
from its_test_engine.python.program_generator import LeetCodeProgramGenerator
from its_test_engine.base.program_generator import OpenAiProgramGenerator
from its_test_engine.python.modifier import VariableRenamer, BinOpModifier
from its_test_engine.base.input_generator.random_input_generator import (
    RandomInputGenerator,
)
from its_test_engine.utils import mutate_code


def run_python():
    open_ai_program_generator = OpenAiProgramGenerator()
    open_ai_program_generator.print_sample()

    program_generator = LeetCodeProgramGenerator("python")
    random_input_generator = RandomInputGenerator()
    transformers = [VariableRenamer(), BinOpModifier()]

    # Step 1: Generate the test case
    function_signature, code = program_generator.generate_test_case()
    #print(function_signature)

    # Step 2: Generate the inputs
    inputs = random_input_generator.generate_inputs(function_signature["arguments"], 10)

    # Step 3: Mutate the code
    mutated_codes = mutate_code(code, transformers)

    # Step 4: Ready to test
    #print(inputs)  # List of inputs
    #print(mutated_codes)  # First element is the original code


if __name__ == "__main__":
    run_python()
