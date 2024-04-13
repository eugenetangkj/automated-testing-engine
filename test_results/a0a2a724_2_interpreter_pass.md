# Test Report

Time: 2024-04-13 16:10:21.184371

### Base Program

```py
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

## Test Case 1

### Modified Program

```py
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[91, 20, 80]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 91,
                "result'": -78,
                "b": 20,
                "c": 80,
                "$ret'": -78,
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
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[77, 63, 58]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 77,
                "result'": 111,
                "b": 63,
                "c": 58,
                "$ret'": 111,
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
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[81, 54, 19]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 81,
                "result'": 248,
                "b": 54,
                "c": 19,
                "$ret'": 248,
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
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[6, 76, 52]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 6,
                "result'": 32,
                "b": 76,
                "c": 52,
                "$ret'": 32,
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
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[8, 75, 82]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 8,
                "result'": -87,
                "b": 75,
                "c": 82,
                "$ret'": -87,
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
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[19, 87, 25]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 19,
                "result'": 199,
                "b": 87,
                "c": 25,
                "$ret'": 199,
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
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[37, 48, 52]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 37,
                "result'": 10,
                "b": 48,
                "c": 52,
                "$ret'": 10,
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
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[58, 49, 32]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 58,
                "result'": 135,
                "b": 49,
                "c": 32,
                "$ret'": 135,
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
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[59, 38, 31]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 59,
                "result'": 108,
                "b": 38,
                "c": 31,
                "$ret'": 108,
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
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[47, 37, 25]"
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
            "functionName": "random_calculation",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "a": 47,
                "result'": 105,
                "b": 37,
                "c": 25,
                "$ret'": 105,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

