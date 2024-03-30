# Test Report

Time: 2024-03-30 08:52:59.526279

### Base Program

```py
def splitArray(nums, m):
    left, right = max(nums), sum(nums)

    while left < right:
        mid = (left + right) // 2
        count, cur_sum = 1, 0
        for num in nums:
            cur_sum += num
            if cur_sum > mid:
                cur_sum = num
                count += 1

        if count > m:
            left = mid + 1
        else:
            right = mid

    return left
```

## Test Case 1

### Modified Program

```py
def splitArray(nums, m):
    (left, right) = (max(nums), sum(nums))
    while left < right:
        mid = (left + right) // 2
        (count, cur_sum) = (1, 0)
        for num in nums:
            cur_sum += num
            if cur_sum > mid:
                cur_sum = num
                count += 1
        if count > m:
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
    "source_code": "def splitArray(nums, m):\n    (left, right) = (max(nums), sum(nums))\n    while left < right:\n        mid = (left + right) // 2\n        (count, cur_sum) = (1, 0)\n        for num in nums:\n            cur_sum += num\n            if cur_sum > mid:\n                cur_sum = num\n                count += 1\n        if count > m:\n            left = mid + 1\n        else:\n            right = mid\n    return left"
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
def splitArray(var_0, var_1):
    (left, right) = (max(var_0), sum(var_0))
    while left < right:
        mid = (left + right) // 2
        (count, cur_sum) = (1, 0)
        for num in var_0:
            cur_sum += num
            if cur_sum > mid:
                cur_sum = num
                count += 1
        if count > var_1:
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
    "source_code": "def splitArray(var_0, var_1):\n    (left, right) = (max(var_0), sum(var_0))\n    while left < right:\n        mid = (left + right) // 2\n        (count, cur_sum) = (1, 0)\n        for num in var_0:\n            cur_sum += num\n            if cur_sum > mid:\n                cur_sum = num\n                count += 1\n        if count > var_1:\n            left = mid + 1\n        else:\n            right = mid\n    return left"
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
def splitArray(nums, m):
    (left, right) = (max(nums), sum(nums))
    while left < right:
        mid = (right + left) // 2
        (count, cur_sum) = (1, 0)
        for num in nums:
            cur_sum += num
            if cur_sum > mid:
                cur_sum = num
                count += 1
        if count > m:
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
    "source_code": "def splitArray(nums, m):\n    (left, right) = (max(nums), sum(nums))\n    while left < right:\n        mid = (right + left) // 2\n        (count, cur_sum) = (1, 0)\n        for num in nums:\n            cur_sum += num\n            if cur_sum > mid:\n                cur_sum = num\n                count += 1\n        if count > m:\n            left = 1 + mid\n        else:\n            right = mid\n    return left"
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
def splitArray(var_2, var_3):
    (left, right) = (max(var_2), sum(var_2))
    while left < right:
        mid = (right + left) // 2
        (count, cur_sum) = (1, 0)
        for num in var_2:
            cur_sum += num
            if cur_sum > mid:
                cur_sum = num
                count += 1
        if count > var_3:
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
    "source_code": "def splitArray(var_2, var_3):\n    (left, right) = (max(var_2), sum(var_2))\n    while left < right:\n        mid = (right + left) // 2\n        (count, cur_sum) = (1, 0)\n        for num in var_2:\n            cur_sum += num\n            if cur_sum > mid:\n                cur_sum = num\n                count += 1\n        if count > var_3:\n            left = 1 + mid\n        else:\n            right = mid\n    return left"
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

