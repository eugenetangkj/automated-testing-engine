"""
    Helper functions
"""

import ast
from copy import deepcopy
from itertools import chain, combinations


# Reference: https://stackoverflow.com/questions/374626/how-can-i-find-all-the-subsets-of-a-set-with-exactly-n-elements
def powerset(iterable):
    """
    Calculates the powerset of an iterable

    Example:
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)

    Parameters:
        iterable: The iterable whose powerset is to be calculated for
    """
    xs = list(iterable)
    # note we return an iterator rather than a list
    return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))


def mutate_code(code, transformers):
    """
    Transform a base program into a modified program by considering all possible
    mutations from the given list of transformers.

    For example, if we have 2 transformers, possible mutations are (None, 1, 2, 1 and 2).

    Parameters:
        code: Base program string to be modified
        transformers: List of transformers to consider for mutation.
    """
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
