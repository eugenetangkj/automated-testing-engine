# Test Report

Time: 2024-04-17 10:17 PM

### Base Program

```py
def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target
```

## Test Case 1

### Modified Program

```py

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[45, 39]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 45,
                "target": 39
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "startValue": 45,
                "target": 39,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "$ret'": 6,
                "startValue": 45,
                "target": 39,
                "$cond": false,
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

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[78, 32]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 78,
                "target": 32
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "startValue": 78,
                "target": 32,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "$ret'": 46,
                "startValue": 78,
                "target": 32,
                "$cond": false,
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

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[22, 65]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 22,
                "target": 65
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": true,
                "startValue": 22,
                "target": 65,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 1,
                "operations": 0,
                "$cond'": true,
                "target'": 66,
                "startValue": 22,
                "target": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 1,
                "operations": 1,
                "$cond'": true,
                "target'": 66,
                "startValue": 22,
                "target": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 2,
                "operations": 1,
                "$cond'": true,
                "target'": 33,
                "startValue": 22,
                "target": 66,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 2,
                "operations": 2,
                "$cond'": true,
                "target'": 33,
                "startValue": 22,
                "target": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 3,
                "operations": 2,
                "$cond'": true,
                "target'": 34,
                "startValue": 22,
                "target": 33,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 3,
                "operations": 3,
                "$cond'": true,
                "target'": 34,
                "startValue": 22,
                "target": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 4,
                "operations": 3,
                "$cond'": true,
                "target'": 17,
                "startValue": 22,
                "target": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 4,
                "operations": 4,
                "$cond'": false,
                "target'": 17,
                "startValue": 22,
                "target": 17,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 4,
                "operations": 4,
                "$cond'": false,
                "target'": 17,
                "$ret'": 9,
                "startValue": 22,
                "target": 17,
                "$cond": false,
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

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[46, 29]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 46,
                "target": 29
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "startValue": 46,
                "target": 29,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "$ret'": 17,
                "startValue": 46,
                "target": 29,
                "$cond": false,
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

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[54, 85]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 54,
                "target": 85
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": true,
                "startValue": 54,
                "target": 85,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 1,
                "operations": 0,
                "$cond'": true,
                "target'": 86,
                "startValue": 54,
                "target": 85,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 1,
                "operations": 1,
                "$cond'": true,
                "target'": 86,
                "startValue": 54,
                "target": 86,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 2,
                "operations": 1,
                "$cond'": true,
                "target'": 43,
                "startValue": 54,
                "target": 86,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 2,
                "operations": 2,
                "$cond'": false,
                "target'": 43,
                "startValue": 54,
                "target": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 2,
                "operations": 2,
                "$cond'": false,
                "target'": 43,
                "$ret'": 13,
                "startValue": 54,
                "target": 43,
                "$cond": false,
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

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[26, 29]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 26,
                "target": 29
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": true,
                "startValue": 26,
                "target": 29,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 1,
                "operations": 0,
                "$cond'": true,
                "target'": 30,
                "startValue": 26,
                "target": 29,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 1,
                "operations": 1,
                "$cond'": true,
                "target'": 30,
                "startValue": 26,
                "target": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 2,
                "operations": 1,
                "$cond'": true,
                "target'": 15,
                "startValue": 26,
                "target": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 2,
                "operations": 2,
                "$cond'": false,
                "target'": 15,
                "startValue": 26,
                "target": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 2,
                "operations": 2,
                "$cond'": false,
                "target'": 15,
                "$ret'": 13,
                "startValue": 26,
                "target": 15,
                "$cond": false,
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

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[72, 20]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 72,
                "target": 20
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "startValue": 72,
                "target": 20,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "$ret'": 52,
                "startValue": 72,
                "target": 20,
                "$cond": false,
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

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[35, 71]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 35,
                "target": 71
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": true,
                "startValue": 35,
                "target": 71,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 1,
                "operations": 0,
                "$cond'": true,
                "target'": 72,
                "startValue": 35,
                "target": 71,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 1,
                "operations": 1,
                "$cond'": true,
                "target'": 72,
                "startValue": 35,
                "target": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 2,
                "operations": 1,
                "$cond'": true,
                "target'": 36,
                "startValue": 35,
                "target": 72,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 2,
                "operations": 2,
                "$cond'": true,
                "target'": 36,
                "startValue": 35,
                "target": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 3,
                "operations": 2,
                "$cond'": true,
                "target'": 18,
                "startValue": 35,
                "target": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 3,
                "operations": 3,
                "$cond'": false,
                "target'": 18,
                "startValue": 35,
                "target": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 3,
                "operations": 3,
                "$cond'": false,
                "target'": 18,
                "$ret'": 20,
                "startValue": 35,
                "target": 18,
                "$cond": false,
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

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[69, 73]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 69,
                "target": 73
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": true,
                "startValue": 69,
                "target": 73,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 1,
                "operations": 0,
                "$cond'": true,
                "target'": 74,
                "startValue": 69,
                "target": 73,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 1,
                "operations": 1,
                "$cond'": true,
                "target'": 74,
                "startValue": 69,
                "target": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 4,
            "mem": {
                "operations'": 2,
                "operations": 1,
                "$cond'": true,
                "target'": 37,
                "startValue": 69,
                "target": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 2,
                "operations": 2,
                "$cond'": false,
                "target'": 37,
                "startValue": 69,
                "target": 37,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 2,
                "operations": 2,
                "$cond'": false,
                "target'": 37,
                "$ret'": 34,
                "startValue": 69,
                "target": 37,
                "$cond": false,
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

def broken_calc(startValue: int, target: int) -> int:
    operations = 0
    while target > startValue:
        target = target // 2 if target % 2 == 0 else target + 1
        operations += 1
    return operations + startValue - target


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"broken_calc\": {\"name\": \"broken_calc\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"startValue\", \"val1\": \"*\", \"valueArray\": [\"startValue\", \"*\"], \"valueList\": [\"startValue\", \"*\"]}, {\"val0\": \"target\", \"val1\": \"*\", \"valueArray\": [\"target\", \"*\"], \"valueList\": [\"target\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"operations\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"operations\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"operations\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"startValue\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"target\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}], \"4\": [{\"val0\": \"target\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"target\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"target\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"operations\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"operations\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"operations\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'broken_calc'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"operations\": \"*\", \"target\": \"*\"}}}}",
    "function": "broken_calc",
    "inputs": "[]",
    "args": "[34, 5]"
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
            "functionName": "broken_calc",
            "location": 1,
            "mem": {
                "operations'": 0,
                "operations": "<undef>",
                "startValue": 34,
                "target": 5
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 2,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "startValue": 34,
                "target": 5,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 0,
                "operations": 0,
                "$cond'": false,
                "$ret'": 29,
                "startValue": 34,
                "target": 5,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

