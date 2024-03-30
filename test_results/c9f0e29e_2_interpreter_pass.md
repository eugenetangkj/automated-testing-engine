# Test Report

Time: 2024-03-30 07:47:17.834141

### Base Program

```py
def count_odds(low, high):
    return (high + 1) // 2 - low // 2
```

## Test Case 1

### Modified Program

```py

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[67, 47]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 47,
                "low": 67,
                "$ret'": -9,
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

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[4, 64]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 64,
                "low": 4,
                "$ret'": 30,
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

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[47, 6]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 6,
                "low": 47,
                "$ret'": -20,
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

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[69, 84]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 84,
                "low": 69,
                "$ret'": 8,
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

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[83, 26]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 26,
                "low": 83,
                "$ret'": -28,
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

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[15, 7]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 7,
                "low": 15,
                "$ret'": -3,
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

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[40, 76]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 76,
                "low": 40,
                "$ret'": 18,
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

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[61, 27]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 27,
                "low": 61,
                "$ret'": -16,
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

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[10, 94]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 94,
                "low": 10,
                "$ret'": 42,
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

def count_odds(low, high):
    return (high + 1) // 2 - low // 2


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[25, 47]"
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
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 47,
                "low": 25,
                "$ret'": 12,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

