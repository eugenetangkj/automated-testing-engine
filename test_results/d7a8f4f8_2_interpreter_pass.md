# Test Report

Time: 2024-04-06 13:48:54.851543

### Base Program

```py
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

## Test Case 1

### Modified Program

```py
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[4, 54, 62, 4]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 4,
                "b": 54,
                "c": 62,
                "d": 4,
                "c'": 58,
                "$ret'": 58,
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
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[54, 86, 98, 21]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 54,
                "b": 86,
                "c": 98,
                "d": 21,
                "c'": 75,
                "$ret'": 75,
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
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[83, 34, 89, 23]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 83,
                "b": 34,
                "c": 89,
                "d": 23,
                "c'": 106,
                "$ret'": 106,
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
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[15, 87, 60, 32]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 15,
                "b": 87,
                "c": 60,
                "d": 32,
                "c'": 47,
                "$ret'": 47,
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
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[93, 19, 34, 47]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 93,
                "b": 19,
                "c": 34,
                "d": 47,
                "c'": 140,
                "$ret'": 140,
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
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[52, 100, 12, 48]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 52,
                "b": 100,
                "c": 12,
                "d": 48,
                "c'": 100,
                "$ret'": 100,
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
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[15, 51, 49, 1]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 15,
                "b": 51,
                "c": 49,
                "d": 1,
                "c'": 16,
                "$ret'": 16,
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
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[33, 11, 13, 47]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 33,
                "b": 11,
                "c": 13,
                "d": 47,
                "c'": 80,
                "$ret'": 80,
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
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[64, 82, 36, 8]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 64,
                "b": 82,
                "c": 36,
                "d": 8,
                "c'": 72,
                "$ret'": 72,
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
def test_function(a, b, c, d):
	c = (a if a > 5 else b) + (c if c < 10 else d)
	return c
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}, {\"val0\": \"d\", \"val1\": \"*\", \"valueArray\": [\"d\", \"*\"], \"valueList\": [\"d\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"c\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"c\", {\"name\": \"Add\", \"args\": [{\"name\": \"ite\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"c\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"c\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {\"c\": \"*\"}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[12, 68, 19, 43]"
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
            "functionName": "test_function",
            "location": 1,
            "mem": {
                "a": 12,
                "b": 68,
                "c": 19,
                "d": 43,
                "c'": 55,
                "$ret'": 55,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

