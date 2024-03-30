# Test Report

Time: 2024-03-30 06:13:53.306793

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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[85, 33]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 33,
                "low": 85,
                "$ret'": -25,
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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[33, 50]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 50,
                "low": 33,
                "$ret'": 9,
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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[39, 4]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 4,
                "low": 39,
                "$ret'": -17,
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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[53, 16]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 16,
                "low": 53,
                "$ret'": -18,
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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[94, 52]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 52,
                "low": 94,
                "$ret'": -21,
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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[39, 78]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 78,
                "low": 39,
                "$ret'": 20,
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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[80, 81]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 81,
                "low": 80,
                "$ret'": 1,
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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[2, 69]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 69,
                "low": 2,
                "$ret'": 34,
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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[10, 22]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 22,
                "low": 10,
                "$ret'": 6,
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

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_odds\": {\"name\": \"count_odds\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"low\", \"val1\": \"*\", \"valueArray\": [\"low\", \"*\"], \"valueList\": [\"low\", \"*\"]}, {\"val0\": \"high\", \"val1\": \"*\", \"valueArray\": [\"high\", \"*\"], \"valueList\": [\"high\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"high\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"low\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_odds'\"}, \"types\": {}}}}",
    "function": "count_odds",
    "inputs": "[]",
    "args": "[20, 79]"
}
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "count_odds",
            "location": 1,
            "mem": {
                "high": 79,
                "low": 20,
                "$ret'": 30,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

