"""
Tester class that contains the logical steps taken in testing
"""

from its_test_engine.enums import Language
from its_test_engine.utils import mutate_code
from its_test_engine.base.argument_generator import BaseArgumentGenerator
from its_test_engine.base.program_generator import BaseProgramGenerator

from its_test_engine.its.its_api_connection import ItsApiConnection
from its_test_engine.its.endpoint_tester import (
    ParserTester,
    InterpreterTester,
    RepairEndpointTester,
    FeedbackFixEndpointTester,
    FeedbackErrorEndpointTester,
    ErrorLocalizerEndpointTester,
)
from its_test_engine.its.test_result import (
    ItsTestSuite,
    ItsTestCase,
)


class Tester:
    # Number of sets of arguments to generate for each test case
    NO_OF_ARGUMENTS = 10


    def __init__(
        self,
        language: Language,
        program_generator: BaseProgramGenerator,
        transformers: list[any],
        argument_generator: BaseArgumentGenerator,
        writer,
    ):
        """
        Initialises a Tester instance

        Parameters:
            language: Language of programs that this Tester instance tests
            program_generator: Base program generator that will be used to generate
            base programs during testing
            transformers: List of modifiers that will modify the base programs
            argument_generator: Argument generator that will be used to generate
            arguments for the functions given their function signature
            writer: Instance that writes the test results to files
        """
        self.language = language
        self.program_generator = program_generator
        self.transformers = transformers
        self.argument_generator = argument_generator
        self.writer = writer

    def run_tests(self) -> list[ItsTestSuite]:
        """
        Runs the testing logic.

        1. Base program generation
        2. Generate arguments
        3. Modify base programs
        4. Test against ITS API

        """
        its_api_connection = ItsApiConnection(self.language)

        # Step 1: Generate test case
        try:
            function_signature, base_code = self.program_generator.generate_test_case()
        except SyntaxError as syntax_error:
            # Some LeetCode programs cannot be successfully parsed via their AST
            print(syntax_error)
            return None

        # Step 2: Generate arguments
        arguments = self.argument_generator.generate_arguments(
            function_signature, base_code, self.NO_OF_ARGUMENTS
        )

        # Step 3: Mutate code
        try:
            modified_programs = mutate_code(base_code, self.transformers)
        except SyntaxError as syntax_error:
            # OpenAI might give code that cannot be mutated by the transformers
            # For example, it could have \n and \t in the base program string instead of using newlines and tabs
            print(syntax_error)
            return None
        # Step 4: Put base and mutated programs into respective API endpoints
        parser_tester = ParserTester(its_api_connection)
        interpreter_tester = InterpreterTester(its_api_connection)
        repair_endpoint_tester = RepairEndpointTester(its_api_connection)
        feedback_fix_endpoint_tester = FeedbackFixEndpointTester(its_api_connection)
        feedback_error_endpoint_tester = FeedbackErrorEndpointTester(its_api_connection)
        error_localizer_endpoint_tester = ErrorLocalizerEndpointTester(
            its_api_connection
        )

        test_suites = []

        parsed_base_program, _ = parser_tester.run_test(base_code)

        parsed_modified_programs = []

        test_suite = ItsTestSuite(Language.PYTHON, "parser", base_code)
        test_suites.append(test_suite)

        for modified_code in modified_programs:
            test_case = ItsTestCase(modified_code)
            test_suite.add_test_case(test_case)

            parsed_modified_program, parser_result = parser_tester.run_test(
                modified_code
            )
            test_case.add_result(parser_result)

            parsed_modified_programs.append(
                (modified_code, parsed_modified_program, parser_result)
            )

        self.writer.write(test_suite)

        # if all programs failed to parse
        if all(
            (
                not parser_result.success
                for _, _, parser_result in parsed_modified_programs
            )
        ):
            return test_suites

        new_arguments = []

        test_suite = ItsTestSuite(Language.PYTHON, "interpreter", base_code)
        test_suites.append(test_suite)

        for program_argument in arguments:
            test_case = ItsTestCase(base_code)
            test_suite.add_test_case(test_case)

            _, interpreter_result = interpreter_tester.run_test(
                function_signature, parsed_base_program, program_argument
            )
            test_case.add_result(interpreter_result)
            if interpreter_result.success:
                new_arguments.append(program_argument)

        self.writer.write(test_suite)

        arguments = new_arguments

        # Remove arguments that failed to run in the interpreter
        # This is done to avoid errors in the other endpoints.

        endpoint_testers = {
            "error_localizer": error_localizer_endpoint_tester,
            "feedback_error": feedback_error_endpoint_tester,
            "feedback_fix": feedback_fix_endpoint_tester,
            "repair": repair_endpoint_tester,
        }

        if len(arguments) == 0:
            return test_suites

        for endpoint, endpoint_tester in endpoint_testers.items():
            test_suite = ItsTestSuite(Language.PYTHON, endpoint, base_code)
            test_suites.append(test_suite)

            for modified_code, parsed_modified_program, _ in parsed_modified_programs:
                test_case = ItsTestCase(modified_code)
                test_suite.add_test_case(test_case)

                endpoint_test_result = endpoint_tester.run_test(
                    function_signature,
                    base_code,
                    modified_code,
                    parsed_base_program,
                    parsed_modified_program,
                    arguments,
                )
                test_case.add_result(endpoint_test_result)

            self.writer.write(test_suite)

        return test_suites
