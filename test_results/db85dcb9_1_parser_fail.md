# Test Report

Time: 2024-03-30 06:13:27.445667

### Base Program

```py
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: TreeNode):
        self.values = set()
        self.recoverTree(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

    def recoverTree(self, node: TreeNode, val: int):
        if node is None:
            return

        node.val = val
        self.values.add(val)

        self.recoverTree(node.left, val * 2 + 1)
        self.recoverTree(node.right, val * 2 + 2)
```

## Test Case 1

### Modified Program

```py
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: TreeNode):
        self.values = set()
        self.recoverTree(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

    def recoverTree(self, node: TreeNode, val: int):
        if node is None:
            return
        node.val = val
        self.values.add(val)
        self.recoverTree(node.left, val * 2 + 1)
        self.recoverTree(node.right, val * 2 + 2)
```

<details>
<summary>parser endpoint: failed ❌</summary>

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Body: 
{
    "language": "py",
    "source_code": "class TreeNode:\n\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\nclass FindElements:\n\n    def __init__(self, root: TreeNode):\n        self.values = set()\n        self.recoverTree(root, 0)\n\n    def find(self, target: int) -> bool:\n        return target in self.values\n\n    def recoverTree(self, node: TreeNode, val: int):\n        if node is None:\n            return\n        node.val = val\n        self.values.add(val)\n        self.recoverTree(node.left, val * 2 + 1)\n        self.recoverTree(node.right, val * 2 + 2)"
}
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.NullPointerException\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:403)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Return_stmtContext.accept(Python3Parser.java:2672)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitFlow_stmt(Python3ParserBaseVisitor.java:174)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Flow_stmtContext.accept(Python3Parser.java:2507)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSmall_stmt(Python3ParserBaseVisitor.java:125)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Small_stmtContext.accept(Python3Parser.java:1829)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSimple_stmt(Python3ParserBaseVisitor.java:118)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Simple_stmtContext.accept(Python3Parser.java:1732)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:516)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$If_stmtContext.accept(Python3Parser.java:3864)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSuite(Python3ParserBaseVisitor.java:356)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$SuiteContext.accept(Python3Parser.java:4463)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitClassdef(Python3ParserBaseVisitor.java:559)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$ClassdefContext.accept(Python3Parser.java:7275)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Request Body: 
```json
{
    "language": "py",
    "source_code": "class TreeNode:\n\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\nclass FindElements:\n\n    def __init__(self, root: TreeNode):\n        self.values = set()\n        self.recoverTree(root, 0)\n\n    def find(self, target: int) -> bool:\n        return target in self.values\n\n    def recoverTree(self, node: TreeNode, val: int):\n        if node is None:\n            return\n        node.val = val\n        self.values.add(val)\n        self.recoverTree(node.left, val * 2 + 1)\n        self.recoverTree(node.right, val * 2 + 2)"
}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
class TreeNode:

    def __init__(var_0, var_1=0, var_2=None, var_3=None):
        var_0.val = var_1
        var_0.left = var_2
        var_0.right = var_3

class FindElements:

    def __init__(var_4, var_5: TreeNode):
        var_4.values = set()
        var_4.recoverTree(var_5, 0)

    def find(var_6, var_7: int) -> bool:
        return var_7 in var_6.values

    def recoverTree(var_8, var_9: TreeNode, var_10: int):
        if var_9 is None:
            return
        var_9.val = var_10
        var_8.values.add(var_10)
        var_8.recoverTree(var_9.left, var_10 * 2 + 1)
        var_8.recoverTree(var_9.right, var_10 * 2 + 2)
```

