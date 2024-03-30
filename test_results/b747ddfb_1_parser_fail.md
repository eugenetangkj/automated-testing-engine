# Test Report

Time: 2024-03-30 06:27:09.259803

### Base Program

```py
import heapq

def mincost_to_hire_workers(quality, wage, k):
    workers = sorted((w / q, q) for w, q in zip(wage, quality))
    total_quality = 0
    max_heap = []
    result = float("inf")

    for ratio, q in workers:
        heapq.heappush(max_heap, -q)
        total_quality += q

        if len(max_heap) > k:
            total_quality += heapq.heappop(max_heap)

        if len(max_heap) == k:
            result = min(result, total_quality * ratio)

    return result
```

## Test Case 1

### Modified Program

```py
import heapq

def mincost_to_hire_workers(quality, wage, k):
    workers = sorted(((w / q, q) for (w, q) in zip(wage, quality)))
    total_quality = 0
    max_heap = []
    result = float('inf')
    for (ratio, q) in workers:
        heapq.heappush(max_heap, -q)
        total_quality += q
        if len(max_heap) > k:
            total_quality += heapq.heappop(max_heap)
        if len(max_heap) == k:
            result = min(result, total_quality * ratio)
    return result
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import heapq\n\ndef mincost_to_hire_workers(quality, wage, k):\n    workers = sorted(((w / q, q) for (w, q) in zip(wage, quality)))\n    total_quality = 0\n    max_heap = []\n    result = float('inf')\n    for (ratio, q) in workers:\n        heapq.heappush(max_heap, -q)\n        total_quality += q\n        if len(max_heap) > k:\n            total_quality += heapq.heappop(max_heap)\n        if len(max_heap) == k:\n            result = min(result, total_quality * ratio)\n    return result"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (ratio,q)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
import heapq

def mincost_to_hire_workers(var_0, var_1, var_2):
    workers = sorted(((w / q, q) for (w, q) in zip(var_1, var_0)))
    total_quality = 0
    max_heap = []
    result = float('inf')
    for (ratio, q) in workers:
        heapq.heappush(max_heap, -q)
        total_quality += q
        if len(max_heap) > var_2:
            total_quality += heapq.heappop(max_heap)
        if len(max_heap) == var_2:
            result = min(result, total_quality * ratio)
    return result
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import heapq\n\ndef mincost_to_hire_workers(var_0, var_1, var_2):\n    workers = sorted(((w / q, q) for (w, q) in zip(var_1, var_0)))\n    total_quality = 0\n    max_heap = []\n    result = float('inf')\n    for (ratio, q) in workers:\n        heapq.heappush(max_heap, -q)\n        total_quality += q\n        if len(max_heap) > var_2:\n            total_quality += heapq.heappop(max_heap)\n        if len(max_heap) == var_2:\n            result = min(result, total_quality * ratio)\n    return result"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (ratio,q)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
import heapq

def mincost_to_hire_workers(quality, wage, k):
    workers = sorted(((w / q, q) for (w, q) in zip(wage, quality)))
    total_quality = 0
    max_heap = []
    result = float('inf')
    for (ratio, q) in workers:
        heapq.heappush(max_heap, -q)
        total_quality += q
        if len(max_heap) > k:
            total_quality += heapq.heappop(max_heap)
        if len(max_heap) == k:
            result = min(result, ratio * total_quality)
    return result
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import heapq\n\ndef mincost_to_hire_workers(quality, wage, k):\n    workers = sorted(((w / q, q) for (w, q) in zip(wage, quality)))\n    total_quality = 0\n    max_heap = []\n    result = float('inf')\n    for (ratio, q) in workers:\n        heapq.heappush(max_heap, -q)\n        total_quality += q\n        if len(max_heap) > k:\n            total_quality += heapq.heappop(max_heap)\n        if len(max_heap) == k:\n            result = min(result, ratio * total_quality)\n    return result"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (ratio,q)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
import heapq

def mincost_to_hire_workers(var_3, var_4, var_5):
    workers = sorted(((w / q, q) for (w, q) in zip(var_4, var_3)))
    total_quality = 0
    max_heap = []
    result = float('inf')
    for (ratio, q) in workers:
        heapq.heappush(max_heap, -q)
        total_quality += q
        if len(max_heap) > var_5:
            total_quality += heapq.heappop(max_heap)
        if len(max_heap) == var_5:
            result = min(result, ratio * total_quality)
    return result
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "import heapq\n\ndef mincost_to_hire_workers(var_3, var_4, var_5):\n    workers = sorted(((w / q, q) for (w, q) in zip(var_4, var_3)))\n    total_quality = 0\n    max_heap = []\n    result = float('inf')\n    for (ratio, q) in workers:\n        heapq.heappush(max_heap, -q)\n        total_quality += q\n        if len(max_heap) > var_5:\n            total_quality += heapq.heappop(max_heap)\n        if len(max_heap) == var_5:\n            result = min(result, ratio * total_quality)\n    return result"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (ratio,q)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

