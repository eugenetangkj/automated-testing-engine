# Test Report

Time: 2024-04-14 07:30:30.168499

### Base Program

```py
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

## Test Case 1

### Modified Program

```py
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[66, 83]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 11245,
                "x": 66,
                "y": 83,
                "$ret'": 11245,
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
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[3, 20]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 409,
                "x": 3,
                "y": 20,
                "$ret'": 409,
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
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[20, 69]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 5161,
                "x": 20,
                "y": 69,
                "$ret'": 5161,
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
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[50, 28]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 3284,
                "x": 50,
                "y": 28,
                "$ret'": 3284,
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
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[100, 41]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 11681,
                "x": 100,
                "y": 41,
                "$ret'": 11681,
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
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[71, 90]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 13141,
                "x": 71,
                "y": 90,
                "$ret'": 13141,
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
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[64, 39]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 5617,
                "x": 64,
                "y": 39,
                "$ret'": 5617,
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
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[63, 53]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 6778,
                "x": 63,
                "y": 53,
                "$ret'": 6778,
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
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[79, 68]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 10865,
                "x": 79,
                "y": 68,
                "$ret'": 10865,
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
def sum_of_squares(x, y): # Function to calculate the sum of squares of two numbers
    result = x**2 + y**2
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"sum_of_squares\": {\"name\": \"sum_of_squares\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'sum_of_squares'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "sum_of_squares",
    "inputs": "[]",
    "args": "[64, 6]"
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
            "functionName": "sum_of_squares",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 4132,
                "x": 64,
                "y": 6,
                "$ret'": 4132,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

