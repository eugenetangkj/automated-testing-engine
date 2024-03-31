import json
from unittest.mock import MagicMock, patch
from its_test_engine.python.program_generator import (
    LeetCodePythonProgramGenerator,
    OpenAIPythonProgramGenerator,
)


def test_leetcode_python_program_generator():
    generator = LeetCodePythonProgramGenerator()

    signature, code = generator.generate_test_case()

    assert signature is not None
    assert code is not None


def test_leetcode_python_program_generator_with_missing_function_name():
    generator = LeetCodePythonProgramGenerator()
    generator.lines = [
        json.dumps(
            {
                "answer": {
                    "python": "a + b",
                    "java": "public int add(int a, int b) {\n    return a + b;\n}",
                }
            }
        )
    ]

    function_signature, code = generator.generate_test_case()
    assert function_signature["name"] is None
    assert code is not None


def generate_mock_response(content):
    response = MagicMock()
    response.choices = [MagicMock()]
    response.choices[0].message.content = content
    return response


@patch("its_test_engine.base.program_generator.openai_program_generator.OpenAI")
def test_openai_program_generator_generate_test_case_successful(mocker):
    mocker_instance = mocker.return_value
    open_ai_program_generator = OpenAIPythonProgramGenerator()

    response = {
        "function": "def add(a, b):\n    return a + b",
        "name": "add",
        "arguments": ["a", "b"],
        "return_type": "int",
    }
    mocker_instance.chat.completions.create.return_value = generate_mock_response(
        json.dumps(response)
    )

    # Valid JSON output, in the format we expect
    function_signature, code = open_ai_program_generator.generate_test_case()

    assert function_signature == {
        "name": "add",
        "argument_types": ["a", "b"],
        "return_type": "int",
    }

    assert code == "def add(a, b):\n    return a + b"
