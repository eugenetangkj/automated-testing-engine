# Test Report

Time: 2024-04-06 13:58:39.637942

### Base Program

```py
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

## Test Case 1

### Modified Program

```py
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[78, 40, 40]"
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
                "a": 78,
                "b": 40,
                "c": 40,
                "$ret'": false,
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
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[0, 52, 55]"
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
                "a": 0,
                "b": 52,
                "c": 55,
                "$ret'": false,
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
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[82, 55, 84]"
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
                "a": 82,
                "b": 55,
                "c": 84,
                "$ret'": false,
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
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[58, 97, 77]"
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
                "a": 58,
                "b": 97,
                "c": 77,
                "$ret'": false,
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
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[92, 56, 65]"
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
                "a": 92,
                "b": 56,
                "c": 65,
                "$ret'": false,
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
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[42, 4, 51]"
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
                "a": 42,
                "b": 4,
                "c": 51,
                "$ret'": true,
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
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[67, 41, 51]"
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
                "a": 67,
                "b": 41,
                "c": 51,
                "$ret'": false,
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
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[40, 79, 21]"
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
                "a": 40,
                "b": 79,
                "c": 21,
                "$ret'": false,
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
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[65, 80, 98]"
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
                "a": 65,
                "b": 80,
                "c": 98,
                "$ret'": false,
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
def test_function(a, b, c):
    if a > 100 or (b < 20 and c > 30):
        return True
    else:
        return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"test_function\": {\"name\": \"test_function\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Or\", \"args\": [{\"name\": \"Gt\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"100\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"20\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"30\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_function'\"}, \"types\": {}}}}",
    "function": "test_function",
    "inputs": "[]",
    "args": "[20, 14, 83]"
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
                "a": 20,
                "b": 14,
                "c": 83,
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

