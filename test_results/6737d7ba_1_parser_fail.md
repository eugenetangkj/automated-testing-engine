# Test Report

Time: 2024-03-30 07:38:06.513287

### Base Program

```py
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.customer_count = 0
        self.prices_map = {products[i]: prices[i] for i in range(len(products))}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        total = sum(self.prices_map[product[i]] * amount[i] for i in range(len(product)))
        if self.customer_count % self.n == 0:
            total *= (100 - self.discount) / 100
        return total
```

## Test Case 1

### Modified Program

```py
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.customer_count = 0
        self.prices_map = {products[i]: prices[i] for i in range(len(products))}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        total = sum((self.prices_map[product[i]] * amount[i] for i in range(len(product))))
        if self.customer_count % self.n == 0:
            total *= (100 - self.discount) / 100
        return total
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "class Cashier:\n\n    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):\n        self.n = n\n        self.discount = discount\n        self.customer_count = 0\n        self.prices_map = {products[i]: prices[i] for i in range(len(products))}\n\n    def getBill(self, product: List[int], amount: List[int]) -> float:\n        self.customer_count += 1\n        total = sum((self.prices_map[product[i]] * amount[i] for i in range(len(product))))\n        if self.customer_count % self.n == 0:\n            total *= (100 - self.discount) / 100\n        return total"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: Unable to parse left operand: [Member: L10] [Name: L10] self.customer_count\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.lambda$visitBinaryOp$7(PyAstVisitor.java:870)\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:408)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitBinaryOp(PyAstVisitor.java:869)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:354)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AugAssignNode.accept(AugAssignNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:172)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
class Cashier:

    def __init__(var_0, var_1: int, var_2: int, var_3: List[int], var_4: List[int]):
        var_0.n = var_1
        var_0.discount = var_2
        var_0.customer_count = 0
        var_0.prices_map = {var_3[i]: var_4[i] for i in range(len(var_3))}

    def getBill(var_5, var_6: List[int], var_7: List[int]) -> float:
        var_5.customer_count += 1
        total = sum((var_5.prices_map[var_6[i]] * var_7[i] for i in range(len(var_6))))
        if var_5.customer_count % var_5.n == 0:
            total *= (100 - var_5.discount) / 100
        return total
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "class Cashier:\n\n    def __init__(var_0, var_1: int, var_2: int, var_3: List[int], var_4: List[int]):\n        var_0.n = var_1\n        var_0.discount = var_2\n        var_0.customer_count = 0\n        var_0.prices_map = {var_3[i]: var_4[i] for i in range(len(var_3))}\n\n    def getBill(var_5, var_6: List[int], var_7: List[int]) -> float:\n        var_5.customer_count += 1\n        total = sum((var_5.prices_map[var_6[i]] * var_7[i] for i in range(len(var_6))))\n        if var_5.customer_count % var_5.n == 0:\n            total *= (100 - var_5.discount) / 100\n        return total"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: Unable to parse left operand: [Member: L10] [Name: L10] var_5.customer_count\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.lambda$visitBinaryOp$7(PyAstVisitor.java:870)\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:408)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitBinaryOp(PyAstVisitor.java:869)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:354)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AugAssignNode.accept(AugAssignNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:172)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.customer_count = 0
        self.prices_map = {products[i]: prices[i] for i in range(len(products))}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        total = sum((amount[i] * self.prices_map[product[i]] for i in range(len(product))))
        if self.customer_count % self.n == 0:
            total *= (100 + -self.discount) / 100
        return total
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "class Cashier:\n\n    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):\n        self.n = n\n        self.discount = discount\n        self.customer_count = 0\n        self.prices_map = {products[i]: prices[i] for i in range(len(products))}\n\n    def getBill(self, product: List[int], amount: List[int]) -> float:\n        self.customer_count += 1\n        total = sum((amount[i] * self.prices_map[product[i]] for i in range(len(product))))\n        if self.customer_count % self.n == 0:\n            total *= (100 + -self.discount) / 100\n        return total"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: Unable to parse left operand: [Member: L10] [Name: L10] self.customer_count\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.lambda$visitBinaryOp$7(PyAstVisitor.java:870)\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:408)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitBinaryOp(PyAstVisitor.java:869)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:354)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AugAssignNode.accept(AugAssignNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:172)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
class Cashier:

    def __init__(var_8, var_9: int, var_10: int, var_11: List[int], var_12: List[int]):
        var_8.n = var_9
        var_8.discount = var_10
        var_8.customer_count = 0
        var_8.prices_map = {var_11[i]: var_12[i] for i in range(len(var_11))}

    def getBill(var_13, var_14: List[int], var_15: List[int]) -> float:
        var_13.customer_count += 1
        total = sum((var_15[i] * var_13.prices_map[var_14[i]] for i in range(len(var_14))))
        if var_13.customer_count % var_13.n == 0:
            total *= (100 + -var_13.discount) / 100
        return total
```

<details>
<summary>parser endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "class Cashier:\n\n    def __init__(var_8, var_9: int, var_10: int, var_11: List[int], var_12: List[int]):\n        var_8.n = var_9\n        var_8.discount = var_10\n        var_8.customer_count = 0\n        var_8.prices_map = {var_11[i]: var_12[i] for i in range(len(var_11))}\n\n    def getBill(var_13, var_14: List[int], var_15: List[int]) -> float:\n        var_13.customer_count += 1\n        total = sum((var_15[i] * var_13.prices_map[var_14[i]] for i in range(len(var_14))))\n        if var_13.customer_count % var_13.n == 0:\n            total *= (100 + -var_13.discount) / 100\n        return total"
}
```

Message: 
```
Error in making API call to https://its.comp.nus.edu.sg/cs3213/parser. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: \nError: ANTLR Tool version 4.9.1 used for code generation does not match the current runtime version 4.7.1Exception in thread \"main\" java.util.NoSuchElementException: Unable to parse left operand: [Member: L10] [Name: L10] var_13.customer_count\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.lambda$visitBinaryOp$7(PyAstVisitor.java:870)\n\tat java.base/java.util.Optional.orElseThrow(Optional.java:408)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitBinaryOp(PyAstVisitor.java:869)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:354)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AugAssignNode.accept(AugAssignNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:172)\n\tat sg.edu.nus.se.its.parser.ast.nodes.AssignmentNode.accept(AssignmentNode.java:23)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.handleCodeBlockChild(PyAstVisitor.java:934)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:144)\n\tat sg.edu.nus.se.its.parser.ast.nodes.FunctionNode.accept(FunctionNode.java:52)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visit(PyAstVisitor.java:109)\n\tat sg.edu.nus.se.its.parser.ast.nodes.ProgramNode.accept(ProgramNode.java:38)\n\tat sg.edu.nus.se.its.parser.ast.PyAstVisitor.visitAst(PyAstVisitor.java:95)\n\tat sg.edu.nus.se.its.parser.cfg.PyProgramModelBuilder.buildProgram(PyProgramModelBuilder.java:27)\n\tat sg.edu.nus.se.its.parser.cfg.CfgBuilder.build(CfgBuilder.java:55)\n\tat sg.edu.nus.se.its.parser.PyParser.parse(PyParser.java:28)\n\tat sg.edu.nus.se.its.parser.pyParse.main(pyParse.java:44)\n"}
```

Actual Output: None

</details>

