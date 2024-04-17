# Test Report

Time: 2024-04-17 10:17 PM

### Base Program

```py
def product_of_two_numbers(a, b):
    result = a * b
    return result
```

## Test Case 1

### Modified Program

```py
def product_of_two_numbers(a, b):
    result = a * b
    return result
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {\"result\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[[84, 84], [32, 49], [70, 76], [91, 23], [7, 64], [95, 100], [48, 95], [96, 44], [66, 0], [49, 46]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
# Mutated by: ExtraArgumentReassignmentModifier
def product_of_two_numbers(a, b):
    a = a
    a = a
    a = a
    a = a
    a = a
    b = b
    b = b
    b = b
    b = b
    b = b
    result = a * b
    return result
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {\"result\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"a\", {\"name\": \"a\", \"primed\": false, \"line\": 3}], \"valueList\": [\"a\", {\"name\": \"a\", \"primed\": false, \"line\": 3}]}, {\"val0\": \"b\", \"val1\": {\"name\": \"b\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, \"valueArray\": [\"b\", {\"name\": \"b\", \"primed\": false, \"line\": 8}], \"valueList\": [\"b\", {\"name\": \"b\", \"primed\": false, \"line\": 8}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}], \"line\": 13}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}], \"line\": 13}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 14, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 14}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 14}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {\"result\": \"*\", \"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[[84, 84], [32, 49], [70, 76], [91, 23], [7, 64], [95, 100], [48, 95], [96, 44], [66, 0], [49, 46]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
# Mutated by: WrapInIfTrueModifier
def product_of_two_numbers(a, b):
    if True:
        result = a * b
        return result
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {\"result\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"result\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"result\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"result\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"result\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[[84, 84], [32, 49], [70, 76], [91, 23], [7, 64], [95, 100], [48, 95], [96, 44], [66, 0], [49, 46]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
# Mutated by: ExtraArgumentReassignmentModifier, WrapInIfTrueModifier
def product_of_two_numbers(a, b):
    if True:
        a = a
        a = a
        a = a
        a = a
        a = a
        b = b
        b = b
        b = b
        b = b
        b = b
        result = a * b
        return result
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {\"result\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"a\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"a\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"a\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"a\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"a\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"b\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"b\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"b\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 14, \"tokentype\": \"Operation\"}, {\"name\": \"result\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 14, \"tokentype\": \"Operation\"}, {\"name\": \"result\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"result\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 14, \"tokentype\": \"Operation\"}, {\"name\": \"result\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 14, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 14, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 14, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {\"result\": \"*\", \"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[[84, 84], [32, 49], [70, 76], [91, 23], [7, 64], [95, 100], [48, 95], [96, 44], [66, 0], [49, 46]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