<details>
<summary>parser endpoint: failed ❌</summary>

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Body: 
{
    "language": "py",
    "source_code": "class TreeNode:\n\n    def __init__(var_0, var_1=0, var_2=None, var_3=None):\n        var_0.val = var_1\n        var_0.left = var_2\n        var_0.right = var_3\n\nclass FindElements:\n\n    def __init__(var_4, var_5: TreeNode):\n        var_4.values = set()\n        var_4.recoverTree(var_5, 0)\n\n    def find(var_6, var_7: int) -> bool:\n        return var_7 in var_6.values\n\n    def recoverTree(var_8, var_9: TreeNode, var_10: int):\n        if var_9 is None:\n            return\n        var_9.val = var_10\n        var_8.values.add(var_10)\n        var_8.recoverTree(var_9.left, var_10 * 2 + 1)\n        var_8.recoverTree(var_9.right, var_10 * 2 + 2)"
}
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.NullPointerException\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:403)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Return_stmtContext.accept(Python3Parser.java:2672)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitFlow_stmt(Python3ParserBaseVisitor.java:174)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Flow_stmtContext.accept(Python3Parser.java:2507)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSmall_stmt(Python3ParserBaseVisitor.java:125)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Small_stmtContext.accept(Python3Parser.java:1829)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSimple_stmt(Python3ParserBaseVisitor.java:118)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Simple_stmtContext.accept(Python3Parser.java:1732)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:516)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$If_stmtContext.accept(Python3Parser.java:3864)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSuite(Python3ParserBaseVisitor.java:356)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$SuiteContext.accept(Python3Parser.java:4463)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitClassdef(Python3ParserBaseVisitor.java:559)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$ClassdefContext.accept(Python3Parser.java:7275)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Request Body: 
```json
{
    "language": "py",
    "source_code": "class TreeNode:\n\n    def __init__(var_0, var_1=0, var_2=None, var_3=None):\n        var_0.val = var_1\n        var_0.left = var_2\n        var_0.right = var_3\n\nclass FindElements:\n\n    def __init__(var_4, var_5: TreeNode):\n        var_4.values = set()\n        var_4.recoverTree(var_5, 0)\n\n    def find(var_6, var_7: int) -> bool:\n        return var_7 in var_6.values\n\n    def recoverTree(var_8, var_9: TreeNode, var_10: int):\n        if var_9 is None:\n            return\n        var_9.val = var_10\n        var_8.values.add(var_10)\n        var_8.recoverTree(var_9.left, var_10 * 2 + 1)\n        var_8.recoverTree(var_9.right, var_10 * 2 + 2)"
}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: TreeNode):
        self.values = set()
        self.recoverTree(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values

    def recoverTree(self, node: TreeNode, val: int):
        if node is None:
            return
        node.val = val
        self.values.add(val)
        self.recoverTree(node.left, 1 + 2 * val)
        self.recoverTree(node.right, 2 + 2 * val)
```

<details>
<summary>parser endpoint: failed ❌</summary>

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Body: 
{
    "language": "py",
    "source_code": "class TreeNode:\n\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\nclass FindElements:\n\n    def __init__(self, root: TreeNode):\n        self.values = set()\n        self.recoverTree(root, 0)\n\n    def find(self, target: int) -> bool:\n        return target in self.values\n\n    def recoverTree(self, node: TreeNode, val: int):\n        if node is None:\n            return\n        node.val = val\n        self.values.add(val)\n        self.recoverTree(node.left, 1 + 2 * val)\n        self.recoverTree(node.right, 2 + 2 * val)"
}
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.NullPointerException\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:403)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Return_stmtContext.accept(Python3Parser.java:2672)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitFlow_stmt(Python3ParserBaseVisitor.java:174)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Flow_stmtContext.accept(Python3Parser.java:2507)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSmall_stmt(Python3ParserBaseVisitor.java:125)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Small_stmtContext.accept(Python3Parser.java:1829)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSimple_stmt(Python3ParserBaseVisitor.java:118)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Simple_stmtContext.accept(Python3Parser.java:1732)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:516)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$If_stmtContext.accept(Python3Parser.java:3864)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSuite(Python3ParserBaseVisitor.java:356)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$SuiteContext.accept(Python3Parser.java:4463)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitClassdef(Python3ParserBaseVisitor.java:559)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$ClassdefContext.accept(Python3Parser.java:7275)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Request Body: 
```json
{
    "language": "py",
    "source_code": "class TreeNode:\n\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\nclass FindElements:\n\n    def __init__(self, root: TreeNode):\n        self.values = set()\n        self.recoverTree(root, 0)\n\n    def find(self, target: int) -> bool:\n        return target in self.values\n\n    def recoverTree(self, node: TreeNode, val: int):\n        if node is None:\n            return\n        node.val = val\n        self.values.add(val)\n        self.recoverTree(node.left, 1 + 2 * val)\n        self.recoverTree(node.right, 2 + 2 * val)"
}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
class TreeNode:

    def __init__(var_11, var_12=0, var_13=None, var_14=None):
        var_11.val = var_12
        var_11.left = var_13
        var_11.right = var_14

class FindElements:

    def __init__(var_15, var_16: TreeNode):
        var_15.values = set()
        var_15.recoverTree(var_16, 0)

    def find(var_17, var_18: int) -> bool:
        return var_18 in var_17.values

    def recoverTree(var_19, var_20: TreeNode, var_21: int):
        if var_20 is None:
            return
        var_20.val = var_21
        var_19.values.add(var_21)
        var_19.recoverTree(var_20.left, 1 + 2 * var_21)
        var_19.recoverTree(var_20.right, 2 + 2 * var_21)
```

