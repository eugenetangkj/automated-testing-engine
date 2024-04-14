"""
    Entry point of application
"""

from its_test_engine.enums import Language
from its_test_engine.its.tester import Tester
from its_test_engine.base.argument_generator import RandomArgumentGenerator
from its_test_engine.python.modifier import (
    VariableRenamerModifier,
    BinOpModifier,
    ForRangeToWhileLoopModifier,
    UnravelTernaryModifier,
    DeMorganModifier,
    IdempotentModifier,
    IdentityModifier,
    ExtraArgumentReassignmentModifier,
    SwapArgumentsModifier,
    WrapInIfTrueModifier,
    WrapInTryBlockModifier,
    WrapInExceptBlockModifier,
    ReverseListModifier,
)
from its_test_engine.python.program_generator import (
    LeetCodePythonProgramGenerator,
    OpenAIPythonProgramGenerator,
)
from its_test_engine.its.test_result import ItsTestSuitesMarkdownWriter

writer = ItsTestSuitesMarkdownWriter("test_results")


def run_leetcode_programs(number_of_test_cases: int):
    """
        Generate and run test cases using LeetCodeProgramGenerator
        to generate base Python programs.

        Parameters:
            number_of_test_cases: Number of test cases to generate using
            the LeetCodeProgramGenerator
    """
    program_generator = LeetCodePythonProgramGenerator()

    # Choose the argument generator
    argument_generator = RandomArgumentGenerator()

    # Put in modifiers that you want to use
    transformers = [VariableRenamerModifier(), BinOpModifier()]

    tester = Tester(
        Language.PYTHON, program_generator, transformers, argument_generator, writer
    )

    # Run for a specified number of test cases
    for _ in range(number_of_test_cases):
        tester.run_tests()


def run_open_ai_programs(number_of_test_cases):
    """
        Generate and run test cases using OpenAiProgramGenerator
        to generate base Python programs.

        Parameters:
            number_of_test_cases: Number of test cases to generate using
            the OpenAiProgramGenerator
    """

    # You can specify constraints for OpenAI to generate programs for
    # If you do not want constraints, can just use OpenAIPythonProgramGenerator()
    program_generator = OpenAIPythonProgramGenerator("Use 1 ternary operator")

    # Choose the argument generator
    argument_generator = RandomArgumentGenerator()

    # Put in modifiers that you want to use
    transformers = [UnravelTernaryModifier()]

    tester = Tester(
        Language.PYTHON, program_generator, transformers, argument_generator, writer
    )

    # Run for a specified number of test cases
    for _ in range(number_of_test_cases):
        tester.run_tests()


if __name__ == "__main__":
    # run_leetcode_programs(10)
    run_open_ai_programs(1)
