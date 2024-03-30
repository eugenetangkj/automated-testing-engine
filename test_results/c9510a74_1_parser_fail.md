# Test Report

Time: 2024-03-30 08:30:37.161934

### Base Program

```py
def min_time_to_eat_grains(hens, grains):
    hens.sort()
    grains.sort()
    left, right = 0, 10**9

    while left < right:
        mid = left + (right - left) // 2
        can_eat = True
        i = 0

        for grain in grains:
            if i >= len(hens):
                can_eat = False
                break

            while i < len(hens) and hens[i] < grain - mid:
                i += 1

            if i >= len(hens) or hens[i] > grain + mid:
                can_eat = False
                break

            i += 1

        if can_eat:
            right = mid
        else:
            left = mid + 1

    return left
```

## Test Case 1

### Modified Program

```py
def min_time_to_eat_grains(hens, grains):
    hens.sort()
    grains.sort()
    (left, right) = (0, 10 ** 9)
    while left < right:
        mid = left + (right - left) // 2
        can_eat = True
        i = 0
        for grain in grains:
            if i >= len(hens):
                can_eat = False
                break
            while i < len(hens) and hens[i] < grain - mid:
                i += 1
            if i >= len(hens) or hens[i] > grain + mid:
                can_eat = False
                break
            i += 1
        if can_eat:
            right = mid
        else:
            left = mid + 1
    return left
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_time_to_eat_grains(hens, grains):\n    hens.sort()\n    grains.sort()\n    (left, right) = (0, 10 ** 9)\n    while left < right:\n        mid = left + (right - left) // 2\n        can_eat = True\n        i = 0\n        for grain in grains:\n            if i >= len(hens):\n                can_eat = False\n                break\n            while i < len(hens) and hens[i] < grain - mid:\n                i += 1\n            if i >= len(hens) or hens[i] > grain + mid:\n                can_eat = False\n                break\n            i += 1\n        if can_eat:\n            right = mid\n        else:\n            left = mid + 1\n    return left"
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
def min_time_to_eat_grains(var_0, var_1):
    var_0.sort()
    var_1.sort()
    (left, right) = (0, 10 ** 9)
    while left < right:
        mid = left + (right - left) // 2
        can_eat = True
        i = 0
        for grain in var_1:
            if i >= len(var_0):
                can_eat = False
                break
            while i < len(var_0) and var_0[i] < grain - mid:
                i += 1
            if i >= len(var_0) or var_0[i] > grain + mid:
                can_eat = False
                break
            i += 1
        if can_eat:
            right = mid
        else:
            left = mid + 1
    return left
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_time_to_eat_grains(var_0, var_1):\n    var_0.sort()\n    var_1.sort()\n    (left, right) = (0, 10 ** 9)\n    while left < right:\n        mid = left + (right - left) // 2\n        can_eat = True\n        i = 0\n        for grain in var_1:\n            if i >= len(var_0):\n                can_eat = False\n                break\n            while i < len(var_0) and var_0[i] < grain - mid:\n                i += 1\n            if i >= len(var_0) or var_0[i] > grain + mid:\n                can_eat = False\n                break\n            i += 1\n        if can_eat:\n            right = mid\n        else:\n            left = mid + 1\n    return left"
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
def min_time_to_eat_grains(hens, grains):
    hens.sort()
    grains.sort()
    (left, right) = (0, 10 ** 9)
    while left < right:
        mid = (right + -left) // 2 + left
        can_eat = True
        i = 0
        for grain in grains:
            if i >= len(hens):
                can_eat = False
                break
            while i < len(hens) and hens[i] < grain + -mid:
                i += 1
            if i >= len(hens) or hens[i] > mid + grain:
                can_eat = False
                break
            i += 1
        if can_eat:
            right = mid
        else:
            left = 1 + mid
    return left
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_time_to_eat_grains(hens, grains):\n    hens.sort()\n    grains.sort()\n    (left, right) = (0, 10 ** 9)\n    while left < right:\n        mid = (right + -left) // 2 + left\n        can_eat = True\n        i = 0\n        for grain in grains:\n            if i >= len(hens):\n                can_eat = False\n                break\n            while i < len(hens) and hens[i] < grain + -mid:\n                i += 1\n            if i >= len(hens) or hens[i] > mid + grain:\n                can_eat = False\n                break\n            i += 1\n        if can_eat:\n            right = mid\n        else:\n            left = 1 + mid\n    return left"
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
def min_time_to_eat_grains(var_2, var_3):
    var_2.sort()
    var_3.sort()
    (left, right) = (0, 10 ** 9)
    while left < right:
        mid = (right + -left) // 2 + left
        can_eat = True
        i = 0
        for grain in var_3:
            if i >= len(var_2):
                can_eat = False
                break
            while i < len(var_2) and var_2[i] < grain + -mid:
                i += 1
            if i >= len(var_2) or var_2[i] > mid + grain:
                can_eat = False
                break
            i += 1
        if can_eat:
            right = mid
        else:
            left = 1 + mid
    return left
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_time_to_eat_grains(var_2, var_3):\n    var_2.sort()\n    var_3.sort()\n    (left, right) = (0, 10 ** 9)\n    while left < right:\n        mid = (right + -left) // 2 + left\n        can_eat = True\n        i = 0\n        for grain in var_3:\n            if i >= len(var_2):\n                can_eat = False\n                break\n            while i < len(var_2) and var_2[i] < grain + -mid:\n                i += 1\n            if i >= len(var_2) or var_2[i] > mid + grain:\n                can_eat = False\n                break\n            i += 1\n        if can_eat:\n            right = mid\n        else:\n            left = 1 + mid\n    return left"
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

