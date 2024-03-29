"""
    This indicates the type of relation.
"""

from enum import Enum


class TypeOfMetamorphicRelation(Enum):
    """
    This class provides the enumeration values for the type of metamorphic relation. It helps
    the ITS API comparator to determine the output, where we are comparing them to be equal
    to be successful or unequal to be successful.

    """

    EQUIVALENT = "EQUIVALENT"
    VARIANT = "VARIANT"


class TestResult(Enum):
    """
    This class provides the enumeration values for the status of a test case, where it is either
    'PASS' or 'FAIL'.

    """

    PASS = "PASS"
    FAIL = "FAIL"


class Language(Enum):
    """
    This class provides the enumeration values for the language of the program, where it is either
    'PYTHON' or 'JAVA'.

    """

    PYTHON = "py"
    C = "c"
