# Test Report

Time: 2024-03-30 07:39:22.685617

### Base Program

```py
import random

class RandomizedSet:
    def __init__(self):
        self.index_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        self.index_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        last = self.nums[-1]
        self.index_map[last] = self.index_map[val]
        self.nums[self.index_map[val]] = last

        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]
```

## Test Case 1

### Modified Program

```py
import random

class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        last = self.nums[-1]
        self.index_map[last] = self.index_map[val]
        self.nums[self.index_map[val]] = last
        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import random\n\nclass RandomizedSet:\n\n    def __init__(self):\n        self.index_map = {}\n        self.nums = []\n\n    def insert(self, val: int) -> bool:\n        if val in self.index_map:\n            return False\n        self.index_map[val] = len(self.nums)\n        self.nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self.index_map:\n            return False\n        last = self.nums[-1]\n        self.index_map[last] = self.index_map[val]\n        self.nums[self.index_map[val]] = last\n        self.nums.pop()\n        del self.index_map[val]\n        return True\n\n    def getRandom(self) -> int:\n        return self.nums[random.randint(0, len(self.nums) - 1)]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: No value present\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:382)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:667)\n\tat sg.edu.nus.se.its.parser.ast.nodes.SubscriptOpNode.accept(SubscriptOpNode.java:43)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:319)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ReturnNode.accept(ReturnNode.java:30)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
import random

class RandomizedSet:

    def __init__(var_0):
        var_0.index_map = {}
        var_0.nums = []

    def insert(var_1, var_2: int) -> bool:
        if var_2 in var_1.index_map:
            return False
        var_1.index_map[var_2] = len(var_1.nums)
        var_1.nums.append(var_2)
        return True

    def remove(var_3, var_4: int) -> bool:
        if var_4 not in var_3.index_map:
            return False
        last = var_3.nums[-1]
        var_3.index_map[last] = var_3.index_map[var_4]
        var_3.nums[var_3.index_map[var_4]] = last
        var_3.nums.pop()
        del var_3.index_map[var_4]
        return True

    def getRandom(var_5) -> int:
        return var_5.nums[random.randint(0, len(var_5.nums) - 1)]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import random\n\nclass RandomizedSet:\n\n    def __init__(var_0):\n        var_0.index_map = {}\n        var_0.nums = []\n\n    def insert(var_1, var_2: int) -> bool:\n        if var_2 in var_1.index_map:\n            return False\n        var_1.index_map[var_2] = len(var_1.nums)\n        var_1.nums.append(var_2)\n        return True\n\n    def remove(var_3, var_4: int) -> bool:\n        if var_4 not in var_3.index_map:\n            return False\n        last = var_3.nums[-1]\n        var_3.index_map[last] = var_3.index_map[var_4]\n        var_3.nums[var_3.index_map[var_4]] = last\n        var_3.nums.pop()\n        del var_3.index_map[var_4]\n        return True\n\n    def getRandom(var_5) -> int:\n        return var_5.nums[random.randint(0, len(var_5.nums) - 1)]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: No value present\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:382)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:667)\n\tat sg.edu.nus.se.its.parser.ast.nodes.SubscriptOpNode.accept(SubscriptOpNode.java:43)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:319)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ReturnNode.accept(ReturnNode.java:30)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
import random

class RandomizedSet:

    def __init__(self):
        self.index_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.index_map[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        last = self.nums[-1]
        self.index_map[last] = self.index_map[val]
        self.nums[self.index_map[val]] = last
        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) + -1)]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import random\n\nclass RandomizedSet:\n\n    def __init__(self):\n        self.index_map = {}\n        self.nums = []\n\n    def insert(self, val: int) -> bool:\n        if val in self.index_map:\n            return False\n        self.index_map[val] = len(self.nums)\n        self.nums.append(val)\n        return True\n\n    def remove(self, val: int) -> bool:\n        if val not in self.index_map:\n            return False\n        last = self.nums[-1]\n        self.index_map[last] = self.index_map[val]\n        self.nums[self.index_map[val]] = last\n        self.nums.pop()\n        del self.index_map[val]\n        return True\n\n    def getRandom(self) -> int:\n        return self.nums[random.randint(0, len(self.nums) + -1)]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: No value present\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:382)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:667)\n\tat sg.edu.nus.se.its.parser.ast.nodes.SubscriptOpNode.accept(SubscriptOpNode.java:43)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:319)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ReturnNode.accept(ReturnNode.java:30)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
import random

class RandomizedSet:

    def __init__(var_6):
        var_6.index_map = {}
        var_6.nums = []

    def insert(var_7, var_8: int) -> bool:
        if var_8 in var_7.index_map:
            return False
        var_7.index_map[var_8] = len(var_7.nums)
        var_7.nums.append(var_8)
        return True

    def remove(var_9, var_10: int) -> bool:
        if var_10 not in var_9.index_map:
            return False
        last = var_9.nums[-1]
        var_9.index_map[last] = var_9.index_map[var_10]
        var_9.nums[var_9.index_map[var_10]] = last
        var_9.nums.pop()
        del var_9.index_map[var_10]
        return True

    def getRandom(var_11) -> int:
        return var_11.nums[random.randint(0, len(var_11.nums) + -1)]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import random\n\nclass RandomizedSet:\n\n    def __init__(var_6):\n        var_6.index_map = {}\n        var_6.nums = []\n\n    def insert(var_7, var_8: int) -> bool:\n        if var_8 in var_7.index_map:\n            return False\n        var_7.index_map[var_8] = len(var_7.nums)\n        var_7.nums.append(var_8)\n        return True\n\n    def remove(var_9, var_10: int) -> bool:\n        if var_10 not in var_9.index_map:\n            return False\n        last = var_9.nums[-1]\n        var_9.index_map[last] = var_9.index_map[var_10]\n        var_9.nums[var_9.index_map[var_10]] = last\n        var_9.nums.pop()\n        del var_9.index_map[var_10]\n        return True\n\n    def getRandom(var_11) -> int:\n        return var_11.nums[random.randint(0, len(var_11.nums) + -1)]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: No value present\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:382)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:667)\n\tat sg.edu.nus.se.its.parser.ast.nodes.SubscriptOpNode.accept(SubscriptOpNode.java:43)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:319)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ReturnNode.accept(ReturnNode.java:30)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

