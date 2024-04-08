# Test Report

Time: 2024-04-06 13:22:11.967818

### Base Program

```py
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

## Test Case 1

### Modified Program

```py
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[98]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 98,
                "iter#0": "<undef>",
                "x'": 99
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 99,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 99,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 99,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 100,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 100,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 100,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 100,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 101,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 101,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 101,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 101,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 102,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 102,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 102,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 102,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 102,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 102,
                "j'": 4
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
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[97]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 97,
                "iter#0": "<undef>",
                "x'": 98
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 98,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 98,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 98,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 99,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 99,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 99,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 99,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 100,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 100,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 100,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 100,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 101,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 101,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 101,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 101,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 101,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 101,
                "j'": 4
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
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[61]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 61,
                "iter#0": "<undef>",
                "x'": 62
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 62,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 62,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 62,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 63,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 63,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 63,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 64,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 64,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 64,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 65,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 65,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 65,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 65,
                "j'": 4
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
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[40]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 40,
                "iter#0": "<undef>",
                "x'": 41
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 41,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 41,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 41,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 42,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 42,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 43,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 43,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 43,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 44,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 44,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 44,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 44,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 44,
                "j'": 4
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
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[90]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 90,
                "iter#0": "<undef>",
                "x'": 91
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 91,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 91,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 91,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 92,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 92,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 92,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 92,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 93,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 93,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 93,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 93,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 94,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 94,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 94,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 94,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 94,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 94,
                "j'": 4
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
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[19]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 19,
                "iter#0": "<undef>",
                "x'": 20
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 20,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 20,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 20,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 21,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 21,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 22,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 22,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 23,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 23,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 23,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 23,
                "j'": 4
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
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[9]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 9,
                "iter#0": "<undef>",
                "x'": 10
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 10,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 10,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 11,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 11,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 12,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 12,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 13,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 13,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 13,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 13,
                "j'": 4
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
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[79]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 79,
                "iter#0": "<undef>",
                "x'": 80
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 80,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 80,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 80,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 81,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 81,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 82,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 82,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 82,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 83,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 83,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 83,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 83,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 83,
                "j'": 4
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
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[6]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 6,
                "iter#0": "<undef>",
                "x'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 7,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 7,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 7,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 8,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 8,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 9,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 9,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 10,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 10,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 10,
                "j'": 4
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
def func(x):
    x = x + 1
    for j in range(2, 5):
        x += 1
    return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[65]"
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
            "functionName": "func",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": "<undef>",
                "x": 65,
                "iter#0": "<undef>",
                "x'": 66
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 66,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "x'": 66,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 0,
                "x": 66,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": "<undef>",
                "j'": 2,
                "x'": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 67,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 2,
                "x'": 67,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 1,
                "x": 67,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 2,
                "j'": 3,
                "x'": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 68,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 3,
                "x'": 68,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 2,
                "x": 68,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 3,
                "j'": 4,
                "x'": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "ind#0": 3,
                "x": 69,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "j'": 4,
                "x'": 69,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "func",
            "location": 3,
            "mem": {
                "iter#0'": [
                    2,
                    3,
                    4
                ],
                "j": 4,
                "x'": 69,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "x": 69,
                "iter#0": [
                    2,
                    3,
                    4
                ],
                "$ret'": 69,
                "j'": 4
            },
            "isChecked": false
        }
    ]
}
```

</details>

