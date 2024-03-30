# Test Report

Time: 2024-03-30 08:05:05.333055

### Base Program

```py
from collections import defaultdict
from random import randint

class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.positions = defaultdict(list)
        for i, num in enumerate(arr):
            self.positions[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            randomIndex = randint(left, right)
            num = self.arr[randomIndex]
            lb = self.lower_bound(self.positions[num], left)
            ub = self.upper_bound(self.positions[num], right)
            if ub - lb >= threshold:
                return num
        return -1

    def lower_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

    def upper_bound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l
```

## Test Case 1

### Modified Program

```py
from collections import defaultdict
from random import randint

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.positions = defaultdict(list)
        for (i, num) in enumerate(arr):
            self.positions[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            randomIndex = randint(left, right)
            num = self.arr[randomIndex]
            lb = self.lower_bound(self.positions[num], left)
            ub = self.upper_bound(self.positions[num], right)
            if ub - lb >= threshold:
                return num
        return -1

    def lower_bound(self, nums, target):
        (l, r) = (0, len(nums))
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

    def upper_bound(self, nums, target):
        (l, r) = (0, len(nums))
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
        return l
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\nfrom random import randint\n\nclass MajorityChecker:\n\n    def __init__(self, arr: List[int]):\n        self.arr = arr\n        self.positions = defaultdict(list)\n        for (i, num) in enumerate(arr):\n            self.positions[num].append(i)\n\n    def query(self, left: int, right: int, threshold: int) -> int:\n        for _ in range(20):\n            randomIndex = randint(left, right)\n            num = self.arr[randomIndex]\n            lb = self.lower_bound(self.positions[num], left)\n            ub = self.upper_bound(self.positions[num], right)\n            if ub - lb >= threshold:\n                return num\n        return -1\n\n    def lower_bound(self, nums, target):\n        (l, r) = (0, len(nums))\n        while l < r:\n            mid = (l + r) // 2\n            if nums[mid] < target:\n                l = mid + 1\n            else:\n                r = mid\n        return l\n\n    def upper_bound(self, nums, target):\n        (l, r) = (0, len(nums))\n        while l < r:\n            mid = (l + r) // 2\n            if nums[mid] <= target:\n                l = mid + 1\n            else:\n                r = mid\n        return l"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (i,num)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSuite(Python3ParserBaseVisitor.java:356)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$SuiteContext.accept(Python3Parser.java:4463)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitClassdef(Python3ParserBaseVisitor.java:559)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$ClassdefContext.accept(Python3Parser.java:7275)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
from collections import defaultdict
from random import randint

class MajorityChecker:

    def __init__(var_0, var_1: List[int]):
        var_0.arr = var_1
        var_0.positions = defaultdict(list)
        for (i, num) in enumerate(var_1):
            var_0.positions[num].append(i)

    def query(var_2, var_3: int, var_4: int, var_5: int) -> int:
        for _ in range(20):
            randomIndex = randint(var_3, var_4)
            num = var_2.arr[randomIndex]
            lb = var_2.lower_bound(var_2.positions[num], var_3)
            ub = var_2.upper_bound(var_2.positions[num], var_4)
            if ub - lb >= var_5:
                return num
        return -1

    def lower_bound(var_6, var_7, var_8):
        (l, r) = (0, len(var_7))
        while l < r:
            mid = (l + r) // 2
            if var_7[mid] < var_8:
                l = mid + 1
            else:
                r = mid
        return l

    def upper_bound(var_9, var_10, var_11):
        (l, r) = (0, len(var_10))
        while l < r:
            mid = (l + r) // 2
            if var_10[mid] <= var_11:
                l = mid + 1
            else:
                r = mid
        return l
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\nfrom random import randint\n\nclass MajorityChecker:\n\n    def __init__(var_0, var_1: List[int]):\n        var_0.arr = var_1\n        var_0.positions = defaultdict(list)\n        for (i, num) in enumerate(var_1):\n            var_0.positions[num].append(i)\n\n    def query(var_2, var_3: int, var_4: int, var_5: int) -> int:\n        for _ in range(20):\n            randomIndex = randint(var_3, var_4)\n            num = var_2.arr[randomIndex]\n            lb = var_2.lower_bound(var_2.positions[num], var_3)\n            ub = var_2.upper_bound(var_2.positions[num], var_4)\n            if ub - lb >= var_5:\n                return num\n        return -1\n\n    def lower_bound(var_6, var_7, var_8):\n        (l, r) = (0, len(var_7))\n        while l < r:\n            mid = (l + r) // 2\n            if var_7[mid] < var_8:\n                l = mid + 1\n            else:\n                r = mid\n        return l\n\n    def upper_bound(var_9, var_10, var_11):\n        (l, r) = (0, len(var_10))\n        while l < r:\n            mid = (l + r) // 2\n            if var_10[mid] <= var_11:\n                l = mid + 1\n            else:\n                r = mid\n        return l"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (i,num)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSuite(Python3ParserBaseVisitor.java:356)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$SuiteContext.accept(Python3Parser.java:4463)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitClassdef(Python3ParserBaseVisitor.java:559)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$ClassdefContext.accept(Python3Parser.java:7275)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
from collections import defaultdict
from random import randint

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.positions = defaultdict(list)
        for (i, num) in enumerate(arr):
            self.positions[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(20):
            randomIndex = randint(left, right)
            num = self.arr[randomIndex]
            lb = self.lower_bound(self.positions[num], left)
            ub = self.upper_bound(self.positions[num], right)
            if ub + -lb >= threshold:
                return num
        return -1

    def lower_bound(self, nums, target):
        (l, r) = (0, len(nums))
        while l < r:
            mid = (r + l) // 2
            if nums[mid] < target:
                l = 1 + mid
            else:
                r = mid
        return l

    def upper_bound(self, nums, target):
        (l, r) = (0, len(nums))
        while l < r:
            mid = (r + l) // 2
            if nums[mid] <= target:
                l = 1 + mid
            else:
                r = mid
        return l
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\nfrom random import randint\n\nclass MajorityChecker:\n\n    def __init__(self, arr: List[int]):\n        self.arr = arr\n        self.positions = defaultdict(list)\n        for (i, num) in enumerate(arr):\n            self.positions[num].append(i)\n\n    def query(self, left: int, right: int, threshold: int) -> int:\n        for _ in range(20):\n            randomIndex = randint(left, right)\n            num = self.arr[randomIndex]\n            lb = self.lower_bound(self.positions[num], left)\n            ub = self.upper_bound(self.positions[num], right)\n            if ub + -lb >= threshold:\n                return num\n        return -1\n\n    def lower_bound(self, nums, target):\n        (l, r) = (0, len(nums))\n        while l < r:\n            mid = (r + l) // 2\n            if nums[mid] < target:\n                l = 1 + mid\n            else:\n                r = mid\n        return l\n\n    def upper_bound(self, nums, target):\n        (l, r) = (0, len(nums))\n        while l < r:\n            mid = (r + l) // 2\n            if nums[mid] <= target:\n                l = 1 + mid\n            else:\n                r = mid\n        return l"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (i,num)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSuite(Python3ParserBaseVisitor.java:356)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$SuiteContext.accept(Python3Parser.java:4463)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitClassdef(Python3ParserBaseVisitor.java:559)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$ClassdefContext.accept(Python3Parser.java:7275)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
from collections import defaultdict
from random import randint

class MajorityChecker:

    def __init__(var_12, var_13: List[int]):
        var_12.arr = var_13
        var_12.positions = defaultdict(list)
        for (i, num) in enumerate(var_13):
            var_12.positions[num].append(i)

    def query(var_14, var_15: int, var_16: int, var_17: int) -> int:
        for _ in range(20):
            randomIndex = randint(var_15, var_16)
            num = var_14.arr[randomIndex]
            lb = var_14.lower_bound(var_14.positions[num], var_15)
            ub = var_14.upper_bound(var_14.positions[num], var_16)
            if ub + -lb >= var_17:
                return num
        return -1

    def lower_bound(var_18, var_19, var_20):
        (l, r) = (0, len(var_19))
        while l < r:
            mid = (r + l) // 2
            if var_19[mid] < var_20:
                l = 1 + mid
            else:
                r = mid
        return l

    def upper_bound(var_21, var_22, var_23):
        (l, r) = (0, len(var_22))
        while l < r:
            mid = (r + l) // 2
            if var_22[mid] <= var_23:
                l = 1 + mid
            else:
                r = mid
        return l
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "from collections import defaultdict\nfrom random import randint\n\nclass MajorityChecker:\n\n    def __init__(var_12, var_13: List[int]):\n        var_12.arr = var_13\n        var_12.positions = defaultdict(list)\n        for (i, num) in enumerate(var_13):\n            var_12.positions[num].append(i)\n\n    def query(var_14, var_15: int, var_16: int, var_17: int) -> int:\n        for _ in range(20):\n            randomIndex = randint(var_15, var_16)\n            num = var_14.arr[randomIndex]\n            lb = var_14.lower_bound(var_14.positions[num], var_15)\n            ub = var_14.upper_bound(var_14.positions[num], var_16)\n            if ub + -lb >= var_17:\n                return num\n        return -1\n\n    def lower_bound(var_18, var_19, var_20):\n        (l, r) = (0, len(var_19))\n        while l < r:\n            mid = (r + l) // 2\n            if var_19[mid] < var_20:\n                l = 1 + mid\n            else:\n                r = mid\n        return l\n\n    def upper_bound(var_21, var_22, var_23):\n        (l, r) = (0, len(var_22))\n        while l < r:\n            mid = (r + l) // 2\n            if var_22[mid] <= var_23:\n                l = 1 + mid\n            else:\n                r = mid\n        return l"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.UnknownFormatConversionException: Conversion = 'Unable to parse expression list: (i,num)'\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:583)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFor_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$For_stmtContext.accept(Python3Parser.java:4042)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSuite(Python3ParserBaseVisitor.java:356)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$SuiteContext.accept(Python3Parser.java:4463)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitClassdef(Python3ParserBaseVisitor.java:559)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$ClassdefContext.accept(Python3Parser.java:7275)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>
