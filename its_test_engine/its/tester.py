from its_test_engine.enums import Language
from its_test_engine.utils import mutate_code
from its_test_engine.base.input_generator import BaseInputGenerator
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
    def __init__(
        self,
        language: Language,
        program_generator: BaseProgramGenerator,
        transformers: list[any],
        input_generator: BaseInputGenerator,
        writer,
    ):
        self.language = language
        self.program_generator = program_generator
        self.transformers = transformers
        self.input_generator = input_generator
        self.writer = writer

    def run_tests(self) -> list[ItsTestSuite]:
        its_api_connection = ItsApiConnection(self.language)

        # Step 1: Generate test case
        function_signature, base_code = self.program_generator.generate_test_case()

        # Step 2: Generate inputs
        inputs = self.input_generator.generate_inputs(function_signature, base_code, 10)

        # Step 3: Mutate code
        modified_programs = mutate_code(base_code, self.transformers)

        parser_tester = ParserTester(its_api_connection)
        interpreter_tester = InterpreterTester(its_api_connection)
        repair_endpoint_tester = RepairEndpointTester(its_api_connection)
        feedback_fix_endpoint_tester = FeedbackFixEndpointTester(its_api_connection)
        feedback_error_endpoint_tester = FeedbackErrorEndpointTester(its_api_connection)
        error_localizer_endpoint_tester = ErrorLocalizerEndpointTester(
            its_api_connection
        )

        test_suites = []

        parsed_base_program, base_parser_result = parser_tester.run_test(base_code)

        parsed_modified_programs = []

        test_suite = ItsTestSuite(Language.PYTHON, base_code, None)
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
            [
                not parser_result.success
                for _, _, parser_result in parsed_modified_programs
            ]
        ):
            return test_suites

        for program_input in inputs:
            test_suite = ItsTestSuite(Language.PYTHON, base_code, program_input)
            test_suites.append(test_suite)

            # Step 1: Parse base program
            test_suite.set_parser_result(base_parser_result)
            if not base_parser_result.success:
                break

            # Step 2: Run interpreter to check if base program runs successfully
            interpreter_output, interpreter_result = interpreter_tester.run_test(
                function_signature, parsed_base_program, program_input
            )
            test_suite.set_interpreter_result(interpreter_result)
            if not interpreter_result.success:
                continue

            # Step 3: Test each modified code
            for index, modified_code in enumerate(modified_programs):
                # Get pre-parsed modified program
                _, parsed_modified_program, parser_result = parsed_modified_programs[
                    index
                ]
                if not parser_result.success:
                    continue

                test_case = ItsTestCase(modified_code)
                test_suite.add_test_case(test_case)

                test_case.add_result(parser_result)

                interpreter_output, interpreter_result = interpreter_tester.run_test(
                    function_signature, parsed_modified_program, program_input
                )
                test_case.add_result(interpreter_result)
                if not interpreter_result.success:
                    continue

                repair_test_result = repair_endpoint_tester.run_test(
                    function_signature,
                    base_code,
                    modified_code,
                    parsed_base_program,
                    parsed_modified_program,
                    program_input,
                )
                test_case.add_result(repair_test_result)

                error_localizer_test_result = error_localizer_endpoint_tester.run_test(
                    function_signature,
                    base_code,
                    modified_code,
                    parsed_base_program,
                    parsed_modified_program,
                    program_input,
                )
                test_case.add_result(error_localizer_test_result)

                feedback_error_test_result = feedback_error_endpoint_tester.run_test(
                    function_signature,
                    base_code,
                    modified_code,
                    parsed_base_program,
                    parsed_modified_program,
                    program_input,
                )
                test_case.add_result(feedback_error_test_result)

                feedback_fix_test_result = feedback_fix_endpoint_tester.run_test(
                    function_signature,
                    base_code,
                    modified_code,
                    parsed_base_program,
                    parsed_modified_program,
                    program_input,
                )
                test_case.add_result(feedback_fix_test_result)

            self.writer.write(test_suite)
            if not test_suite.success:
                break
        return test_suites
