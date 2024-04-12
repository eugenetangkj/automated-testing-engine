import subprocess
from unittest.mock import patch
import pytest
import its_test_engine.python.argument_generator as generator

CODE = """
def add(a, b):
    return a + b
"""

# generate a complicated code semgnet
COMPLICATED_CODE = """
def generate_random(seed, n):
    a = 1664525
    c = 1013904223
    m = 2**32
    result = []
    for _ in range(n):
        seed = (a * seed + c) % m
        result.append(seed)
    return result
"""


@pytest.mark.timeout(60)
def test_generate_arguments():
    argument_generator = generator.PynGuinArgumentGenerator(CODE)
    inputs = argument_generator.generate_arguments()

    assert len(inputs) > 0

    argument_generator = generator.PynGuinArgumentGenerator(COMPLICATED_CODE)
    inputs = argument_generator.generate_arguments()

    assert len(inputs) > 0


@patch("subprocess.check_output")
def test_generate_arguments_exception(mocker):
    mocker.side_effect = subprocess.CalledProcessError(1, "cmd")
    argument_generator = generator.PynGuinArgumentGenerator(CODE)
    inputs = argument_generator.generate_arguments()

    assert len(inputs) == 0

    mocker.side_effect = subprocess.TimeoutExpired("cmd", 1)
    argument_generator = generator.PynGuinArgumentGenerator(CODE)
    inputs = argument_generator.generate_arguments()

    assert len(inputs) == 0
