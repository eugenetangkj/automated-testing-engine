"""
    Helper functions
"""

import ast
from copy import deepcopy
from itertools import chain, combinations


# Reference: https://stackoverflow.com/questions/374626/how-can-i-find-all-the-subsets-of-a-set-with-exactly-n-elements
def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))


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


def process_arguments(raw_arguments):
    """
    The argument format accepted by the ITS API is unique. We need to transform
    our internal argument format to be the format accepted by the ITS API

    Examples of transformations:
        [] -> "[]"
        [2] -> "[2]"
        [2, 3] -> "[[2,3]]"
    """

    if len(raw_arguments) == 0:
        return "[]"

    if len(raw_arguments) == 1:
        return "[" + str(raw_arguments[0]) + "]"

    output = "[["

    for index, current_raw_argument in enumerate(raw_arguments):
        output += str(current_raw_argument)
        if index < len(raw_arguments) - 1:
            output += ","

    output += "]]"
    return output
