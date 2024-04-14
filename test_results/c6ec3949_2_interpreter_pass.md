# Test Report

Time: 2024-04-14 11:22:46.650698

### Base Program

```py
def find_product(x, y):
    result = x * y
    return result
```

## Test Case 1

### Modified Program

```py
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[23, 29]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 667,
                "x": 23,
                "y": 29,
                "$ret'": 667,
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
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[50, 10]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 500,
                "x": 50,
                "y": 10,
                "$ret'": 500,
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
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[28, 13]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 364,
                "x": 28,
                "y": 13,
                "$ret'": 364,
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
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[7, 76]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 532,
                "x": 7,
                "y": 76,
                "$ret'": 532,
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
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[78, 91]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 7098,
                "x": 78,
                "y": 91,
                "$ret'": 7098,
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
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[16, 35]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 560,
                "x": 16,
                "y": 35,
                "$ret'": 560,
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
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[96, 19]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1824,
                "x": 96,
                "y": 19,
                "$ret'": 1824,
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
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[1, 94]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 94,
                "x": 1,
                "y": 94,
                "$ret'": 94,
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
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[69, 21]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1449,
                "x": 69,
                "y": 21,
                "$ret'": 1449,
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
def find_product(x, y):
    result = x * y
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_product\": {\"name\": \"find_product\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_product'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "find_product",
    "inputs": "[]",
    "args": "[22, 83]"
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
            "functionName": "find_product",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 1826,
                "x": 22,
                "y": 83,
                "$ret'": 1826,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

