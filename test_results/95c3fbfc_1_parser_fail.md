# Test Report

Time: 2024-03-30 06:27:38.424956

### Base Program

```py
def countSquareFreeSubsets(nums):
    from collections import Counter
    counter = Counter(nums)
    MOD = 10**9 + 7

    dp = [[0] * 1001 for _ in range(61)]
    dp[0][0] = 1
    idx = 0
    for num, freq in counter.items():
        idx += 1
        for sq in range(61):
            for ns in range(1001 - freq):
                dp[idx][ns + freq] += dp[idx - 1][ns] * ((1 << freq) - 1) % MOD
                dp[idx][ns + freq] %= MOD
                dp[idx][ns] += dp[idx - 1][ns]
                dp[idx][ns] %= MOD

                if (sq // num) % 2 == 1:
                    dp[idx][ns + freq] -= dp[idx - 1][ns] * ((1 << (freq - 1)) - 1) % MOD
                    if dp[idx][ns + freq] < 0:
                        dp[idx][ns + freq] += MOD
    return dp[idx][0]
```

## Test Case 1

### Modified Program

```py
def countSquareFreeSubsets(nums):
    from collections import Counter
    counter = Counter(nums)
    MOD = 10 ** 9 + 7
    dp = [[0] * 1001 for _ in range(61)]
    dp[0][0] = 1
    idx = 0
    for (num, freq) in counter.items():
        idx += 1
        for sq in range(61):
            for ns in range(1001 - freq):
                dp[idx][ns + freq] += dp[idx - 1][ns] * ((1 << freq) - 1) % MOD
                dp[idx][ns + freq] %= MOD
                dp[idx][ns] += dp[idx - 1][ns]
                dp[idx][ns] %= MOD
                if sq // num % 2 == 1:
                    dp[idx][ns + freq] -= dp[idx - 1][ns] * ((1 << freq - 1) - 1) % MOD
                    if dp[idx][ns + freq] < 0:
                        dp[idx][ns + freq] += MOD
    return dp[idx][0]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def countSquareFreeSubsets(nums):\n    from collections import Counter\n    counter = Counter(nums)\n    MOD = 10 ** 9 + 7\n    dp = [[0] * 1001 for _ in range(61)]\n    dp[0][0] = 1\n    idx = 0\n    for (num, freq) in counter.items():\n        idx += 1\n        for sq in range(61):\n            for ns in range(1001 - freq):\n                dp[idx][ns + freq] += dp[idx - 1][ns] * ((1 << freq) - 1) % MOD\n                dp[idx][ns + freq] %= MOD\n                dp[idx][ns] += dp[idx - 1][ns]\n                dp[idx][ns] %= MOD\n                if sq // num % 2 == 1:\n                    dp[idx][ns + freq] -= dp[idx - 1][ns] * ((1 << freq - 1) - 1) % MOD\n                    if dp[idx][ns + freq] < 0:\n                        dp[idx][ns + freq] += MOD\n    return dp[idx][0]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (num,freq)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
def countSquareFreeSubsets(var_0):
    from collections import Counter
    counter = Counter(var_0)
    MOD = 10 ** 9 + 7
    dp = [[0] * 1001 for _ in range(61)]
    dp[0][0] = 1
    idx = 0
    for (num, freq) in counter.items():
        idx += 1
        for sq in range(61):
            for ns in range(1001 - freq):
                dp[idx][ns + freq] += dp[idx - 1][ns] * ((1 << freq) - 1) % MOD
                dp[idx][ns + freq] %= MOD
                dp[idx][ns] += dp[idx - 1][ns]
                dp[idx][ns] %= MOD
                if sq // num % 2 == 1:
                    dp[idx][ns + freq] -= dp[idx - 1][ns] * ((1 << freq - 1) - 1) % MOD
                    if dp[idx][ns + freq] < 0:
                        dp[idx][ns + freq] += MOD
    return dp[idx][0]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def countSquareFreeSubsets(var_0):\n    from collections import Counter\n    counter = Counter(var_0)\n    MOD = 10 ** 9 + 7\n    dp = [[0] * 1001 for _ in range(61)]\n    dp[0][0] = 1\n    idx = 0\n    for (num, freq) in counter.items():\n        idx += 1\n        for sq in range(61):\n            for ns in range(1001 - freq):\n                dp[idx][ns + freq] += dp[idx - 1][ns] * ((1 << freq) - 1) % MOD\n                dp[idx][ns + freq] %= MOD\n                dp[idx][ns] += dp[idx - 1][ns]\n                dp[idx][ns] %= MOD\n                if sq // num % 2 == 1:\n                    dp[idx][ns + freq] -= dp[idx - 1][ns] * ((1 << freq - 1) - 1) % MOD\n                    if dp[idx][ns + freq] < 0:\n                        dp[idx][ns + freq] += MOD\n    return dp[idx][0]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (num,freq)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
def countSquareFreeSubsets(nums):
    from collections import Counter
    counter = Counter(nums)
    MOD = 7 + 10 ** 9
    dp = [1001 * [0] for _ in range(61)]
    dp[0][0] = 1
    idx = 0
    for (num, freq) in counter.items():
        idx += 1
        for sq in range(61):
            for ns in range(1001 + -freq):
                dp[idx][freq + ns] += ((1 << freq) + -1) * dp[idx + -1][ns] % MOD
                dp[idx][freq + ns] %= MOD
                dp[idx][ns] += dp[idx + -1][ns]
                dp[idx][ns] %= MOD
                if sq // num % 2 == 1:
                    dp[idx][freq + ns] -= ((1 << freq + -1) + -1) * dp[idx + -1][ns] % MOD
                    if dp[idx][freq + ns] < 0:
                        dp[idx][freq + ns] += MOD
    return dp[idx][0]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def countSquareFreeSubsets(nums):\n    from collections import Counter\n    counter = Counter(nums)\n    MOD = 7 + 10 ** 9\n    dp = [1001 * [0] for _ in range(61)]\n    dp[0][0] = 1\n    idx = 0\n    for (num, freq) in counter.items():\n        idx += 1\n        for sq in range(61):\n            for ns in range(1001 + -freq):\n                dp[idx][freq + ns] += ((1 << freq) + -1) * dp[idx + -1][ns] % MOD\n                dp[idx][freq + ns] %= MOD\n                dp[idx][ns] += dp[idx + -1][ns]\n                dp[idx][ns] %= MOD\n                if sq // num % 2 == 1:\n                    dp[idx][freq + ns] -= ((1 << freq + -1) + -1) * dp[idx + -1][ns] % MOD\n                    if dp[idx][freq + ns] < 0:\n                        dp[idx][freq + ns] += MOD\n    return dp[idx][0]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (num,freq)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
def countSquareFreeSubsets(var_1):
    from collections import Counter
    counter = Counter(var_1)
    MOD = 7 + 10 ** 9
    dp = [1001 * [0] for _ in range(61)]
    dp[0][0] = 1
    idx = 0
    for (num, freq) in counter.items():
        idx += 1
        for sq in range(61):
            for ns in range(1001 + -freq):
                dp[idx][freq + ns] += ((1 << freq) + -1) * dp[idx + -1][ns] % MOD
                dp[idx][freq + ns] %= MOD
                dp[idx][ns] += dp[idx + -1][ns]
                dp[idx][ns] %= MOD
                if sq // num % 2 == 1:
                    dp[idx][freq + ns] -= ((1 << freq + -1) + -1) * dp[idx + -1][ns] % MOD
                    if dp[idx][freq + ns] < 0:
                        dp[idx][freq + ns] += MOD
    return dp[idx][0]
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def countSquareFreeSubsets(var_1):\n    from collections import Counter\n    counter = Counter(var_1)\n    MOD = 7 + 10 ** 9\n    dp = [1001 * [0] for _ in range(61)]\n    dp[0][0] = 1\n    idx = 0\n    for (num, freq) in counter.items():\n        idx += 1\n        for sq in range(61):\n            for ns in range(1001 + -freq):\n                dp[idx][freq + ns] += ((1 << freq) + -1) * dp[idx + -1][ns] % MOD\n                dp[idx][freq + ns] %= MOD\n                dp[idx][ns] += dp[idx + -1][ns]\n                dp[idx][ns] %= MOD\n                if sq // num % 2 == 1:\n                    dp[idx][freq + ns] -= ((1 << freq + -1) + -1) * dp[idx + -1][ns] % MOD\n                    if dp[idx][freq + ns] < 0:\n                        dp[idx][freq + ns] += MOD\n    return dp[idx][0]"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (num,freq)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

