# Test Report

Time: 2024-03-30 07:34:58.090756

### Base Program

```py
def arraysIntersection(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    result = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            result.append(arr1[i])
            i, j, k = i + 1, j + 1, k + 1
        else:
            if arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
                i += 1
            elif arr2[j] <= arr3[k]:
                j += 1
            else:
                k += 1
    return result
```

## Test Case 1

### Modified Program

```py
def arraysIntersection(arr1, arr2, arr3):
    (i, j, k) = (0, 0, 0)
    result = []
    while i < len(arr1) and j < len(arr2) and (k < len(arr3)):
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            result.append(arr1[i])
            (i, j, k) = (i + 1, j + 1, k + 1)
        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i += 1
        elif arr2[j] <= arr3[k]:
            j += 1
        else:
            k += 1
    return result
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def arraysIntersection(arr1, arr2, arr3):\n    (i, j, k) = (0, 0, 0)\n    result = []\n    while i < len(arr1) and j < len(arr2) and (k < len(arr3)):\n        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:\n            result.append(arr1[i])\n            (i, j, k) = (i + 1, j + 1, k + 1)\n        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:\n            i += 1\n        elif arr2[j] <= arr3[k]:\n            j += 1\n        else:\n            k += 1\n    return result"
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
def arraysIntersection(var_0, var_1, var_2):
    (i, j, k) = (0, 0, 0)
    result = []
    while i < len(var_0) and j < len(var_1) and (k < len(var_2)):
        if var_0[i] == var_1[j] and var_1[j] == var_2[k]:
            result.append(var_0[i])
            (i, j, k) = (i + 1, j + 1, k + 1)
        elif var_0[i] <= var_1[j] and var_0[i] <= var_2[k]:
            i += 1
        elif var_1[j] <= var_2[k]:
            j += 1
        else:
            k += 1
    return result
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def arraysIntersection(var_0, var_1, var_2):\n    (i, j, k) = (0, 0, 0)\n    result = []\n    while i < len(var_0) and j < len(var_1) and (k < len(var_2)):\n        if var_0[i] == var_1[j] and var_1[j] == var_2[k]:\n            result.append(var_0[i])\n            (i, j, k) = (i + 1, j + 1, k + 1)\n        elif var_0[i] <= var_1[j] and var_0[i] <= var_2[k]:\n            i += 1\n        elif var_1[j] <= var_2[k]:\n            j += 1\n        else:\n            k += 1\n    return result"
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
def arraysIntersection(arr1, arr2, arr3):
    (i, j, k) = (0, 0, 0)
    result = []
    while i < len(arr1) and j < len(arr2) and (k < len(arr3)):
        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
            result.append(arr1[i])
            (i, j, k) = (1 + i, 1 + j, 1 + k)
        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i += 1
        elif arr2[j] <= arr3[k]:
            j += 1
        else:
            k += 1
    return result
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def arraysIntersection(arr1, arr2, arr3):\n    (i, j, k) = (0, 0, 0)\n    result = []\n    while i < len(arr1) and j < len(arr2) and (k < len(arr3)):\n        if arr1[i] == arr2[j] and arr2[j] == arr3[k]:\n            result.append(arr1[i])\n            (i, j, k) = (1 + i, 1 + j, 1 + k)\n        elif arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:\n            i += 1\n        elif arr2[j] <= arr3[k]:\n            j += 1\n        else:\n            k += 1\n    return result"
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
def arraysIntersection(var_3, var_4, var_5):
    (i, j, k) = (0, 0, 0)
    result = []
    while i < len(var_3) and j < len(var_4) and (k < len(var_5)):
        if var_3[i] == var_4[j] and var_4[j] == var_5[k]:
            result.append(var_3[i])
            (i, j, k) = (1 + i, 1 + j, 1 + k)
        elif var_3[i] <= var_4[j] and var_3[i] <= var_5[k]:
            i += 1
        elif var_4[j] <= var_5[k]:
            j += 1
        else:
            k += 1
    return result
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def arraysIntersection(var_3, var_4, var_5):\n    (i, j, k) = (0, 0, 0)\n    result = []\n    while i < len(var_3) and j < len(var_4) and (k < len(var_5)):\n        if var_3[i] == var_4[j] and var_4[j] == var_5[k]:\n            result.append(var_3[i])\n            (i, j, k) = (1 + i, 1 + j, 1 + k)\n        elif var_3[i] <= var_4[j] and var_3[i] <= var_5[k]:\n            i += 1\n        elif var_4[j] <= var_5[k]:\n            j += 1\n        else:\n            k += 1\n    return result"
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

