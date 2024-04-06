# Test Report

Time: 2024-04-06 13:55:15.108834

### Base Program

```py
def test_function(a, b):
    if a > 5 or b > 10:
        return True
    else:
        return False
```

## Test Case 1

### Modified Program

```py
def test_function(a, b):
    if a > 5 or b > 10:
        return True
    else:
        return False
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[[70, 21], [15, 1], [49, 71], [56, 55], [16, 30], [15, 86], [21, 89], [19, 75], [17, 39], [90, 38]]"
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
def test_function(a, b):
    if not (not a > 5 and (not b > 10)):
        return True
    else:
        return False
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[[70, 21], [15, 1], [49, 71], [56, 55], [16, 30], [15, 86], [21, 89], [19, 75], [17, 39], [90, 38]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

