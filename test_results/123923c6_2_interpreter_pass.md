# Test Report

Time: 2024-03-30 07:24:27.771584

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
    "args": "[44, 31]"
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
                "startValue": 44,
                "target": 31
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
                "startValue": 44,
                "target": 31,
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
                "$ret'": 13,
                "startValue": 44,
                "target": 31,
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
    "args": "[89, 15]"
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
                "startValue": 89,
                "target": 15
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
                "startValue": 89,
                "target": 15,
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
                "$ret'": 74,
                "startValue": 89,
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
    "args": "[52, 8]"
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
                "startValue": 52,
                "target": 8
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
                "startValue": 52,
                "target": 8,
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
                "$ret'": 44,
                "startValue": 52,
                "target": 8,
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
    "args": "[56, 67]"
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
                "startValue": 56,
                "target": 67
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
                "startValue": 56,
                "target": 67,
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
                "target'": 68,
                "startValue": 56,
                "target": 67,
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
                "target'": 68,
                "startValue": 56,
                "target": 68,
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
                "target'": 34,
                "startValue": 56,
                "target": 68,
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
                "target'": 34,
                "startValue": 56,
                "target": 34,
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
                "target'": 34,
                "$ret'": 24,
                "startValue": 56,
                "target": 34,
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
    "args": "[80, 13]"
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
                "startValue": 80,
                "target": 13
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
                "startValue": 80,
                "target": 13,
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
                "$ret'": 67,
                "startValue": 80,
                "target": 13,
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
    "args": "[99, 43]"
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
                "startValue": 99,
                "target": 43
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
                "startValue": 99,
                "target": 43,
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
                "$ret'": 56,
                "startValue": 99,
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
    "args": "[55, 88]"
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
                "startValue": 55,
                "target": 88
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
                "startValue": 55,
                "target": 88,
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
                "target'": 44,
                "startValue": 55,
                "target": 88,
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
                "$cond'": false,
                "target'": 44,
                "startValue": 55,
                "target": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "broken_calc",
            "location": 3,
            "mem": {
                "operations'": 1,
                "operations": 1,
                "$cond'": false,
                "target'": 44,
                "$ret'": 12,
                "startValue": 55,
                "target": 44,
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
    "args": "[87, 0]"
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
                "startValue": 87,
                "target": 0
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
                "startValue": 87,
                "target": 0,
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
                "$ret'": 87,
                "startValue": 87,
                "target": 0,
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
    "args": "[47, 83]"
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
                "startValue": 47,
                "target": 83
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
                "startValue": 47,
                "target": 83,
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
                "target'": 84,
                "startValue": 47,
                "target": 83,
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
                "target'": 84,
                "startValue": 47,
                "target": 84,
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
                "target'": 42,
                "startValue": 47,
                "target": 84,
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
                "target'": 42,
                "startValue": 47,
                "target": 42,
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
                "target'": 42,
                "$ret'": 7,
                "startValue": 47,
                "target": 42,
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
    "args": "[92, 16]"
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
                "startValue": 92,
                "target": 16
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
                "startValue": 92,
                "target": 16,
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
                "$ret'": 76,
                "startValue": 92,
                "target": 16,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

