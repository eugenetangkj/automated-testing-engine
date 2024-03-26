from its_test_engine.python.program_generator import LeetCodeProgramGenerator


def test_leetcode_program_generator():

    generator = LeetCodeProgramGenerator()

    signature, code = generator.generate_test_case()

    assert signature is not None
    assert code is not None

    print(signature)

    print(code)
