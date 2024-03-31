# Test Report

Time: 2024-03-31 15:23:44.651950

### Base Program

```py
def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
```

## Test Case 1

### Modified Program

```py
def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
```

<details>
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 2}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[[81], [27], [35], [56], [74], [94], [21], [34], [18], [84]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

## Test Case 2

### Modified Program

```py
def trailing_zeroes(var_0: int) -> int:
    count = 0
    while var_0 > 0:
        var_0 //= 5
        count += var_0
    return count
```

<details>
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_0\", \"val1\": \"*\", \"valueArray\": [\"var_0\", \"*\"], \"valueList\": [\"var_0\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 2}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"var_0\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"var_0\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"var_0\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_0\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_0\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_0\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"var_0\": \"*\", \"count\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[[81], [27], [35], [56], [74], [94], [21], [34], [18], [84]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

## Test Case 3

### Modified Program

```py
def trailing_zeroes(var_1: int) -> int:
    count = 0
    while var_1 > 0:
        var_1 //= 5
        count += var_1
    return count
```

<details>
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_1\", \"val1\": \"*\", \"valueArray\": [\"var_1\", \"*\"], \"valueList\": [\"var_1\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 2}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"var_1\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"var_1\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"var_1\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_1\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_1\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_1\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"var_1\": \"*\", \"count\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[[81], [27], [35], [56], [74], [94], [21], [34], [18], [84]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

