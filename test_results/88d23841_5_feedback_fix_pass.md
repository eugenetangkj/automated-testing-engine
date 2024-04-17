# Test Report

Time: 2024-04-16 12:26 AM

### Base Program

```py
def multiply_two_numbers(a, b):
	return a * b
```

## Test Case 1

### Modified Program

```py
# Mutated by: 
def multiply_two_numbers(a, b):
    return a * b
```

<details>
<summary>feedback_fix endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"multiply_two_numbers\": {\"name\": \"multiply_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_two_numbers'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"multiply_two_numbers\": {\"name\": \"multiply_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_two_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_two_numbers",
    "inputs": "[]",
    "args": "[[21, 89], [9, 13], [75, 87], [7, 93], [30, 4], [45, 52], [69, 89], [78, 66], [11, 31], [98, 13]]"
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
def multiply_two_numbers(a, b):
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
    return a * b
```

<details>
<summary>feedback_fix endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"multiply_two_numbers\": {\"name\": \"multiply_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_two_numbers'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"multiply_two_numbers\": {\"name\": \"multiply_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"a\", {\"name\": \"a\", \"primed\": false, \"line\": 3}], \"valueList\": [\"a\", {\"name\": \"a\", \"primed\": false, \"line\": 3}]}, {\"val0\": \"b\", \"val1\": {\"name\": \"b\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, \"valueArray\": [\"b\", {\"name\": \"b\", \"primed\": false, \"line\": 8}], \"valueList\": [\"b\", {\"name\": \"b\", \"primed\": false, \"line\": 8}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}], \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}], \"line\": 13}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_two_numbers'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "multiply_two_numbers",
    "inputs": "[]",
    "args": "[[21, 89], [9, 13], [75, 87], [7, 93], [30, 4], [45, 52], [69, 89], [78, 66], [11, 31], [98, 13]]"
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
def multiply_two_numbers(a, b):
    if True:
        return a * b
```

<details>
<summary>feedback_fix endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"multiply_two_numbers\": {\"name\": \"multiply_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_two_numbers'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"multiply_two_numbers\": {\"name\": \"multiply_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_two_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_two_numbers",
    "inputs": "[]",
    "args": "[[21, 89], [9, 13], [75, 87], [7, 93], [30, 4], [45, 52], [69, 89], [78, 66], [11, 31], [98, 13]]"
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
def multiply_two_numbers(a, b):
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
        return a * b
```

<details>
<summary>feedback_fix endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"multiply_two_numbers\": {\"name\": \"multiply_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_two_numbers'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"multiply_two_numbers\": {\"name\": \"multiply_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"a\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"a\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"a\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"a\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"a\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"b\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"b\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"b\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 14, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 14, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 14, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_two_numbers'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "multiply_two_numbers",
    "inputs": "[]",
    "args": "[[21, 89], [9, 13], [75, 87], [7, 93], [30, 4], [45, 52], [69, 89], [78, 66], [11, 31], [98, 13]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

