from its_test_engine.base.program_generator.openai_program_generator import (
    OpenAiProgramGenerator,
)
import httpx

# Mock classes that simulates OpenAI API
class MockChatCompletionMessage():
    def __init__(self, mock_content):
        self.content = mock_content

class MockChoice():
    def __init__(self, mock_message: MockChatCompletionMessage):
        self.message = mock_message

class MockChatCompletion():
    def __init__(self, mock_choice:MockChoice):
        self.choices = []
        self.choices.append(mock_choice)

# Mock function to simulate a properly formatted JSON returned from OpenAI
def mock_get_answer_from_openai_api(system_prompt, user_prompt):
    mock_chat_completion_message = MockChatCompletionMessage('{ "function": "def sum_nums(x, y, z): \\n\\tres_sum = x + y + z \\n\\treturn res_sum", "name": "sum_nums","arguments": ["int", "int", "int"], "return_type": "int"}')
    mock_choice = MockChoice(mock_chat_completion_message)
    mock_chat_completion = MockChatCompletion(mock_choice)
    return mock_chat_completion

# Mock function to simulate a timeout from OpenAI
def mock_get_timeout_from_openai_api(system_prompt, user_prompt):
    raise httpx.TimeoutException("Mock timeout message")

# Mock function that simulates a string that cannot be parsed into JSON, returned from OpenAI.
# In this case, we just have a string that cannot parsed into JSON.
def mock_get_invalid_json_from_openai_api(system_prompt, user_prompt):
    mock_chat_completion_message = MockChatCompletionMessage('{"return_type": "int"}')
    mock_choice = MockChoice(mock_chat_completion_message)
    mock_chat_completion = MockChatCompletion(mock_choice)
    return mock_chat_completion

# Mock function that simulates a JSON without required keys returned from OpenAI. In this case, there is only
# the key 'return_type' so in the actual function, it will throw a key error
def mock_get_json_without_all_keys_from_openai_api(system_prompt, user_prompt):
    mock_chat_completion_message = MockChatCompletionMessage('{"return_type": "int"}')
    mock_choice = MockChoice(mock_chat_completion_message)
    mock_chat_completion = MockChatCompletion(mock_choice)
    return mock_chat_completion

# Test the generate test_case() method
def test_openai_program_generator_generate_test_case():
    open_ai_program_generator = OpenAiProgramGenerator("py", "")

    # Test case 1: Valid JSON output, in the format we expect
    output = open_ai_program_generator.generate_test_case(mock_get_answer_from_openai_api)
    assert output == ({'name': 'sum_nums', 'argument_types': ['int', 'int', 'int'], 'return_type': 'int'},
                      'def sum_nums(x, y, z): \n\tres_sum = x + y + z \n\treturn res_sum') 
    
    # Test case 2: Timeout exception
    output = open_ai_program_generator.generate_test_case(mock_get_timeout_from_openai_api)
    assert output == None

    # Test case 3: Invalid string that cannot be parsed into JSON
    output = open_ai_program_generator.generate_test_case(mock_get_invalid_json_from_openai_api)
    assert output == None

    # Test case 4: JSON with missing keys
    output = open_ai_program_generator.generate_test_case(mock_get_json_without_all_keys_from_openai_api)
    assert output == None

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
