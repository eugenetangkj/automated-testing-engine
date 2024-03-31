# Test Report

Time: 2024-03-31 15:24:02.805765

### Base Program

```py
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

## Test Case 1

### Modified Program

```py
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[-23.858853435013344]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 1787.4291,
                "radius": -23.858854,
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
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[41.77580098520218]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 5479.984,
                "radius": 41.775803,
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
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[-60.35460883645556]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 11438.013,
                "radius": -60.35461,
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
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[-9.12017724492982]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 261.17776,
                "radius": -9.120177,
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
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[-73.66797613475168]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 17040.69,
                "radius": -73.66798,
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
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[-56.4877863599232]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 10019.332,
                "radius": -56.487785,
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
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[19.342871975815328]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 1174.8208,
                "radius": 19.342873,
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
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[-96.91290290942402]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 29491.229,
                "radius": -96.9129,
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
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[18.371674770780942]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 1059.808,
                "radius": 18.371675,
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
def calculate_area_circle(radius):
    return 3.14 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_area_circle\": {\"name\": \"calculate_area_circle\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area_circle'\"}, \"types\": {}}}}",
    "function": "calculate_area_circle",
    "inputs": "[]",
    "args": "[64.36377838841776]"
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
            "functionName": "calculate_area_circle",
            "location": 1,
            "mem": {
                "$ret'": 13008.065,
                "radius": 64.36378,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

