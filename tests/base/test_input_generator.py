from its_test_engine.base.input_generator import RandomInputGenerator


CODE = """
def add(a, b):
    return a + b
"""

# generate a complicated code segment
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


def test_random_input_generator():
    input_generator = RandomInputGenerator()

    inputs = input_generator.generate_inputs(
        {"name": "add", "argument_types": ["int", "int"]}, CODE, 20
    )

    assert len(inputs) == 20
    assert all(len(i) == 2 for i in inputs)
    assert all(isinstance(i[0], int) for i in inputs)
    assert all(isinstance(i[1], int) for i in inputs)

    inputs = input_generator.generate_inputs(
        {"name": "add", "argument_types": ["int", "int"]}, COMPLICATED_CODE, 20
    )

    assert len(inputs) == 20
    assert all(len(i) == 2 for i in inputs)
    assert all(isinstance(i[0], int) for i in inputs)
    assert all(isinstance(i[1], int) for i in inputs)

    inputs = input_generator.generate_inputs(
        {"name": "add", "argument_types": ["float", "bool"]}, CODE, 20
    )

    assert len(inputs) == 20
    assert all(len(i) == 2 for i in inputs)
    assert all(isinstance(i[0], float) for i in inputs)
    assert all(isinstance(i[1], bool) for i in inputs)

    inputs = input_generator.generate_inputs(
        {"name": "add", "argument_types": ["str", "List[int]"]}, CODE, 20
    )

    assert len(inputs) == 20
    assert all(len(i) == 2 for i in inputs)
    assert all(isinstance(i[0], str) for i in inputs)
    assert all(isinstance(i[1], list) for i in inputs)
    assert all(all(isinstance(j, int) for j in i[1]) for i in inputs)

    inputs = input_generator.generate_inputs(
        {"name": "add", "argument_types": ["List[float]", "List[str]"]}, CODE, 20
    )

    assert len(inputs) == 20
    assert all(len(i) == 2 for i in inputs)
    assert all(isinstance(i[0], list) for i in inputs)
    assert all(isinstance(i[1], list) for i in inputs)
    assert all(all(isinstance(j, float) for j in i[0]) for i in inputs)
    assert all(all(isinstance(j, str) for j in i[1]) for i in inputs)

    inputs = input_generator.generate_inputs(
        {"name": "add", "argument_types": ["List[bool]", "List[bool]"]}, CODE, 20
    )

    assert len(inputs) == 20
    assert all(len(i) == 2 for i in inputs)
    assert all(isinstance(i[0], list) for i in inputs)
    assert all(isinstance(i[1], list) for i in inputs)
    assert all(all(isinstance(j, bool) for j in i[0]) for i in inputs)
    assert all(all(isinstance(j, bool) for j in i[1]) for i in inputs)
