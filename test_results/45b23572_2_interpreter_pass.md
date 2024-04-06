# Test Report

Time: 2024-04-06 14:00:18.555565

### Base Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

## Test Case 1

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[32, 79]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 32,
                "b": 79,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 2

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[14, 81]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 14,
                "b": 81,
                "$ret'": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 3

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[33, 10]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 33,
                "b": 10,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 4

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[91, 33]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 91,
                "b": 33,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 5

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[73, 100]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 73,
                "b": 100,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 6

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[30, 78]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 30,
                "b": 78,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 7

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[87, 47]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 87,
                "b": 47,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 8

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[61, 56]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 61,
                "b": 56,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 9

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[44, 51]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 44,
                "b": 51,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 10

### Modified Program

```py
def test_function(a, b):
    if not a < 20 or not b > 20:
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Not\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[26, 4]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 26,
                "b": 4,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

