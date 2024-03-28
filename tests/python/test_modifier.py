import ast, copy
import its_test_engine.python.modifier as mutator

code = """
def add(a, b):
    return a + b
"""


def evaluate_function(func_node, *args):
    func_name = func_node.name
    func_code = ast.unparse(func_node)
    namespace = {}

    try:
        exec(func_code, namespace)
        func = namespace[func_name]
        result = func(*args)
        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def test_variable_renamer():
    transformer = mutator.VariableRenamer()

    node = ast.parse(code)
    modified_node = transformer.visit(node)

    assert (
        ast.unparse(modified_node) == "def add(var_0, var_1):\n    return var_0 + var_1"
    )

    assert evaluate_function(node.body[0], 1, 2) == 3
    assert evaluate_function(modified_node.body[0], 1, 2) == 3


def test_bin_op_modified():
    transformer = mutator.BinOpModifier()

    test_cases = [
        ["a = a + b", "a = b + a"],
        ["a = b + a", "a = a + b"],
        ["a = a + 0", "a = a"],
        ["a = 0 + a", "a = a"],
        ["a = a * b", "a = b * a"],
        ["a = b * a", "a = a * b"],
        ["a = a * 1", "a = a"],
        ["a = 1 * a", "a = a"],
        ["a = a - b", "a = a + -b"],
        ["a = b - a", "a = b + -a"],
    ]

    for test_case in test_cases:
        node = ast.parse(test_case[0])
        modified_node = transformer.visit(node)
        assert ast.unparse(modified_node) == test_case[1]
