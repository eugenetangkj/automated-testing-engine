# Test Report

Time: 2024-04-14 07:34:40.335462

### Base Program

```py
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

## Test Case 1

### Modified Program

```py
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[19, 43, 89]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 19,
                "b": 43,
                "c": 89,
                "$ret'": 89,
                "max_num'": 89,
                "max_num": "<undef>",
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
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[36, 99, 12]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 36,
                "b": 99,
                "c": 12,
                "$ret'": 99,
                "max_num'": 99,
                "max_num": "<undef>",
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
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[76, 48, 63]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 76,
                "b": 48,
                "c": 63,
                "$ret'": 76,
                "max_num'": 76,
                "max_num": "<undef>",
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
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[69, 45, 16]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 69,
                "b": 45,
                "c": 16,
                "$ret'": 69,
                "max_num'": 69,
                "max_num": "<undef>",
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
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[20, 55, 53]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 20,
                "b": 55,
                "c": 53,
                "$ret'": 55,
                "max_num'": 55,
                "max_num": "<undef>",
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
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[32, 10, 49]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 32,
                "b": 10,
                "c": 49,
                "$ret'": 49,
                "max_num'": 49,
                "max_num": "<undef>",
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
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[42, 7, 83]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 42,
                "b": 7,
                "c": 83,
                "$ret'": 83,
                "max_num'": 83,
                "max_num": "<undef>",
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
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[36, 31, 96]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 36,
                "b": 31,
                "c": 96,
                "$ret'": 96,
                "max_num'": 96,
                "max_num": "<undef>",
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
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[75, 49, 51]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 75,
                "b": 49,
                "c": 51,
                "$ret'": 75,
                "max_num'": 75,
                "max_num": "<undef>",
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
def find_largest_number(a, b, c):
    max_num = max(a, b, c)
    return max_num
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"find_largest_number\": {\"name\": \"find_largest_number\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_num\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"max_num\", {\"name\": \"max\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"max_num\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"max_num\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_largest_number'\"}, \"types\": {\"max_num\": \"*\"}}}}",
    "function": "find_largest_number",
    "inputs": "[]",
    "args": "[72, 4, 39]"
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
            "functionName": "find_largest_number",
            "location": 1,
            "mem": {
                "a": 72,
                "b": 4,
                "c": 39,
                "$ret'": 72,
                "max_num'": 72,
                "max_num": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