<details>
<summary>parser endpoint: failed ❌</summary>

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Body: 
{
    "language": "py",
    "source_code": "class TreeNode:\n\n    def __init__(var_11, var_12=0, var_13=None, var_14=None):\n        var_11.val = var_12\n        var_11.left = var_13\n        var_11.right = var_14\n\nclass FindElements:\n\n    def __init__(var_15, var_16: TreeNode):\n        var_15.values = set()\n        var_15.recoverTree(var_16, 0)\n\n    def find(var_17, var_18: int) -> bool:\n        return var_18 in var_17.values\n\n    def recoverTree(var_19, var_20: TreeNode, var_21: int):\n        if var_20 is None:\n            return\n        var_20.val = var_21\n        var_19.values.add(var_21)\n        var_19.recoverTree(var_20.left, 1 + 2 * var_21)\n        var_19.recoverTree(var_20.right, 2 + 2 * var_21)"
}
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.NullPointerException\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:403)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Return_stmtContext.accept(Python3Parser.java:2672)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitFlow_stmt(Python3ParserBaseVisitor.java:174)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Flow_stmtContext.accept(Python3Parser.java:2507)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSmall_stmt(Python3ParserBaseVisitor.java:125)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Small_stmtContext.accept(Python3Parser.java:1829)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSimple_stmt(Python3ParserBaseVisitor.java:118)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Simple_stmtContext.accept(Python3Parser.java:1732)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:516)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$If_stmtContext.accept(Python3Parser.java:3864)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSuite(Python3ParserBaseVisitor.java:356)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$SuiteContext.accept(Python3Parser.java:4463)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitClassdef(Python3ParserBaseVisitor.java:559)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$ClassdefContext.accept(Python3Parser.java:7275)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Request Body: 
```json
{
    "language": "py",
    "source_code": "class TreeNode:\n\n    def __init__(var_11, var_12=0, var_13=None, var_14=None):\n        var_11.val = var_12\n        var_11.left = var_13\n        var_11.right = var_14\n\nclass FindElements:\n\n    def __init__(var_15, var_16: TreeNode):\n        var_15.values = set()\n        var_15.recoverTree(var_16, 0)\n\n    def find(var_17, var_18: int) -> bool:\n        return var_18 in var_17.values\n\n    def recoverTree(var_19, var_20: TreeNode, var_21: int):\n        if var_20 is None:\n            return\n        var_20.val = var_21\n        var_19.values.add(var_21)\n        var_19.recoverTree(var_20.left, 1 + 2 * var_21)\n        var_19.recoverTree(var_20.right, 2 + 2 * var_21)"
}
```

Actual Output: None

</details>

