"""
    Generate random c programs using csmith
"""
import os
import subprocess
from .base_program_generator import BaseProgramGenerator

class CsmithProgramGenerator(BaseProgramGenerator):
    """
    This class generates a random C program using the Csmith open source library found at
    https://github.com/csmith-project/csmith
    
    """

    def __init__(self):
        """
        Initialisation method for a CsmithProgramGenerator instance
        """

    def generate_test_case(self, language="c", constraints=None):
        """
        Generate a random c program using Csmith
        """
        if language != "c":
            raise ValueError("Csmith only supports c programs")

        # Run csmith binary
        cwd = os.path.dirname(os.path.realpath(__file__)) + "/csmith"
        result = subprocess.run(["./csmith"], capture_output=True, cwd=cwd, text=True, check=False)

        if result.returncode != 0:
            raise ValueError("Csmith failed to generate a program")

        return result.stdout
