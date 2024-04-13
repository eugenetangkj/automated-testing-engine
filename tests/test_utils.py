from its_test_engine.utils import powerset, mutate_code
from its_test_engine.python.modifier import VariableRenamerModifier, BinOpModifier

CODE = """
def add(a, b):
    return a + b
"""


def test_powerset():
    assert list(powerset([1, 2, 3])) == [
        (),
        (1,),
        (2,),
        (3,),
        (1, 2),
        (1, 3),
        (2, 3),
        (1, 2, 3),
    ]
    assert list(powerset([1])) == [(), (1,)]


def test_mutate_code():
    transformers = [VariableRenamerModifier()]
    mutated_codes = mutate_code(CODE, transformers)
    assert len(mutated_codes) == 2

    transformers = [VariableRenamerModifier(), BinOpModifier()]
    mutated_codes = mutate_code(CODE, transformers)
    assert len(mutated_codes) == 4

    transformers = [VariableRenamerModifier(), VariableRenamerModifier()]
    mutated_codes = mutate_code(CODE, transformers)
    assert len(mutated_codes) == 3
