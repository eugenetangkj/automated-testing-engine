# Issue 1: No multi-demensional list support

## Description

Parser does not support multi-demensional lists.

### Code

```py
def f():
    dp = [[0] * (10) for _ in range(10)]
    dp[0][0] = 1
    return dp[0][0]
```

### Input

```json
{
  "language": "py",
  "source_code": "def f():\n    dp = [[0] * (10) for _ in range(10)]\n    dp[0][0] = 1\n    return dp[0][0]"
}
```

### Output

```json
{
  "detail": "Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.IllegalStateException: LHS of assignment should be a variable or subscript op\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:217)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"
}
```

### Steps to Reproduce

```bash
curl -X 'POST' 'https://its.comp.nus.edu.sg/cs3213/parser' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "language": "py",
  "source_code": "def f():\n    dp = [[0] * (10) for _ in range(10)]\n    dp[0][0] = 1\n    return dp[0][0]"
}'
```

### Expected Output

It should return valid parsed output.
