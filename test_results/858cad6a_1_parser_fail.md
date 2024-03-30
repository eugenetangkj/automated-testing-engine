# Test Report

Time: 2024-03-30 07:56:23.839917

### Base Program

```py
def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```

## Test Case 1

### Modified Program

```py
def findPeakElement(nums):
    (left, right) = (0, len(nums) - 1)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findPeakElement(nums):\n    (left, right) = (0, len(nums) - 1)\n    while left < right:\n        mid = left + (right - left) // 2\n        if nums[mid] < nums[mid + 1]:\n            left = mid + 1\n        else:\n            right = mid\n    return left"
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
def findPeakElement(var_0):
    (left, right) = (0, len(var_0) - 1)
    while left < right:
        mid = left + (right - left) // 2
        if var_0[mid] < var_0[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findPeakElement(var_0):\n    (left, right) = (0, len(var_0) - 1)\n    while left < right:\n        mid = left + (right - left) // 2\n        if var_0[mid] < var_0[mid + 1]:\n            left = mid + 1\n        else:\n            right = mid\n    return left"
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
def findPeakElement(nums):
    (left, right) = (0, len(nums) + -1)
    while left < right:
        mid = (right + -left) // 2 + left
        if nums[mid] < nums[1 + mid]:
            left = 1 + mid
        else:
            right = mid
    return left
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findPeakElement(nums):\n    (left, right) = (0, len(nums) + -1)\n    while left < right:\n        mid = (right + -left) // 2 + left\n        if nums[mid] < nums[1 + mid]:\n            left = 1 + mid\n        else:\n            right = mid\n    return left"
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
def findPeakElement(var_1):
    (left, right) = (0, len(var_1) + -1)
    while left < right:
        mid = (right + -left) // 2 + left
        if var_1[mid] < var_1[1 + mid]:
            left = 1 + mid
        else:
            right = mid
    return left
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findPeakElement(var_1):\n    (left, right) = (0, len(var_1) + -1)\n    while left < right:\n        mid = (right + -left) // 2 + left\n        if var_1[mid] < var_1[1 + mid]:\n            left = 1 + mid\n        else:\n            right = mid\n    return left"
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

