# Test Report

Time: 2024-03-30 07:23:04.664682

### Base Program

```py
def minWastedSpace(nums, k):
    n = len(nums)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        total = 0
        for j in range(i, 0, -1):
            total += nums[j - 1]
            for l in range(k):
                dp[i][l + 1] = min(dp[i][l + 1], dp[j - 1][l] + (i - j + 1) * nums[j - 1] - total)

    return min(dp[n])
```

## Test Case 1

### Modified Program

```py
def minWastedSpace(nums, k):
    n = len(nums)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        total = 0
        for j in range(i, 0, -1):
            total += nums[j - 1]
            for l in range(k):
                dp[i][l + 1] = min(dp[i][l + 1], dp[j - 1][l] + (i - j + 1) * nums[j - 1] - total)
    return min(dp[n])
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minWastedSpace(nums, k):\n    n = len(nums)\n    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]\n    dp[0][0] = 0\n    for i in range(1, n + 1):\n        total = 0\n        for j in range(i, 0, -1):\n            total += nums[j - 1]\n            for l in range(k):\n                dp[i][l + 1] = min(dp[i][l + 1], dp[j - 1][l] + (i - j + 1) * nums[j - 1] - total)\n    return min(dp[n])"
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
def minWastedSpace(var_0, var_1):
    n = len(var_0)
    dp = [[float('inf')] * (var_1 + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        total = 0
        for j in range(i, 0, -1):
            total += var_0[j - 1]
            for l in range(var_1):
                dp[i][l + 1] = min(dp[i][l + 1], dp[j - 1][l] + (i - j + 1) * var_0[j - 1] - total)
    return min(dp[n])
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minWastedSpace(var_0, var_1):\n    n = len(var_0)\n    dp = [[float('inf')] * (var_1 + 1) for _ in range(n + 1)]\n    dp[0][0] = 0\n    for i in range(1, n + 1):\n        total = 0\n        for j in range(i, 0, -1):\n            total += var_0[j - 1]\n            for l in range(var_1):\n                dp[i][l + 1] = min(dp[i][l + 1], dp[j - 1][l] + (i - j + 1) * var_0[j - 1] - total)\n    return min(dp[n])"
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
def minWastedSpace(nums, k):
    n = len(nums)
    dp = [(1 + k) * [float('inf')] for _ in range(1 + n)]
    dp[0][0] = 0
    for i in range(1, 1 + n):
        total = 0
        for j in range(i, 0, -1):
            total += nums[j + -1]
            for l in range(k):
                dp[i][1 + l] = min(dp[i][1 + l], nums[j + -1] * (1 + (i + -j)) + dp[j + -1][l] + -total)
    return min(dp[n])
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minWastedSpace(nums, k):\n    n = len(nums)\n    dp = [(1 + k) * [float('inf')] for _ in range(1 + n)]\n    dp[0][0] = 0\n    for i in range(1, 1 + n):\n        total = 0\n        for j in range(i, 0, -1):\n            total += nums[j + -1]\n            for l in range(k):\n                dp[i][1 + l] = min(dp[i][1 + l], nums[j + -1] * (1 + (i + -j)) + dp[j + -1][l] + -total)\n    return min(dp[n])"
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
def minWastedSpace(var_2, var_3):
    n = len(var_2)
    dp = [(1 + var_3) * [float('inf')] for _ in range(1 + n)]
    dp[0][0] = 0
    for i in range(1, 1 + n):
        total = 0
        for j in range(i, 0, -1):
            total += var_2[j + -1]
            for l in range(var_3):
                dp[i][1 + l] = min(dp[i][1 + l], var_2[j + -1] * (1 + (i + -j)) + dp[j + -1][l] + -total)
    return min(dp[n])
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minWastedSpace(var_2, var_3):\n    n = len(var_2)\n    dp = [(1 + var_3) * [float('inf')] for _ in range(1 + n)]\n    dp[0][0] = 0\n    for i in range(1, 1 + n):\n        total = 0\n        for j in range(i, 0, -1):\n            total += var_2[j + -1]\n            for l in range(var_3):\n                dp[i][1 + l] = min(dp[i][1 + l], var_2[j + -1] * (1 + (i + -j)) + dp[j + -1][l] + -total)\n    return min(dp[n])"
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

