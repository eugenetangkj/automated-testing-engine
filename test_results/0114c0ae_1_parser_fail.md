# Test Report

Time: 2024-03-30 07:38:15.425546

### Base Program

```py
def findLength(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maxLength = 0

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                maxLength = max(maxLength, dp[i][j])

    return maxLength
```

## Test Case 1

### Modified Program

```py
def findLength(nums1, nums2):
    (m, n) = (len(nums1), len(nums2))
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maxLength = 0
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                maxLength = max(maxLength, dp[i][j])
    return maxLength
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findLength(nums1, nums2):\n    (m, n) = (len(nums1), len(nums2))\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    maxLength = 0\n    for i in range(m - 1, -1, -1):\n        for j in range(n - 1, -1, -1):\n            if nums1[i] == nums2[j]:\n                dp[i][j] = dp[i + 1][j + 1] + 1\n                maxLength = max(maxLength, dp[i][j])\n    return maxLength"
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
def findLength(var_0, var_1):
    (m, n) = (len(var_0), len(var_1))
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    maxLength = 0
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if var_0[i] == var_1[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
                maxLength = max(maxLength, dp[i][j])
    return maxLength
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findLength(var_0, var_1):\n    (m, n) = (len(var_0), len(var_1))\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    maxLength = 0\n    for i in range(m - 1, -1, -1):\n        for j in range(n - 1, -1, -1):\n            if var_0[i] == var_1[j]:\n                dp[i][j] = dp[i + 1][j + 1] + 1\n                maxLength = max(maxLength, dp[i][j])\n    return maxLength"
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
def findLength(nums1, nums2):
    (m, n) = (len(nums1), len(nums2))
    dp = [(1 + n) * [0] for _ in range(1 + m)]
    maxLength = 0
    for i in range(m + -1, -1, -1):
        for j in range(n + -1, -1, -1):
            if nums1[i] == nums2[j]:
                dp[i][j] = 1 + dp[1 + i][1 + j]
                maxLength = max(maxLength, dp[i][j])
    return maxLength
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findLength(nums1, nums2):\n    (m, n) = (len(nums1), len(nums2))\n    dp = [(1 + n) * [0] for _ in range(1 + m)]\n    maxLength = 0\n    for i in range(m + -1, -1, -1):\n        for j in range(n + -1, -1, -1):\n            if nums1[i] == nums2[j]:\n                dp[i][j] = 1 + dp[1 + i][1 + j]\n                maxLength = max(maxLength, dp[i][j])\n    return maxLength"
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
def findLength(var_2, var_3):
    (m, n) = (len(var_2), len(var_3))
    dp = [(1 + n) * [0] for _ in range(1 + m)]
    maxLength = 0
    for i in range(m + -1, -1, -1):
        for j in range(n + -1, -1, -1):
            if var_2[i] == var_3[j]:
                dp[i][j] = 1 + dp[1 + i][1 + j]
                maxLength = max(maxLength, dp[i][j])
    return maxLength
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findLength(var_2, var_3):\n    (m, n) = (len(var_2), len(var_3))\n    dp = [(1 + n) * [0] for _ in range(1 + m)]\n    maxLength = 0\n    for i in range(m + -1, -1, -1):\n        for j in range(n + -1, -1, -1):\n            if var_2[i] == var_3[j]:\n                dp[i][j] = 1 + dp[1 + i][1 + j]\n                maxLength = max(maxLength, dp[i][j])\n    return maxLength"
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

