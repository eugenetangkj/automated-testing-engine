from its_test_engine.base.program_generator.leetcode_program_generator import (
    LeetCodeProgramGenerator,
)


def test_leetcode_program_generator():
    generator = LeetCodeProgramGenerator(language="python")

    signature, code = generator.generate_test_case()

    assert signature is not None
    assert code is not None

    print(code)
