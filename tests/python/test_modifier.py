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


def test_idempotent_modifier():
    # Test indempotent relation 1
    test_cases_and = [
        ["a and b", "(a and a) and (b and b)"],
        ["a or b", "a and a or (b and b)"],

        ["def test_function(a, b):\n    if a and b:\n        return True\n    else:\n        return False",
         "def test_function(a, b):\n    if (a and a) and (b and b):\n        return True\n    else:\n        return False"],

        ["def test_function(a, b):\n    if a or b:\n        return True\n    else:\n        return False",
         "def test_function(a, b):\n    if a and a or (b and b):\n        return True\n    else:\n        return False"],

        ["def test_function(a, b):\n    x = x + 1\n    if a and b:\n        return True\n    else:\n        return False",
        "def test_function(a, b):\n    x = x + 1\n    if (a and a) and (b and b):\n        return True\n    else:\n        return False"]
    ]

    transformer_and = mutator.IdempotentModifier(type_of_transformation=1)
    for test_case in test_cases_and:
        node = ast.parse(test_case[0])
        modified_node = transformer_and.visit(node)
        assert ast.unparse(modified_node) == test_case[1]


    # # Test indempotent relation 2
    test_cases_or = [
        ["a and b", "(a or a) and (b or b)"],
        ["a or b", "(a or a) or (b or b)"],

        ["def test_function(a, b):\n    if a and b:\n        return True\n    else:\n        return False",
        "def test_function(a, b):\n    if (a or a) and (b or b):\n        return True\n    else:\n        return False"],

        ["def test_function(a, b):\n    if a or b:\n        return True\n    else:\n        return False",
         "def test_function(a, b):\n    if (a or a) or (b or b):\n        return True\n    else:\n        return False"],
    ]

    transformer_or = mutator.IdempotentModifier(type_of_transformation=2)
    for test_case in test_cases_or:
        node = ast.parse(test_case[0])
        modified_node = transformer_or.visit(node)
        assert ast.unparse(modified_node) == test_case[1]


def test_identity_modifier():
    # Test identity relation 1
    test_cases_and = [

        ["a and b", "(a and True) and (b and True)"],
        ["a or b", "a and True or (b and True)"],

        ["def test_function(a, b):\n    if a and b:\n        return True\n    else:\n        return False",
        "def test_function(a, b):\n    if (a and True) and (b and True):\n        return True\n    else:\n        return False"],

        ["def test_function(a, b):\n    if a or b:\n        return True\n    else:\n        return False",
        "def test_function(a, b):\n    if a and True or (b and True):\n        return True\n    else:\n        return False"],
    ]

    transformer_and = mutator.IdentityModifier(type_of_transformation=1)
    for test_case in test_cases_and:
        node = ast.parse(test_case[0])
        modified_node = transformer_and.visit(node)
        assert ast.unparse(modified_node) == test_case[1]


    # Test indempotent relation 2
    test_cases_or = [

        ["a and b", "(a or False) and (b or False)"],
        ["a or b", "(a or False) or (b or False)"],

        ["def test_function(a, b):\n    if a and b:\n        return True\n    else:\n        return False",
        "def test_function(a, b):\n    if (a or False) and (b or False):\n        return True\n    else:\n        return False"],

        ["def test_function(a, b):\n    if a or b:\n        return True\n    else:\n        return False",
         "def test_function(a, b):\n    if (a or False) or (b or False):\n        return True\n    else:\n        return False"],
    ]

    transformer_or = mutator.IdentityModifier(type_of_transformation=2)
    for test_case in test_cases_or:
        node = ast.parse(test_case[0])
        modified_node = transformer_or.visit(node)
        assert ast.unparse(modified_node) == test_case[1]


def test_unravel_ternary_modifier():
    
    transformer = mutator.UnravelTernaryModifier()

    test_cases = [
        ["c = a if a > 5 else b", "if a > 5:\n    c = a\nelse:\n    c = b"],

        ["def test_function(a):\n    return True if a > 5 else False",
         "def test_function(a):\n    if a > 5:\n        return True\n    else:\n        return False"],

        ["def test_function(a):\n    a = a + 1\n    return True if a > 5 else False",
         "def test_function(a):\n    a = a + 1\n    if a > 5:\n        return True\n    else:\n        return False"],

        ["c = 2 + (a if a > 5 else b)", "if a > 5:\n    c = 2 + a\nelse:\n    c = 2 + b"],
        ["c = (a if a > 5 else b) + 2", "if a > 5:\n    c = a + 2\nelse:\n    c = b + 2"],

        ["c = (a if a > 5 else b) + (c if c < 10 else d)",
         "if a > 5 and c < 10:\n    c = a + c\nelif a > 5 and (not c < 10):\n    c = a + d\nelif not a > 5 and c < 10:\n    c = b + c\nelif not a > 5 and (not c < 10):\n    c = b + d"],

        ["c = 1 + 2", "c = 1 + 2"]
    ]

    for test_case in test_cases:
        node = ast.parse(test_case[0])
        modified_node = transformer.visit(node)
        assert ast.unparse(modified_node) == test_case[1]


