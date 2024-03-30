# Test Report

Time: 2024-03-30 07:56:59.780973

### Base Program

```py
def minCost(n, cuts):
    cuts = [0] + cuts + [n]
    cuts.sort()
    size = len(cuts)
    dp = [[0] * size for _ in range(size)]

    for len in range(2, size):
        for i in range(size - len):
            j = i + len
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

    return dp[0][size - 1]
```

## Test Case 1

### Modified Program

```py
def minCost(n, cuts):
    cuts = [0] + cuts + [n]
    cuts.sort()
    size = len(cuts)
    dp = [[0] * size for _ in range(size)]
    for len in range(2, size):
        for i in range(size - len):
            j = i + len
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
    return dp[0][size - 1]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minCost(n, cuts):\n    cuts = [0] + cuts + [n]\n    cuts.sort()\n    size = len(cuts)\n    dp = [[0] * size for _ in range(size)]\n    for len in range(2, size):\n        for i in range(size - len):\n            j = i + len\n            dp[i][j] = float('inf')\n            for k in range(i + 1, j):\n                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])\n    return dp[0][size - 1]"
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
def minCost(var_0, var_1):
    var_1 = [0] + var_1 + [var_0]
    var_1.sort()
    size = len(var_1)
    dp = [[0] * size for _ in range(size)]
    for len in range(2, size):
        for i in range(size - len):
            j = i + len
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + var_1[j] - var_1[i])
    return dp[0][size - 1]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minCost(var_0, var_1):\n    var_1 = [0] + var_1 + [var_0]\n    var_1.sort()\n    size = len(var_1)\n    dp = [[0] * size for _ in range(size)]\n    for len in range(2, size):\n        for i in range(size - len):\n            j = i + len\n            dp[i][j] = float('inf')\n            for k in range(i + 1, j):\n                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + var_1[j] - var_1[i])\n    return dp[0][size - 1]"
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
def minCost(n, cuts):
    cuts = [0] + [n] + cuts
    cuts.sort()
    size = len(cuts)
    dp = [size * [0] for _ in range(size)]
    for len in range(2, size):
        for i in range(size + -len):
            j = len + i
            dp[i][j] = float('inf')
            for k in range(1 + i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + cuts[j] + dp[k][j] + -cuts[i])
    return dp[0][size + -1]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minCost(n, cuts):\n    cuts = [0] + [n] + cuts\n    cuts.sort()\n    size = len(cuts)\n    dp = [size * [0] for _ in range(size)]\n    for len in range(2, size):\n        for i in range(size + -len):\n            j = len + i\n            dp[i][j] = float('inf')\n            for k in range(1 + i, j):\n                dp[i][j] = min(dp[i][j], dp[i][k] + cuts[j] + dp[k][j] + -cuts[i])\n    return dp[0][size + -1]"
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
def minCost(var_2, var_3):
    var_3 = [0] + [var_2] + var_3
    var_3.sort()
    size = len(var_3)
    dp = [size * [0] for _ in range(size)]
    for len in range(2, size):
        for i in range(size + -len):
            j = len + i
            dp[i][j] = float('inf')
            for k in range(1 + i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + var_3[j] + dp[k][j] + -var_3[i])
    return dp[0][size + -1]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minCost(var_2, var_3):\n    var_3 = [0] + [var_2] + var_3\n    var_3.sort()\n    size = len(var_3)\n    dp = [size * [0] for _ in range(size)]\n    for len in range(2, size):\n        for i in range(size + -len):\n            j = len + i\n            dp[i][j] = float('inf')\n            for k in range(1 + i, j):\n                dp[i][j] = min(dp[i][j], dp[i][k] + var_3[j] + dp[k][j] + -var_3[i])\n    return dp[0][size + -1]"
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

