# Test Report

Time: 2024-03-30 08:41:04.727255

### Base Program

```py
def stoneGame(stones):
    n = len(stones)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(stones[j] - dp[i][j - 1], stones[i] - dp[i + 1][j])
    
    return dp[0][n - 1]
```

## Test Case 1

### Modified Program

```py
def stoneGame(stones):
    n = len(stones)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(stones[j] - dp[i][j - 1], stones[i] - dp[i + 1][j])
    return dp[0][n - 1]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def stoneGame(stones):\n    n = len(stones)\n    dp = [[0] * n for _ in range(n)]\n    for i in range(n - 1, -1, -1):\n        for j in range(i + 1, n):\n            dp[i][j] = max(stones[j] - dp[i][j - 1], stones[i] - dp[i + 1][j])\n    return dp[0][n - 1]"
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
def stoneGame(var_0):
    n = len(var_0)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = max(var_0[j] - dp[i][j - 1], var_0[i] - dp[i + 1][j])
    return dp[0][n - 1]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def stoneGame(var_0):\n    n = len(var_0)\n    dp = [[0] * n for _ in range(n)]\n    for i in range(n - 1, -1, -1):\n        for j in range(i + 1, n):\n            dp[i][j] = max(var_0[j] - dp[i][j - 1], var_0[i] - dp[i + 1][j])\n    return dp[0][n - 1]"
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
def stoneGame(stones):
    n = len(stones)
    dp = [n * [0] for _ in range(n)]
    for i in range(n + -1, -1, -1):
        for j in range(1 + i, n):
            dp[i][j] = max(stones[j] + -dp[i][j + -1], stones[i] + -dp[1 + i][j])
    return dp[0][n + -1]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def stoneGame(stones):\n    n = len(stones)\n    dp = [n * [0] for _ in range(n)]\n    for i in range(n + -1, -1, -1):\n        for j in range(1 + i, n):\n            dp[i][j] = max(stones[j] + -dp[i][j + -1], stones[i] + -dp[1 + i][j])\n    return dp[0][n + -1]"
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
def stoneGame(var_1):
    n = len(var_1)
    dp = [n * [0] for _ in range(n)]
    for i in range(n + -1, -1, -1):
        for j in range(1 + i, n):
            dp[i][j] = max(var_1[j] + -dp[i][j + -1], var_1[i] + -dp[1 + i][j])
    return dp[0][n + -1]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def stoneGame(var_1):\n    n = len(var_1)\n    dp = [n * [0] for _ in range(n)]\n    for i in range(n + -1, -1, -1):\n        for j in range(1 + i, n):\n            dp[i][j] = max(var_1[j] + -dp[i][j + -1], var_1[i] + -dp[1 + i][j])\n    return dp[0][n + -1]"
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

