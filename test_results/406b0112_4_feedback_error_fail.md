# Test Report

Time: 2024-04-06 13:22:20.686258

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
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[[98], [97], [61], [40], [90], [19], [9], [79], [6], [65]]"
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
def func(x):
    x = x + 1
    j = 2
    while j < 5:
        x += 1
        j = j + 1
    return x
```

<details>
<summary>feedback_error endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 5}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'for' loop at line 3\", \"3\": \"*after* the 'for' loop starting at line 3\", \"4\": \"inside the body of the 'for' loop beginning at line 4\"}, \"types\": {\"ind#0\": \"int\", \"x\": \"*\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"func\": {\"name\": \"func\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"j\", \"val1\": {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"j\", {\"value\": \"2\", \"line\": 3}], \"valueList\": [\"j\", {\"value\": \"2\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"x\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"x\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"j\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"Add\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"j\", {\"name\": \"Add\", \"args\": [{\"name\": \"j\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'func'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"x\": \"*\", \"j\": \"*\"}}}}",
    "function": "func",
    "inputs": "[]",
    "args": "[[98], [97], [61], [40], [90], [19], [9], [79], [6], [65]]"
}
```

Message: 
```
Feedback error endpoint failed
```

Actual Output: 
```json
[
    {
        "lineNumber": 3,
        "hintStrings": [
            "Incorrect/Unnecessary expression assigned to variable: *j*"
        ]
    },
    {
        "lineNumber": 1,
        "hintStrings": [
            "You need to assign a suitable value to variable: *dummy2*"
        ]
    },
    {
        "lineNumber": 1,
        "hintStrings": [
            "You need to assign a suitable value to variable: *dummy1*"
        ]
    },
    {
        "lineNumber": 4,
        "hintStrings": [
            "Wrong loop condition: (j < 5)"
        ]
    },
    {
        "lineNumber": 6,
        "hintStrings": [
            "Wrong expression for variable: *j*"
        ]
    },
    {
        "lineNumber": 4,
        "hintStrings": [
            "You need to assign a suitable value to variable: *dummy1*"
        ]
    }
]
```

</details>

