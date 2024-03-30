# Test Report

Time: 2024-03-30 08:31:03.121499

### Base Program

```py
from collections import defaultdict
import heapq

class MyCalendarThree:

    def __init__(self):
        self.timeline = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1
        ongoing, k = 0, 0
        for value in self.timeline.values():
            k = max(k, ongoing + value)
            ongoing += value
        return k
```

## Test Case 1

### Modified Program

```py
from collections import defaultdict
import heapq

class MyCalendarThree:

    def __init__(self):
        self.timeline = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1
        (ongoing, k) = (0, 0)
        for value in self.timeline.values():
            k = max(k, ongoing + value)
            ongoing += value
        return k
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\nimport heapq\n\nclass MyCalendarThree:\n\n    def __init__(self):\n        self.timeline = defaultdict(int)\n\n    def book(self, start: int, end: int) -> int:\n        self.timeline[start] += 1\n        self.timeline[end] -= 1\n        (ongoing, k) = (0, 0)\n        for value in self.timeline.values():\n            k = max(k, ongoing + value)\n            ongoing += value\n        return k"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: No value present\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:382)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:667)\n\tat sg.edu.nus.se.its.parser.ast.nodes.SubscriptOpNode.accept(SubscriptOpNode.java:43)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitBinaryOp(PyAstVisitor.java:869)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:354)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AugAssignNode.accept(AugAssignNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:172)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
from collections import defaultdict
import heapq

class MyCalendarThree:

    def __init__(var_0):
        var_0.timeline = defaultdict(int)

    def book(var_1, var_2: int, var_3: int) -> int:
        var_1.timeline[var_2] += 1
        var_1.timeline[var_3] -= 1
        (ongoing, k) = (0, 0)
        for value in var_1.timeline.values():
            k = max(k, ongoing + value)
            ongoing += value
        return k
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\nimport heapq\n\nclass MyCalendarThree:\n\n    def __init__(var_0):\n        var_0.timeline = defaultdict(int)\n\n    def book(var_1, var_2: int, var_3: int) -> int:\n        var_1.timeline[var_2] += 1\n        var_1.timeline[var_3] -= 1\n        (ongoing, k) = (0, 0)\n        for value in var_1.timeline.values():\n            k = max(k, ongoing + value)\n            ongoing += value\n        return k"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: No value present\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:382)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:667)\n\tat sg.edu.nus.se.its.parser.ast.nodes.SubscriptOpNode.accept(SubscriptOpNode.java:43)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitBinaryOp(PyAstVisitor.java:869)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:354)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AugAssignNode.accept(AugAssignNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:172)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
from collections import defaultdict
import heapq

class MyCalendarThree:

    def __init__(self):
        self.timeline = defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1
        (ongoing, k) = (0, 0)
        for value in self.timeline.values():
            k = max(k, value + ongoing)
            ongoing += value
        return k
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\nimport heapq\n\nclass MyCalendarThree:\n\n    def __init__(self):\n        self.timeline = defaultdict(int)\n\n    def book(self, start: int, end: int) -> int:\n        self.timeline[start] += 1\n        self.timeline[end] -= 1\n        (ongoing, k) = (0, 0)\n        for value in self.timeline.values():\n            k = max(k, value + ongoing)\n            ongoing += value\n        return k"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: No value present\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:382)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:667)\n\tat sg.edu.nus.se.its.parser.ast.nodes.SubscriptOpNode.accept(SubscriptOpNode.java:43)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitBinaryOp(PyAstVisitor.java:869)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:354)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AugAssignNode.accept(AugAssignNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:172)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
from collections import defaultdict
import heapq

class MyCalendarThree:

    def __init__(var_4):
        var_4.timeline = defaultdict(int)

    def book(var_5, var_6: int, var_7: int) -> int:
        var_5.timeline[var_6] += 1
        var_5.timeline[var_7] -= 1
        (ongoing, k) = (0, 0)
        for value in var_5.timeline.values():
            k = max(k, value + ongoing)
            ongoing += value
        return k
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\nimport heapq\n\nclass MyCalendarThree:\n\n    def __init__(var_4):\n        var_4.timeline = defaultdict(int)\n\n    def book(var_5, var_6: int, var_7: int) -> int:\n        var_5.timeline[var_6] += 1\n        var_5.timeline[var_7] -= 1\n        (ongoing, k) = (0, 0)\n        for value in var_5.timeline.values():\n            k = max(k, value + ongoing)\n            ongoing += value\n        return k"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: No value present\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:382)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:667)\n\tat sg.edu.nus.se.its.parser.ast.nodes.SubscriptOpNode.accept(SubscriptOpNode.java:43)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitBinaryOp(PyAstVisitor.java:869)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:354)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AugAssignNode.accept(AugAssignNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:172)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>
