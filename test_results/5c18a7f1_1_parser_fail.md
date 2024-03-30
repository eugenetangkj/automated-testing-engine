# Test Report

Time: 2024-03-30 07:08:38.245215

### Base Program

```py
def getMoneyAmount(n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n + 1):
            min_cost = float("inf")
            for k in range(i, j):
                cost = k + max(dp[i][k - 1], dp[k + 1][j])
                min_cost = min(min_cost, cost)
            dp[i][j] = min_cost
    return dp[1][n]
```

## Test Case 1

### Modified Program

```py
def getMoneyAmount(n: int) -> int:
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n + 1):
            min_cost = float('inf')
            for k in range(i, j):
                cost = k + max(dp[i][k - 1], dp[k + 1][j])
                min_cost = min(min_cost, cost)
            dp[i][j] = min_cost
    return dp[1][n]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def getMoneyAmount(n: int) -> int:\n    dp = [[0] * (n + 1) for _ in range(n + 1)]\n    for i in range(n - 1, 0, -1):\n        for j in range(i + 1, n + 1):\n            min_cost = float('inf')\n            for k in range(i, j):\n                cost = k + max(dp[i][k - 1], dp[k + 1][j])\n                min_cost = min(min_cost, cost)\n            dp[i][j] = min_cost\n    return dp[1][n]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
def getMoneyAmount(var_0: int) -> int:
    dp = [[0] * (var_0 + 1) for _ in range(var_0 + 1)]
    for i in range(var_0 - 1, 0, -1):
        for j in range(i + 1, var_0 + 1):
            min_cost = float('inf')
            for k in range(i, j):
                cost = k + max(dp[i][k - 1], dp[k + 1][j])
                min_cost = min(min_cost, cost)
            dp[i][j] = min_cost
    return dp[1][var_0]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def getMoneyAmount(var_0: int) -> int:\n    dp = [[0] * (var_0 + 1) for _ in range(var_0 + 1)]\n    for i in range(var_0 - 1, 0, -1):\n        for j in range(i + 1, var_0 + 1):\n            min_cost = float('inf')\n            for k in range(i, j):\n                cost = k + max(dp[i][k - 1], dp[k + 1][j])\n                min_cost = min(min_cost, cost)\n            dp[i][j] = min_cost\n    return dp[1][var_0]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
def getMoneyAmount(n: int) -> int:
    dp = [(1 + n) * [0] for _ in range(1 + n)]
    for i in range(n + -1, 0, -1):
        for j in range(1 + i, 1 + n):
            min_cost = float('inf')
            for k in range(i, j):
                cost = max(dp[i][k + -1], dp[1 + k][j]) + k
                min_cost = min(min_cost, cost)
            dp[i][j] = min_cost
    return dp[1][n]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def getMoneyAmount(n: int) -> int:\n    dp = [(1 + n) * [0] for _ in range(1 + n)]\n    for i in range(n + -1, 0, -1):\n        for j in range(1 + i, 1 + n):\n            min_cost = float('inf')\n            for k in range(i, j):\n                cost = max(dp[i][k + -1], dp[1 + k][j]) + k\n                min_cost = min(min_cost, cost)\n            dp[i][j] = min_cost\n    return dp[1][n]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
def getMoneyAmount(var_1: int) -> int:
    dp = [(1 + var_1) * [0] for _ in range(1 + var_1)]
    for i in range(var_1 + -1, 0, -1):
        for j in range(1 + i, 1 + var_1):
            min_cost = float('inf')
            for k in range(i, j):
                cost = max(dp[i][k + -1], dp[1 + k][j]) + k
                min_cost = min(min_cost, cost)
            dp[i][j] = min_cost
    return dp[1][var_1]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def getMoneyAmount(var_1: int) -> int:\n    dp = [(1 + var_1) * [0] for _ in range(1 + var_1)]\n    for i in range(var_1 + -1, 0, -1):\n        for j in range(1 + i, 1 + var_1):\n            min_cost = float('inf')\n            for k in range(i, j):\n                cost = max(dp[i][k + -1], dp[1 + k][j]) + k\n                min_cost = min(min_cost, cost)\n            dp[i][j] = min_cost\n    return dp[1][var_1]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