def test_for_range_to_while_loop_modifier():
    transformer = mutator.ForRangeToWhileLoopModifier()

    test_cases = [
        ["for i in range(5):\n    print(i)",
         "i = 0\nwhile i < 5:\n    print(i)\n    i = i + 1"],

        ["for x in range(0, 6, 2):\n    x = x + 1\n    call_func()",
         "x = 0\nwhile x < 6:\n    x = x + 1\n    call_func()\n    x = x + 2"],

        ["for x in range(6, 1, -2):\n    x = x + 1\n    call_func()",
         "x = 6\nwhile x > 1:\n    x = x + 1\n    call_func()\n    x = x + -2"],

        ["for x in range(6, -5):\n    x = x + 1\n    call_func()",
         "x = 6\nwhile x < -5:\n    x = x + 1\n    call_func()\n    x = x + 1"],

        ["def func(x):\n    x = x + 1\n    for j in range(2, 5):\n        x += 1\n    return x",
         "def func(x):\n    x = x + 1\n    j = 2\n    while j < 5:\n        x += 1\n        j = j + 1\n    return x"],

        ["def func(x):\n    x = x + 1\n    for j in range(2, 5, 0):\n        x += 1\n    return x",
         "def func(x):\n    x = x + 1\n    j = 2\n    while j < 5:\n        x += 1\n        j = j + 0\n    return x"],
    ]

    for test_case in test_cases:
        node = ast.parse(test_case[0])
        modified_node = transformer.visit(node)
        assert ast.unparse(modified_node) == test_case[1]


def test_extra_argument_reassignment_modifier():

    transformer = mutator.ExtraArgumentReassignmentModifier()

    test_cases = [
       
        ["def func(x):\n    return x",
         "def func(x):\n    x = x\n    x = x\n    x = x\n    x = x\n    x = x\n    return x"],

        ["def func(x, y):\n    sum = x + y\n    return sum",
         "def func(x, y):\n    x = x\n    x = x\n    x = x\n    x = x\n    x = x\n    y = y\n    y = y\n    " +\
            "y = y\n    y = y\n    y = y\n    sum = x + y\n    return sum"],     
    ]

    for test_case in test_cases:
        node = ast.parse(test_case[0])
        modified_node = transformer.visit(node)
        assert ast.unparse(modified_node) == test_case[1]


def test_swap_arguments_modifier():
    transformer = mutator.SwapArgumentsModifier()

    test_cases = [
        ["def func(a, b):\n    diff = a - b\n    return diff",
         "def func(a, b):\n    (a, b) = (b, a)\n    diff = b - a\n    return diff"],

        ["def func(x, y, z):\n    diff = x - z + y\n    return diff",
         "def func(x, y, z):\n    (x, y, z) = (z, y, x)\n    diff = z - x + y\n    return diff"],

        ["def func(w, x, y, z):\n    diff = x - z * w + y\n    return diff",
         "def func(w, x, y, z):\n    (w, x, y, z) = (z, y, x, w)\n    diff = y - w * z + x\n    return diff"],

        ["def func(x, y):\n    diff = x - y\n    sum = x + y\n    return diff * sum",
         "def func(x, y):\n    (x, y) = (y, x)\n    diff = y - x\n    sum = y + x\n    return diff * sum"]
    ]

    for test_case in test_cases:
        node = ast.parse(test_case[0])
        modified_node = transformer.visit(node)
        assert ast.unparse(modified_node) == test_case[1]


def test_wrap_in_if_true_modifier():
    transformer = mutator.WrapInIfTrueModifier()

    test_cases = [
        ["def func(x, y, z):\n    return True",
         "def func(x, y, z):\n    if True:\n        return True"],

        ["def func(x, y):\n    sum = x + y\n    diff = x - y\n    return sum + diff",
         "def func(x, y):\n    if True:\n        sum = x + y\n        diff = x - y\n        return sum + diff"],
    ]

    for test_case in test_cases:
        node = ast.parse(test_case[0])
        modified_node = transformer.visit(node)
        print(ast.unparse(modified_node))
        assert ast.unparse(modified_node) == test_case[1]
