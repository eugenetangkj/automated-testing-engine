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
        try:
            # function_signature, base_code = self.program_generator.generate_test_case()
            # base_code = "def generate_random_number():\n    local_var = object()\n    seed = id(local_var)\n    a = 1140671485\n    c = 128201163\n    m = 2 ** 24\n    rand = seed\n    rand = (a * rand + c) % m\n    return rand"
            base_code = "def main():\n\tx = 2\n\treturn x"
            
            
            function_signature = {
                    "name": "main",
                    "argument_types": [],
                    "return_type": "float",
            }




        except SyntaxError as syntax_error:
            # Some LeetCode programs cannot be successfully parsed via their AST
            print(syntax_error)
            return None

        # Step 2: Generate inputs
        inputs = self.input_generator.generate_inputs(function_signature, base_code, 10)

        # Step 3: Mutate code
        try:
            modified_programs = mutate_code(base_code, self.transformers)
            modified_programs = ["def main():\n\tx = 2\n\t\treturn x"]
        except SyntaxError as syntax_error:
            # OpenAI might give code that cannot be mutated by the transformers
            # For example, it could have \n and \t in the base program string instead of using newlines and tabs
            print(syntax_error)
            return None
        # Step 4: Put base and mutated inputs into respective API endpoints
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

        new_inputs = []

        test_suite = ItsTestSuite(Language.PYTHON, "interpreter", base_code)
        test_suites.append(test_suite)

        for program_input in inputs:
            test_case = ItsTestCase(base_code)
            test_suite.add_test_case(test_case)

            _, interpreter_result = interpreter_tester.run_test(
                function_signature, parsed_base_program, program_input
            )
            test_case.add_result(interpreter_result)
            if interpreter_result.success:
                new_inputs.append(program_input)

        self.writer.write(test_suite)

        inputs = new_inputs

        # Remove inputs that failed to run in the interpreter
        # This is done to avoid errors in the other endpoints.

        endpoint_testers = {
            "error_localizer": error_localizer_endpoint_tester,
            "feedback_error": feedback_error_endpoint_tester,
            "feedback_fix": feedback_fix_endpoint_tester,
            "repair": repair_endpoint_tester,
        }

        # if len(inputs) == 0:
        #     return test_suites

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
                    inputs,
                )
                test_case.add_result(endpoint_test_result)

            self.writer.write(test_suite)

        return test_suites
