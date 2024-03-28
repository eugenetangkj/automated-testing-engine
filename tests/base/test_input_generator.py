import pytest
from its_test_engine.base.input_generator.random_input_generator import (
    RandomInputGenerator,
)

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


def test_random_input_generator():
    types = ["int", "int"]
    input_generator = RandomInputGenerator()

    inputs = input_generator.generate_inputs(["int"], 20)

    assert len(inputs) == 20
