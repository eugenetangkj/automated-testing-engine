"""
    Tester for the feedback fixendpoint
"""

import json

from its_test_engine.its.endpoint_tester import EndpointTester
from its_test_engine.enums import TypeOfMetamorphicRelation
from its_test_engine.its.test_result import ItsTestResult


class FeedbackFixEndpointTester(EndpointTester):
    endpoint = "feedback_fix"

    def run_test(
        self,
        function_signature: str,
        base_program_string: str,
        modified_program_string: str,
        parsed_base_program: str,
        parsed_modified_program: str,
        arguments: list[any],
    ) -> ItsTestResult:

        function_name = function_signature["name"]
        try:
            feedback_fix_output = self.its_api_connection.call_feedback_fix_endpoint(
                parsed_base_program,
                parsed_modified_program,
                function_name,
                "[]",
                arguments,
            )

            passed = False

            if (
                self.type_of_metamorphic_relation
                == TypeOfMetamorphicRelation.EQUIVALENT
            ):
                passed = len(feedback_fix_output) == 0
            else:
                passed = len(feedback_fix_output) != 0

            return ItsTestResult(
                passed,
                self.endpoint,
                "Success" if passed else "Feedback fix endpoint failed",
                json.dumps(feedback_fix_output, indent=4),
            )
        except Exception as e:
            message = e.__class__.__name__ + "\n" + str(e)
            return ItsTestResult(False, self.endpoint, message, None)
