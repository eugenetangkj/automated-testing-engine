# Test Report

Time: 2024-04-14 07:33:21.796079

### Base Program

```py
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

## Test Case 1

### Modified Program

```py
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[29.754900742900077]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 2781.4197,
                "radius": 29.7549,
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
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[51.46225226308218]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 8320.073,
                "radius": 51.462254,
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
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[13.039486204438717]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 534.15894,
                "radius": 13.039486,
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
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[19.407383176729454]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 1183.2689,
                "radius": 19.407383,
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
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[76.01431580868987]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 18152.66,
                "radius": 76.01431,
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
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[-75.25425742209325]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 17791.463,
                "radius": -75.25426,
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
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[82.21862867365121]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 21236.846,
                "radius": 82.21863,
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
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[30.166276229768528]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 2858.8606,
                "radius": 30.166277,
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
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[47.40210301130975]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 7059.026,
                "radius": 47.402103,
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
def calculate_circle_area(radius):
    return 3.14159 * radius * radius
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[-58.47243520490868]"
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
            "functionName": "calculate_circle_area",
            "location": 1,
            "mem": {
                "$ret'": 10741.178,
                "radius": -58.472435,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

