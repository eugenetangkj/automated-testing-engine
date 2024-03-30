from its_test_engine.base.input_generator import RandomInputGenerator


CODE = """
def add(a, b):
    return a + b
"""

# generate a complicated code semgnet
COMPLICAED_CODE = """
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
    input_generator = RandomInputGenerator()

    inputs = input_generator.generate_inputs(
        {"name": "add", "argument_types": ["int", "int"]}, CODE, 20
    )

    assert len(inputs) == 20

    inputs = input_generator.generate_inputs(
        {"name": "add", "argument_types": ["int", "int"]}, COMPLICAED_CODE, 20
    )

    assert len(inputs) == 20
