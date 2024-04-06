# Test Report

Time: 2024-04-06 14:53:45.007956

### Base Program

```py
def test_function():
    a = True
    b = False
    if a or b:
        return True
    else:
        return False
```

## Test Case 1

### Modified Program

```py
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
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
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
                "$ret'": true,
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
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
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
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
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
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
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
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
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
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
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
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
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
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
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
def test_function():
    a = True
    b = False
    if a or b:
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
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"a\", {\"value\": \"True\", \"line\": 2}], \"valueList\": [\"a\", {\"value\": \"True\", \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"b\", {\"value\": \"False\", \"line\": 3}], \"valueList\": [\"b\", {\"value\": \"False\", \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[]"
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
                "a": "<undef>",
                "b": "<undef>",
                "b'": false,
                "a'": true,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

