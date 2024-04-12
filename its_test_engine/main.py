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


def run_leetcode_programs():
    program_generator = LeetCodePythonProgramGenerator()
    argument_generator = RandomArgumentGenerator()
    transformers = [VariableRenamerModifier(), BinOpModifier()]

    tester = Tester(
        Language.PYTHON, program_generator, transformers, argument_generator, writer
    )
    tester.run_tests()


def run_open_ai_programs():
    program_generator = OpenAIPythonProgramGenerator()
    argument_generator = RandomArgumentGenerator()
    transformers = [VariableRenamerModifier(), BinOpModifier()]

    tester = Tester(
        Language.PYTHON, program_generator, transformers, argument_generator, writer
    )
    tester.run_tests()


if __name__ == "__main__":
    run_leetcode_programs()
    run_open_ai_programs()
