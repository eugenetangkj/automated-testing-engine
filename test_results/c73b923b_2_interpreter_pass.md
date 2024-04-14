# Test Report

Time: 2024-04-14 07:29:14.245433

### Base Program

```py
def calculate_circle_area(radius):
    return 3.14159 * (radius ** 2)
```

## Test Case 1

### Modified Program

```py
def calculate_circle_area(radius):
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[-89.19263419000734]"
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
                "$ret'": 24992.375,
                "radius": -89.192635,
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
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[-83.25105550910557]"
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
                "$ret'": 21773.537,
                "radius": -83.25105,
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
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[-44.52011180453588]"
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
                "$ret'": 6226.7583,
                "radius": -44.52011,
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
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[40.83277828554273]"
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
                "$ret'": 5238.023,
                "radius": 40.83278,
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
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[-37.39021677568468]"
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
                "$ret'": 4392.0317,
                "radius": -37.390217,
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
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[-62.42810615265433]"
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
                "$ret'": 12243.619,
                "radius": -62.428104,
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
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[-43.83553026936231]"
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
                "$ret'": 6036.734,
                "radius": -43.83553,
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
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[35.70472252683649]"
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
                "$ret'": 4004.9849,
                "radius": 35.704723,
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
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[60.53767146101029]"
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
                "$ret'": 11513.329,
                "radius": 60.53767,
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
    return 3.14159 * (radius ** 2)
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[8.23968652102856]"
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
                "$ret'": 213.29022,
                "radius": 8.239687,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

