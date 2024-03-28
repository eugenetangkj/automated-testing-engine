'''
    This indicates the status of a test case
'''
from enum import Enum

class TypeOfTestResult(Enum):
    """
    This class provides the enumeration values for the status of a test case, where it is either
    'PASS' or 'FAIL'.
    
    """
    PASS = "PASS"
    FAIL = "FAIL"