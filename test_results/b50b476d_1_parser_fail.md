# Test Report

Time: 2024-03-30 08:57:26.329835

### Base Program

```py
class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random
        
def copyRandomList(head):
    if not head:
        return None

    curr = head
    while curr:
        temp = Node(curr.val)
        temp.next = curr.next
        curr.next = temp
        curr = curr.next.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    orig = head
    copy = head.next
    copy_head = copy

    while orig and copy:
        orig.next = copy.next
        orig = orig.next
        if orig:
            copy.next = orig.next
            copy = copy.next

    return copy_head
```

## Test Case 1

### Modified Program

```py
class Node:

    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None
    curr = head
    while curr:
        temp = Node(curr.val)
        temp.next = curr.next
        curr.next = temp
        curr = curr.next.next
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    orig = head
    copy = head.next
    copy_head = copy
    while orig and copy:
        orig.next = copy.next
        orig = orig.next
        if orig:
            copy.next = orig.next
            copy = copy.next
    return copy_head
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "class Node:\n\n    def __init__(self, val, next=None, random=None):\n        self.val = val\n        self.next = next\n        self.random = random\n\ndef copyRandomList(head):\n    if not head:\n        return None\n    curr = head\n    while curr:\n        temp = Node(curr.val)\n        temp.next = curr.next\n        curr.next = temp\n        curr = curr.next.next\n    curr = head\n    while curr:\n        if curr.random:\n            curr.next.random = curr.random.next\n        curr = curr.next.next\n    orig = head\n    copy = head.next\n    copy_head = copy\n    while orig and copy:\n        orig.next = copy.next\n        orig = orig.next\n        if orig:\n            copy.next = orig.next\n            copy = copy.next\n    return copy_head"
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
class Node:

    def __init__(var_0, var_1, var_2=None, var_3=None):
        var_0.val = var_1
        var_0.next = var_2
        var_0.random = var_3

def copyRandomList(var_4):
    if not var_4:
        return None
    curr = var_4
    while curr:
        temp = Node(curr.val)
        temp.next = curr.next
        curr.next = temp
        curr = curr.next.next
    curr = var_4
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    orig = var_4
    copy = var_4.next
    copy_head = copy
    while orig and copy:
        orig.next = copy.next
        orig = orig.next
        if orig:
            copy.next = orig.next
            copy = copy.next
    return copy_head
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "class Node:\n\n    def __init__(var_0, var_1, var_2=None, var_3=None):\n        var_0.val = var_1\n        var_0.next = var_2\n        var_0.random = var_3\n\ndef copyRandomList(var_4):\n    if not var_4:\n        return None\n    curr = var_4\n    while curr:\n        temp = Node(curr.val)\n        temp.next = curr.next\n        curr.next = temp\n        curr = curr.next.next\n    curr = var_4\n    while curr:\n        if curr.random:\n            curr.next.random = curr.random.next\n        curr = curr.next.next\n    orig = var_4\n    copy = var_4.next\n    copy_head = copy\n    while orig and copy:\n        orig.next = copy.next\n        orig = orig.next\n        if orig:\n            copy.next = orig.next\n            copy = copy.next\n    return copy_head"
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
class Node:

    def __init__(var_5, var_6, var_7=None, var_8=None):
        var_5.val = var_6
        var_5.next = var_7
        var_5.random = var_8

def copyRandomList(var_9):
    if not var_9:
        return None
    curr = var_9
    while curr:
        temp = Node(curr.val)
        temp.next = curr.next
        curr.next = temp
        curr = curr.next.next
    curr = var_9
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    orig = var_9
    copy = var_9.next
    copy_head = copy
    while orig and copy:
        orig.next = copy.next
        orig = orig.next
        if orig:
            copy.next = orig.next
            copy = copy.next
    return copy_head
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "class Node:\n\n    def __init__(var_5, var_6, var_7=None, var_8=None):\n        var_5.val = var_6\n        var_5.next = var_7\n        var_5.random = var_8\n\ndef copyRandomList(var_9):\n    if not var_9:\n        return None\n    curr = var_9\n    while curr:\n        temp = Node(curr.val)\n        temp.next = curr.next\n        curr.next = temp\n        curr = curr.next.next\n    curr = var_9\n    while curr:\n        if curr.random:\n            curr.next.random = curr.random.next\n        curr = curr.next.next\n    orig = var_9\n    copy = var_9.next\n    copy_head = copy\n    while orig and copy:\n        orig.next = copy.next\n        orig = orig.next\n        if orig:\n            copy.next = orig.next\n            copy = copy.next\n    return copy_head"
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
