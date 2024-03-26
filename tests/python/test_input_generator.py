import pytest
import its_test_engine.python.input_generator as generator

code = """
def add(a, b):
    return a + b
"""

# generate a complicated code semgnet
complicated_code = """
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
    input_generator = generator.PynGuinInputGenerator(code)
    inputs = input_generator.generate_inputs()

    assert len(inputs) > 0

    input_generator = generator.PynGuinInputGenerator(complicated_code)
    inputs = input_generator.generate_inputs()

    assert len(inputs) > 0


def test_random_input_generator():
    types = ["int", "int"]
    input_generator = generator.RandomInputGenerator(code, types, no_of_inputs=20)

    inputs = input_generator.generate_inputs()

    assert len(inputs) == 20
