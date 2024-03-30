# Test Report

Time: 2024-03-30 07:23:14.001057

### Base Program

```py
def maxDistance(nums1, nums2):
    i, j, maxDist = 0, 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            i += 1
        else:
            maxDist = max(maxDist, j - i)
            j += 1
    return maxDist
```

## Test Case 1

### Modified Program

```py
def maxDistance(nums1, nums2):
    (i, j, maxDist) = (0, 0, 0)
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            i += 1
        else:
            maxDist = max(maxDist, j - i)
            j += 1
    return maxDist
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxDistance(nums1, nums2):\n    (i, j, maxDist) = (0, 0, 0)\n    while i < len(nums1) and j < len(nums2):\n        if nums1[i] > nums2[j]:\n            i += 1\n        else:\n            maxDist = max(maxDist, j - i)\n            j += 1\n    return maxDist"
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
def maxDistance(var_0, var_1):
    (i, j, maxDist) = (0, 0, 0)
    while i < len(var_0) and j < len(var_1):
        if var_0[i] > var_1[j]:
            i += 1
        else:
            maxDist = max(maxDist, j - i)
            j += 1
    return maxDist
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxDistance(var_0, var_1):\n    (i, j, maxDist) = (0, 0, 0)\n    while i < len(var_0) and j < len(var_1):\n        if var_0[i] > var_1[j]:\n            i += 1\n        else:\n            maxDist = max(maxDist, j - i)\n            j += 1\n    return maxDist"
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
def maxDistance(nums1, nums2):
    (i, j, maxDist) = (0, 0, 0)
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            i += 1
        else:
            maxDist = max(maxDist, j + -i)
            j += 1
    return maxDist
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxDistance(nums1, nums2):\n    (i, j, maxDist) = (0, 0, 0)\n    while i < len(nums1) and j < len(nums2):\n        if nums1[i] > nums2[j]:\n            i += 1\n        else:\n            maxDist = max(maxDist, j + -i)\n            j += 1\n    return maxDist"
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
def maxDistance(var_2, var_3):
    (i, j, maxDist) = (0, 0, 0)
    while i < len(var_2) and j < len(var_3):
        if var_2[i] > var_3[j]:
            i += 1
        else:
            maxDist = max(maxDist, j + -i)
            j += 1
    return maxDist
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def maxDistance(var_2, var_3):\n    (i, j, maxDist) = (0, 0, 0)\n    while i < len(var_2) and j < len(var_3):\n        if var_2[i] > var_3[j]:\n            i += 1\n        else:\n            maxDist = max(maxDist, j + -i)\n            j += 1\n    return maxDist"
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

