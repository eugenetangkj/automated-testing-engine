from its_test_engine.base.program_generator.leetcode_program_generator import (
    LeetCodeProgramGenerator,
)


def test_leetcode_program_generator():
    generator = LeetCodeProgramGenerator(language="python")

    signature, code = generator.generate_test_case()

    assert signature is not None
    assert code is not None

    mock_question = {
        "answer": {
            "java": "Mock java solution"
        }
    }
    signature = generator.get_function_signatures(mock_question)
    assert signature is None

    mock_question = {
        "answer": {
            "java": "public ArrayList<Integer> mockFunction()"
        }
    }
    signature = generator.get_function_signatures(mock_question)
    assert signature is None
