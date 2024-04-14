# Test Report

Time: 2024-04-14 09:30 PM

### Base Program

```py
def calculate_area(width, height):
    return width * height
```

## Test Case 1

### Modified Program

```py
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[100, 62]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 100,
                "$ret'": 6200,
                "height": 62,
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
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[84, 49]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 84,
                "$ret'": 4116,
                "height": 49,
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
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[0, 35]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 0,
                "$ret'": 0,
                "height": 35,
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
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[47, 53]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 47,
                "$ret'": 2491,
                "height": 53,
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
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[89, 83]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 89,
                "$ret'": 7387,
                "height": 83,
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
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[94, 48]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 94,
                "$ret'": 4512,
                "height": 48,
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
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[30, 42]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 30,
                "$ret'": 1260,
                "height": 42,
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
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[84, 82]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 84,
                "$ret'": 6888,
                "height": 82,
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
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[25, 10]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 25,
                "$ret'": 250,
                "height": 10,
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
def calculate_area(width, height):
    return width * height
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[33, 59]"
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
            "functionName": "calculate_area",
            "location": 1,
            "mem": {
                "width": 33,
                "$ret'": 1947,
                "height": 59,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

