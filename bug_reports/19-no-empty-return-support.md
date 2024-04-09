# Issue 19: No Empty Return Statement Support

## Description

Parser does not support an empty return statement.

### Code

```py
# This code throws an error for the parser
def main(y):
    if False:
		    return
	  else:
		    return y + 1
```

The above code doesn't get parsed and throws an error (Refer to Test Report ID c54c5f7d). However, if we assigned a value to the `return` statement that does not return anything, it gets parsed successfully (Refer to Test Report ID 58e16050.)

```python
# This code gets successfully parsed
def main(x):
    if False:
		    return 2
	  else:
		    return x + 1
```



### Input

```json
{
    "language": "py",
    "source_code": "def main(y):\n\tif False:\n\t\treturn\n\telse:\n\t\treturn y + 1"
}
```

### Output
Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
```

```json
{
  "detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.NullPointerException\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:403)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitReturn_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Return_stmtContext.accept(Python3Parser.java:2672)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitFlow_stmt(Python3ParserBaseVisitor.java:174)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Flow_stmtContext.accept(Python3Parser.java:2507)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSmall_stmt(Python3ParserBaseVisitor.java:125)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Small_stmtContext.accept(Python3Parser.java:1829)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitSimple_stmt(Python3ParserBaseVisitor.java:118)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Simple_stmtContext.accept(Python3Parser.java:1732)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:516)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitIf_stmt(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$If_stmtContext.accept(Python3Parser.java:3864)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:92)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFuncdef(PyParseTreeVisitor.java:61)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$FuncdefContext.accept(Python3Parser.java:747)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitCompound_stmt(Python3ParserBaseVisitor.java:293)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$Compound_stmtContext.accept(Python3Parser.java:3662)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visitChildren(AbstractParseTreeVisitor.java:46)\n\tat sg.edu.nus.se.its.parser.antlr.Python3ParserBaseVisitor.visitStmt(Python3ParserBaseVisitor.java:111)\n\tat sg.edu.nus.se.its.parser.antlr.Python3Parser$StmtContext.accept(Python3Parser.java:1629)\n\tat org.antlr.v4.runtime.tree.AbstractParseTreeVisitor.visit(AbstractParseTreeVisitor.java:18)\n\tat java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:195)\n\tat java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1655)\n\tat java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:484)\n\tat java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:474)\n\tat java.base/java.util.stream.ReduceOps$ReduceOp.evaluateSequential(ReduceOps.java:913)\n\tat java.base/java.util.stream.AbstractPipeline.evaluate(AbstractPipeline.java:234)\n\tat java.base/java.util.stream.ReferencePipeline.collect(ReferencePipeline.java:578)\n\tat sg.edu.nus.se.its.parser.cfg.treevisitors.PyParseTreeVisitor.visitFile_input(PyParseTreeVisitor.java:73)\n\tat sg.edu.nus.se.its.parser.ast.PyAstBuilder.buildAst(PyAstBuilder.java:20)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:53)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"
}
```

### Steps to Reproduce

```bash
curl -X 'POST' \
  'https://its.comp.nus.edu.sg/cs3213/parser' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "language": "python",
  "source_code": "def main(y):\n\tif False:\n\t\treturn\n\telse:\n\t\treturn y + 1"
}'
```

### Expected Output

It should return valid parsed output since an empty return statement is syntatically correct in Python.
