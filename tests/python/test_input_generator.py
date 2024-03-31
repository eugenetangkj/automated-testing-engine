import pytest
import subprocess
from unittest.mock import patch
import its_test_engine.python.input_generator as generator

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
def test_generate_inputs():
    input_generator = generator.PynGuinInputGenerator(CODE)
    inputs = input_generator.generate_inputs()

    assert len(inputs) > 0

    input_generator = generator.PynGuinInputGenerator(COMPLICATED_CODE)
    inputs = input_generator.generate_inputs()

    assert len(inputs) > 0


@patch("subprocess.check_output")
def test_generate_inputs_exception(mocker):
    mocker.side_effect = subprocess.CalledProcessError(1, "cmd")
    input_generator = generator.PynGuinInputGenerator(CODE)
    inputs = input_generator.generate_inputs()

    assert len(inputs) == 0

    mocker.side_effect = subprocess.TimeoutExpired("cmd", 1)
    input_generator = generator.PynGuinInputGenerator(CODE)
    inputs = input_generator.generate_inputs()

    assert len(inputs) == 0
