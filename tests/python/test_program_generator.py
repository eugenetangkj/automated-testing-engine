from its_test_engine.python.program_generator import LeetCodePythonProgramGenerator


def test_leetcode_python_program_generator():
    generator = LeetCodePythonProgramGenerator()

    signature, code = generator.generate_test_case()

    assert signature is not None
    assert code is not None
