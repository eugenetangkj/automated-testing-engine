# Test Report

Time: 2024-03-30 07:12:46.358885

### Base Program

```py
def kBigIndices(nums, k):
    n = len(nums)
    left, right = [0] * n, [0] * n

    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            left[i] = left[i - 1] + 1

        j = n - i - 1
        if nums[j] < nums[j + 1]:
            right[j] = right[j + 1] + 1

    return sum(1 for i in range(n) if left[i] >= k and right[i] >= k)
```

## Test Case 1

### Modified Program

```py
def kBigIndices(nums, k):
    n = len(nums)
    (left, right) = ([0] * n, [0] * n)
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            left[i] = left[i - 1] + 1
        j = n - i - 1
        if nums[j] < nums[j + 1]:
            right[j] = right[j + 1] + 1
    return sum((1 for i in range(n) if left[i] >= k and right[i] >= k))
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def kBigIndices(nums, k):\n    n = len(nums)\n    (left, right) = ([0] * n, [0] * n)\n    for i in range(1, n):\n        if nums[i] > nums[i - 1]:\n            left[i] = left[i - 1] + 1\n        j = n - i - 1\n        if nums[j] < nums[j + 1]:\n            right[j] = right[j + 1] + 1\n    return sum((1 for i in range(n) if left[i] >= k and right[i] >= k))"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
def kBigIndices(var_0, var_1):
    n = len(var_0)
    (left, right) = ([0] * n, [0] * n)
    for i in range(1, n):
        if var_0[i] > var_0[i - 1]:
            left[i] = left[i - 1] + 1
        j = n - i - 1
        if var_0[j] < var_0[j + 1]:
            right[j] = right[j + 1] + 1
    return sum((1 for i in range(n) if left[i] >= var_1 and right[i] >= var_1))
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def kBigIndices(var_0, var_1):\n    n = len(var_0)\n    (left, right) = ([0] * n, [0] * n)\n    for i in range(1, n):\n        if var_0[i] > var_0[i - 1]:\n            left[i] = left[i - 1] + 1\n        j = n - i - 1\n        if var_0[j] < var_0[j + 1]:\n            right[j] = right[j + 1] + 1\n    return sum((1 for i in range(n) if left[i] >= var_1 and right[i] >= var_1))"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
def kBigIndices(nums, k):
    n = len(nums)
    (left, right) = (n * [0], n * [0])
    for i in range(1, n):
        if nums[i] > nums[i + -1]:
            left[i] = 1 + left[i + -1]
        j = n + -i + -1
        if nums[j] < nums[1 + j]:
            right[j] = 1 + right[1 + j]
    return sum((1 for i in range(n) if left[i] >= k and right[i] >= k))
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def kBigIndices(nums, k):\n    n = len(nums)\n    (left, right) = (n * [0], n * [0])\n    for i in range(1, n):\n        if nums[i] > nums[i + -1]:\n            left[i] = 1 + left[i + -1]\n        j = n + -i + -1\n        if nums[j] < nums[1 + j]:\n            right[j] = 1 + right[1 + j]\n    return sum((1 for i in range(n) if left[i] >= k and right[i] >= k))"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
def kBigIndices(var_2, var_3):
    n = len(var_2)
    (left, right) = (n * [0], n * [0])
    for i in range(1, n):
        if var_2[i] > var_2[i + -1]:
            left[i] = 1 + left[i + -1]
        j = n + -i + -1
        if var_2[j] < var_2[1 + j]:
            right[j] = 1 + right[1 + j]
    return sum((1 for i in range(n) if left[i] >= var_3 and right[i] >= var_3))
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def kBigIndices(var_2, var_3):\n    n = len(var_2)\n    (left, right) = (n * [0], n * [0])\n    for i in range(1, n):\n        if var_2[i] > var_2[i + -1]:\n            left[i] = 1 + left[i + -1]\n        j = n + -i + -1\n        if var_2[j] < var_2[1 + j]:\n            right[j] = 1 + right[1 + j]\n    return sum((1 for i in range(n) if left[i] >= var_3 and right[i] >= var_3))"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

