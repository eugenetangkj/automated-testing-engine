# Test Report

Time: 2024-03-31 15:23:39.423739

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
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[81]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 81
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 81,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 16,
                "count'": 16,
                "n": 81,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 16,
                "n'": 16,
                "count'": 16,
                "n": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 16,
                "n'": 3,
                "count'": 19,
                "n": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 19,
                "n'": 3,
                "count'": 19,
                "n": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 19,
                "n'": 0,
                "count'": 19,
                "n": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 19,
                "n'": 0,
                "count'": 19,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 19,
                "n'": 0,
                "count'": 19,
                "$ret'": 19,
                "n": 0,
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

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[27]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 27
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 27,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 5,
                "count'": 5,
                "n": 27,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 5,
                "n'": 5,
                "count'": 5,
                "n": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 5,
                "n'": 1,
                "count'": 6,
                "n": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 6,
                "n'": 1,
                "count'": 6,
                "n": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 6,
                "n'": 0,
                "count'": 6,
                "n": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 6,
                "n'": 0,
                "count'": 6,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 6,
                "n'": 0,
                "count'": 6,
                "$ret'": 6,
                "n": 0,
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

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[35]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 35
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 35,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 7,
                "count'": 7,
                "n": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 7,
                "n'": 7,
                "count'": 7,
                "n": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 7,
                "n'": 1,
                "count'": 8,
                "n": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 8,
                "n'": 1,
                "count'": 8,
                "n": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 8,
                "n'": 0,
                "count'": 8,
                "n": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 8,
                "n'": 0,
                "count'": 8,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 8,
                "n'": 0,
                "count'": 8,
                "$ret'": 8,
                "n": 0,
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

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[56]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 56
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 56,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 11,
                "count'": 11,
                "n": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 11,
                "n'": 11,
                "count'": 11,
                "n": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 11,
                "n'": 2,
                "count'": 13,
                "n": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 13,
                "n'": 2,
                "count'": 13,
                "n": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 13,
                "n'": 0,
                "count'": 13,
                "n": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 13,
                "n'": 0,
                "count'": 13,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 13,
                "n'": 0,
                "count'": 13,
                "$ret'": 13,
                "n": 0,
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

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[74]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 74
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 74,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 14,
                "count'": 14,
                "n": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 14,
                "n'": 14,
                "count'": 14,
                "n": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 14,
                "n'": 2,
                "count'": 16,
                "n": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 16,
                "n'": 2,
                "count'": 16,
                "n": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 16,
                "n'": 0,
                "count'": 16,
                "n": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 16,
                "n'": 0,
                "count'": 16,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 16,
                "n'": 0,
                "count'": 16,
                "$ret'": 16,
                "n": 0,
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

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[94]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 94
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 94,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 18,
                "count'": 18,
                "n": 94,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 18,
                "n'": 18,
                "count'": 18,
                "n": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 18,
                "n'": 3,
                "count'": 21,
                "n": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 21,
                "n'": 3,
                "count'": 21,
                "n": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 21,
                "n'": 0,
                "count'": 21,
                "n": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 21,
                "n'": 0,
                "count'": 21,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 21,
                "n'": 0,
                "count'": 21,
                "$ret'": 21,
                "n": 0,
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

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[21]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 21
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 21,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 4,
                "count'": 4,
                "n": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 4,
                "n'": 4,
                "count'": 4,
                "n": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 4,
                "n'": 0,
                "count'": 4,
                "n": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 4,
                "n'": 0,
                "count'": 4,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 4,
                "n'": 0,
                "count'": 4,
                "$ret'": 4,
                "n": 0,
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

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[34]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 34
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 34,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 6,
                "count'": 6,
                "n": 34,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 6,
                "n'": 6,
                "count'": 6,
                "n": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 6,
                "n'": 1,
                "count'": 7,
                "n": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 7,
                "n'": 1,
                "count'": 7,
                "n": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 7,
                "n'": 0,
                "count'": 7,
                "n": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 7,
                "n'": 0,
                "count'": 7,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 7,
                "n'": 0,
                "count'": 7,
                "$ret'": 7,
                "n": 0,
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

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[18]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 18
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 18,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 3,
                "count'": 3,
                "n": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 3,
                "n'": 3,
                "count'": 3,
                "n": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 3,
                "n'": 0,
                "count'": 3,
                "n": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 3,
                "n'": 0,
                "count'": 3,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 3,
                "n'": 0,
                "count'": 3,
                "$ret'": 3,
                "n": 0,
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

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"trailing_zeroes\": {\"name\": \"trailing_zeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"n\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'trailing_zeroes'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"n\": \"*\"}}}}",
    "function": "trailing_zeroes",
    "inputs": "[]",
    "args": "[84]"
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
            "functionName": "trailing_zeroes",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "count'": 0,
                "n": 84
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "count'": 0,
                "n": 84,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "n'": 16,
                "count'": 16,
                "n": 84,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 16,
                "n'": 16,
                "count'": 16,
                "n": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 16,
                "n'": 3,
                "count'": 19,
                "n": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 19,
                "n'": 3,
                "count'": 19,
                "n": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 19,
                "n'": 0,
                "count'": 19,
                "n": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 19,
                "n'": 0,
                "count'": 19,
                "n": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "trailing_zeroes",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 19,
                "n'": 0,
                "count'": 19,
                "$ret'": 19,
                "n": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

