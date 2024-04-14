# Issue 23: Incomplete List Slicing Support in Parser

## Description

The parser supports list slicing with indices, but when indices are not provided, the parser throws an error. In Python, it is possible to not include indices for slicing.

### Code

```py
def main(x):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[:]
	return new_list
```

The code snippet above uses slicing without indices to obtain a copy of the original list. The parser is unable to parse it. (Test Report ID b5446b8f)

However, it works with the following code snippet (Test Report ID 311c9d7e):

```py
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

### Input

```json
{
    "language": "py",
    "source_code": "def main(x):\n\toriginal_list = [1, 2, 3, 4, 5]\n\tnew_list = original_list[:]\n\treturn new_list"
}
```

### Output

```json
null
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.lang.NullPointerException\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:696)\n\tat sg.edu.nus.se.its.parser.ast.nodes.SubscriptOpNode.accept(SubscriptOpNode.java:43)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:172)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:962)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

### Steps to Reproduce

```bash
curl -X 'POST' \
  'https://its.comp.nus.edu.sg/cs3213/parser' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "language": "py",
    "source_code": "def main(x):\n\toriginal_list = [1, 2, 3, 4, 5]\n\tnew_list = original_list[:]\n\treturn new_list"
}'
```

### Expected Output

It should return valid execution output.
