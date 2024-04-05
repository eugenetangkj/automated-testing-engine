import ast
import its_test_engine.python.modifier as mutator

CODE = """
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

    node = ast.parse(CODE)
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
        ["a = a + b + c", "a = a + c + b"],
    ]

    for test_case in test_cases:
        node = ast.parse(test_case[0])
        modified_node = transformer.visit(node)
        assert ast.unparse(modified_node) == test_case[1]

def test_de_morgan_modifier():
    transformer = mutator.DeMorganModifier()

    test_cases = [
        ["a or b", "not (not a and (not b))"], 
        ["a and b", "not (not a or not b)"],
        ["not a or b", "not (a and (not b))"],
        ["a or not b", "not (not a and b)"],
        ["not a and b", "not (a or not b)"],
        ["a and not b", "not (not a or b)"],
        ["not a or not b", "not (a and b)"],
        ["not a and not b", "not (a or b)"],
        ["a or (b and c)", "not (not a and (not (b and c)))"],
        ["a and (b or c)", "not (not a or not (b or c))"],
        ["a and not (b and c)", "not (not a or (b and c))"],
        ["def test_function(a, b):\n    if a or b:\n        return True\n    else:\n        return False",
         "def test_function(a, b):\n    if not (not a and (not b)):\n        return True\n    else:\n        return False"],
        ["a + b", "a + b"],
    ]

    for test_case in test_cases:
        node = ast.parse(test_case[0])
        modified_node = transformer.visit(node)
        assert ast.unparse(modified_node) == test_case[1]
    

if __name__ == "__main__":
    test_de_morgan_modifier()
    