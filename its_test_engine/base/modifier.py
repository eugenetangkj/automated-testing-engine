import ast
from copy import deepcopy
from its_test_engine.utils import powerset


def mutate_code(code, transformers):
    mutated_codes = []
    mutated_codes_exists = set()

    for subset_of_transformers in powerset(transformers):
        mutated_code = ast.parse(deepcopy(code))
        for transformer in subset_of_transformers:
            mutated_code = transformer.visit(mutated_code)

        mutated_code = ast.unparse(mutated_code)
        if hash(mutated_code) not in mutated_codes_exists:
            mutated_codes.append(mutated_code)
            mutated_codes_exists.add(hash(mutated_code))

    return mutated_codes
