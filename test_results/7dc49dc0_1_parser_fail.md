# Test Report

Time: 2024-03-30 08:33:49.329069

### Base Program

```py
def findKthPositive(arr, k):
    i, num = 0, 1
    while k > 0:
        if i < len(arr) and arr[i] == num:
            i += 1
        else:
            k -= 1
        num += 1
    return num - 1
```

## Test Case 1

### Modified Program

```py
def findKthPositive(arr, k):
    (i, num) = (0, 1)
    while k > 0:
        if i < len(arr) and arr[i] == num:
            i += 1
        else:
            k -= 1
        num += 1
    return num - 1
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findKthPositive(arr, k):\n    (i, num) = (0, 1)\n    while k > 0:\n        if i < len(arr) and arr[i] == num:\n            i += 1\n        else:\n            k -= 1\n        num += 1\n    return num - 1"
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
def findKthPositive(var_0, var_1):
    (i, num) = (0, 1)
    while var_1 > 0:
        if i < len(var_0) and var_0[i] == num:
            i += 1
        else:
            var_1 -= 1
        num += 1
    return num - 1
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findKthPositive(var_0, var_1):\n    (i, num) = (0, 1)\n    while var_1 > 0:\n        if i < len(var_0) and var_0[i] == num:\n            i += 1\n        else:\n            var_1 -= 1\n        num += 1\n    return num - 1"
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
def findKthPositive(arr, k):
    (i, num) = (0, 1)
    while k > 0:
        if i < len(arr) and arr[i] == num:
            i += 1
        else:
            k -= 1
        num += 1
    return num + -1
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findKthPositive(arr, k):\n    (i, num) = (0, 1)\n    while k > 0:\n        if i < len(arr) and arr[i] == num:\n            i += 1\n        else:\n            k -= 1\n        num += 1\n    return num + -1"
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
def findKthPositive(var_2, var_3):
    (i, num) = (0, 1)
    while var_3 > 0:
        if i < len(var_2) and var_2[i] == num:
            i += 1
        else:
            var_3 -= 1
        num += 1
    return num + -1
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findKthPositive(var_2, var_3):\n    (i, num) = (0, 1)\n    while var_3 > 0:\n        if i < len(var_2) and var_2[i] == num:\n            i += 1\n        else:\n            var_3 -= 1\n        num += 1\n    return num + -1"
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

