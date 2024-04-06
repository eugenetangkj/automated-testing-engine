"""
    Entry point of application
"""

from its_test_engine.enums import Language
from its_test_engine.its.tester import Tester
from its_test_engine.base.input_generator import RandomInputGenerator
from its_test_engine.python.modifier import VariableRenamer, BinOpModifier, ForRangeToWhileLoopModifier, UnravelTernaryModifier, DeMorganModifier
from its_test_engine.python.program_generator import (
    LeetCodePythonProgramGenerator,
    OpenAIPythonProgramGenerator,
)
from its_test_engine.its.test_result import ItsTestSuitesMarkdownWriter

writer = ItsTestSuitesMarkdownWriter("test_results")


def run_leetcode_programs():
    program_generator = LeetCodePythonProgramGenerator()
    input_generator = RandomInputGenerator()
    transformers = [VariableRenamer(), BinOpModifier()]

    tester = Tester(
        Language.PYTHON, program_generator, transformers, input_generator, writer
    )
    tester.run_tests()


def run_open_ai_programs():
    program_generator = OpenAIPythonProgramGenerator()
    input_generator = RandomInputGenerator()
    transformers = [DeMorganModifier()]

    tester = Tester(
        Language.PYTHON, program_generator, transformers, input_generator, writer
    )
    tester.run_tests()


if __name__ == "__main__":
    #run_leetcode_programs()
    run_open_ai_programs()
