import json
from unittest.mock import patch, MagicMock
import httpx
from its_test_engine.base.program_generator.openai_program_generator import (
    OpenAiProgramGenerator,
)


def generate_mock_response(content):
    response = MagicMock()
    response.choices = [MagicMock()]
    response.choices[0].message.content = content
    return response


@patch("its_test_engine.base.program_generator.openai_program_generator.OpenAI")
def test_openai_program_generator_generate_test_case_successful(mocker):
    mocker_instance = mocker.return_value
    open_ai_program_generator = OpenAiProgramGenerator("py", "")

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


@patch("its_test_engine.base.program_generator.openai_program_generator.OpenAI")
def test_openai_program_generator_generate_test_case_timeout(mocker):
    mocker_instance = mocker.return_value
    mocker_instance.chat.completions.create.side_effect = httpx.TimeoutException(
        message="Timeout"
    )

    open_ai_program_generator = OpenAiProgramGenerator("py", "")
    # Timeout exception
    output = open_ai_program_generator.generate_test_case()
    assert output is None


@patch("its_test_engine.base.program_generator.openai_program_generator.OpenAI")
def test_openai_program_generator_generate_test_case_invalid_json(mocker):
    mocker_instance = mocker.return_value
    open_ai_program_generator = OpenAiProgramGenerator("py", "")

    # Invalid string that cannot be parsed into JSON
    mocker_instance.chat.completions.create.return_value = generate_mock_response("{}")
    output = open_ai_program_generator.generate_test_case()
    assert output is None

    # JSON with missing keys
    mocker_instance.chat.completions.create.return_value = generate_mock_response(
        json.dumps({"return_type": "int"})
    )
    output = open_ai_program_generator.generate_test_case()
    assert output is None

    mocker_instance.chat.completions.create.return_value = generate_mock_response(
        "invalid json"
    )
    output = open_ai_program_generator.generate_test_case()
    assert output is None


# Test the generate user prompt method
def test_openai_program_generator_generate_user_prompt():
    open_ai_program_generator = OpenAiProgramGenerator("py", "")

    # Test case 1: Empty constraints
    constraints = ""
    output = open_ai_program_generator.generate_user_prompt(constraints)
    assert output == "###Constraints: "

    # Test case 2: Normal string constraints
    constraints = "Have 1 while loop"
    output = open_ai_program_generator.generate_user_prompt(constraints)
    assert output == "###Constraints: Have 1 while loop"

    # Test case 3: No constraints given (None)
    constraints = None
    output = open_ai_program_generator.generate_user_prompt(constraints)
    assert output == "###Constraints: None"

    # Test case 4: No constraints given ("None")
    constraints = "None"
    output = open_ai_program_generator.generate_user_prompt(constraints)
    assert output == "###Constraints: None"
