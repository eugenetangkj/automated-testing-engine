import pytest
from src.base_program_generator.csmith_program_generator import CsmithProgramGenerator


def test_generate_test_case():
	csmith = CsmithProgramGenerator()

	program = csmith.generate_test_case("C")

	assert program is not None
	assert len(program) > 0
	