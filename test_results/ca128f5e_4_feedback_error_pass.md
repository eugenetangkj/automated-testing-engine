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
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[[100, 62], [84, 49], [0, 35], [47, 53], [89, 83], [94, 48], [30, 42], [84, 82], [25, 10], [33, 59]]"
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
def calculate_area(var_0, var_1):
    return var_0 * var_1
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_0\", \"val1\": \"*\", \"valueArray\": [\"var_0\", \"*\"], \"valueList\": [\"var_0\", \"*\"]}, {\"val0\": \"var_1\", \"val1\": \"*\", \"valueArray\": [\"var_1\", \"*\"], \"valueList\": [\"var_1\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[[100, 62], [84, 49], [0, 35], [47, 53], [89, 83], [94, 48], [30, 42], [84, 82], [25, 10], [33, 59]]"
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
def calculate_area(width, height):
    return height * width
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[[100, 62], [84, 49], [0, 35], [47, 53], [89, 83], [94, 48], [30, 42], [84, 82], [25, 10], [33, 59]]"
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
def calculate_area(var_2, var_3):
    return var_3 * var_2
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"width\", \"val1\": \"*\", \"valueArray\": [\"width\", \"*\"], \"valueList\": [\"width\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"width\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_area\": {\"name\": \"calculate_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_2\", \"val1\": \"*\", \"valueArray\": [\"var_2\", \"*\"], \"valueList\": [\"var_2\", \"*\"]}, {\"val0\": \"var_3\", \"val1\": \"*\", \"valueArray\": [\"var_3\", \"*\"], \"valueList\": [\"var_3\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_area'\"}, \"types\": {}}}}",
    "function": "calculate_area",
    "inputs": "[]",
    "args": "[[100, 62], [84, 49], [0, 35], [47, 53], [89, 83], [94, 48], [30, 42], [84, 82], [25, 10], [33, 59]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

