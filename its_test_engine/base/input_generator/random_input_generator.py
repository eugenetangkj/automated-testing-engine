import random
from its_test_engine.base.input_generator.base_input_generator import BaseInputGenerator


class RandomInputGenerator(BaseInputGenerator):
    def _generate_random_integer(self, min_value=-1e9, max_value=1e9):
        return random.randint(min_value, max_value)

    def _generate_random_float(self, min_value=-1e5, max_value=1e5):
        return random.uniform(min_value, max_value)

    def _generate_random_string(self, length=10):
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for _ in range(length))

    def _generate_random_boolean(self):
        return random.choice([True, False])

    def generate_inputs(self, types: list[str], no_of_inputs: int):
        results = []
        for _ in range(no_of_inputs):
            inputs = []
            for t in types:
                if t == "int":
                    inputs.append(self._generate_random_integer())
                elif t == "float":
                    inputs.append(self._generate_random_float())
                elif t == "str":
                    inputs.append(self._generate_random_string())
                elif t == "bool":
                    inputs.append(self._generate_random_boolean())
                elif t == "any":
                    inputs.append(
                        random.choice(
                            [
                                self._generate_random_integer(),
                                self._generate_random_float(),
                                self._generate_random_string(),
                                self._generate_random_boolean(),
                            ]
                        )
                    )
                elif t == "List[int]":
                    inputs.append([self._generate_random_integer() for _ in range(10)])
                elif t == "List[float]":
                    inputs.append([self._generate_random_float() for _ in range(10)])
                elif t == "List[str]":
                    inputs.append([self._generate_random_string() for _ in range(10)])
                elif t == "List[bool]":
                    inputs.append([self._generate_random_boolean() for _ in range(10)])

            results.append(inputs)
        return results
