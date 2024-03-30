# Test Report

Time: 2024-03-30 07:08:24.344721

### Base Program

```py
def beautifulSubarrays(nums):
    odd = [0] * 20
    even = [0] * 20
    even[0] = 1

    for num in nums:
        parity = bin(num).count('1') % 2
        for i in range(19, -1, -1):
            mask = 1 << i
            if num & mask:
                if parity:
                    odd[i], even[i] = even[i], odd[i]
                odd[i] += 1
            else:
                if not parity:
                    odd[i], even[i] = even[i], odd[i]
                even[i] += 1
            num -= num & mask

    ans = 0
    for i in range(20):
        ans += even[i] * (even[i] - 1) // 2
    return ans
```

## Test Case 1

### Modified Program

```py
def beautifulSubarrays(nums):
    odd = [0] * 20
    even = [0] * 20
    even[0] = 1
    for num in nums:
        parity = bin(num).count('1') % 2
        for i in range(19, -1, -1):
            mask = 1 << i
            if num & mask:
                if parity:
                    (odd[i], even[i]) = (even[i], odd[i])
                odd[i] += 1
            else:
                if not parity:
                    (odd[i], even[i]) = (even[i], odd[i])
                even[i] += 1
            num -= num & mask
    ans = 0
    for i in range(20):
        ans += even[i] * (even[i] - 1) // 2
    return ans
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def beautifulSubarrays(nums):\n    odd = [0] * 20\n    even = [0] * 20\n    even[0] = 1\n    for num in nums:\n        parity = bin(num).count('1') % 2\n        for i in range(19, -1, -1):\n            mask = 1 << i\n            if num & mask:\n                if parity:\n                    (odd[i], even[i]) = (even[i], odd[i])\n                odd[i] += 1\n            else:\n                if not parity:\n                    (odd[i], even[i]) = (even[i], odd[i])\n                even[i] += 1\n            num -= num & mask\n    ans = 0\n    for i in range(20):\n        ans += even[i] * (even[i] - 1) // 2\n    return ans"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:778)\n\tat sg.edu.nus.se.its.parser.ast.nodes.IfNode.accept(IfNode.java:74)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:778)\n\tat sg.edu.nus.se.its.parser.ast.nodes.IfNode.accept(IfNode.java:74)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
def beautifulSubarrays(var_0):
    odd = [0] * 20
    even = [0] * 20
    even[0] = 1
    for num in var_0:
        parity = bin(num).count('1') % 2
        for i in range(19, -1, -1):
            mask = 1 << i
            if num & mask:
                if parity:
                    (odd[i], even[i]) = (even[i], odd[i])
                odd[i] += 1
            else:
                if not parity:
                    (odd[i], even[i]) = (even[i], odd[i])
                even[i] += 1
            num -= num & mask
    ans = 0
    for i in range(20):
        ans += even[i] * (even[i] - 1) // 2
    return ans
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def beautifulSubarrays(var_0):\n    odd = [0] * 20\n    even = [0] * 20\n    even[0] = 1\n    for num in var_0:\n        parity = bin(num).count('1') % 2\n        for i in range(19, -1, -1):\n            mask = 1 << i\n            if num & mask:\n                if parity:\n                    (odd[i], even[i]) = (even[i], odd[i])\n                odd[i] += 1\n            else:\n                if not parity:\n                    (odd[i], even[i]) = (even[i], odd[i])\n                even[i] += 1\n            num -= num & mask\n    ans = 0\n    for i in range(20):\n        ans += even[i] * (even[i] - 1) // 2\n    return ans"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:778)\n\tat sg.edu.nus.se.its.parser.ast.nodes.IfNode.accept(IfNode.java:74)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:778)\n\tat sg.edu.nus.se.its.parser.ast.nodes.IfNode.accept(IfNode.java:74)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
def beautifulSubarrays(nums):
    odd = 20 * [0]
    even = 20 * [0]
    even[0] = 1
    for num in nums:
        parity = bin(num).count('1') % 2
        for i in range(19, -1, -1):
            mask = 1 << i
            if num & mask:
                if parity:
                    (odd[i], even[i]) = (even[i], odd[i])
                odd[i] += 1
            else:
                if not parity:
                    (odd[i], even[i]) = (even[i], odd[i])
                even[i] += 1
            num -= num & mask
    ans = 0
    for i in range(20):
        ans += (even[i] + -1) * even[i] // 2
    return ans
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def beautifulSubarrays(nums):\n    odd = 20 * [0]\n    even = 20 * [0]\n    even[0] = 1\n    for num in nums:\n        parity = bin(num).count('1') % 2\n        for i in range(19, -1, -1):\n            mask = 1 << i\n            if num & mask:\n                if parity:\n                    (odd[i], even[i]) = (even[i], odd[i])\n                odd[i] += 1\n            else:\n                if not parity:\n                    (odd[i], even[i]) = (even[i], odd[i])\n                even[i] += 1\n            num -= num & mask\n    ans = 0\n    for i in range(20):\n        ans += (even[i] + -1) * even[i] // 2\n    return ans"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:778)\n\tat sg.edu.nus.se.its.parser.ast.nodes.IfNode.accept(IfNode.java:74)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:778)\n\tat sg.edu.nus.se.its.parser.ast.nodes.IfNode.accept(IfNode.java:74)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
def beautifulSubarrays(var_1):
    odd = 20 * [0]
    even = 20 * [0]
    even[0] = 1
    for num in var_1:
        parity = bin(num).count('1') % 2
        for i in range(19, -1, -1):
            mask = 1 << i
            if num & mask:
                if parity:
                    (odd[i], even[i]) = (even[i], odd[i])
                odd[i] += 1
            else:
                if not parity:
                    (odd[i], even[i]) = (even[i], odd[i])
                even[i] += 1
            num -= num & mask
    ans = 0
    for i in range(20):
        ans += (even[i] + -1) * even[i] // 2
    return ans
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def beautifulSubarrays(var_1):\n    odd = 20 * [0]\n    even = 20 * [0]\n    even[0] = 1\n    for num in var_1:\n        parity = bin(num).count('1') % 2\n        for i in range(19, -1, -1):\n            mask = 1 << i\n            if num & mask:\n                if parity:\n                    (odd[i], even[i]) = (even[i], odd[i])\n                odd[i] += 1\n            else:\n                if not parity:\n                    (odd[i], even[i]) = (even[i], odd[i])\n                even[i] += 1\n            num -= num & mask\n    ans = 0\n    for i in range(20):\n        ans += (even[i] + -1) * even[i] // 2\n    return ans"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:778)\n\tat sg.edu.nus.se.its.parser.ast.nodes.IfNode.accept(IfNode.java:74)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:778)\n\tat sg.edu.nus.se.its.parser.ast.nodes.IfNode.accept(IfNode.java:74)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:533)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ForNode.accept(ForNode.java:51)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

