# Test Report

Time: 2024-04-14 11:21:17.194306

### Base Program

```py
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

## Test Case 1

### Modified Program

```py
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[27, 6]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 27,
                "b": 6
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
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[65, 49]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 65,
                "b": 49
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
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[13, 85]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 13,
                "b": 85
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
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[71, 64]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 71,
                "b": 64
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
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[47, 59]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 47,
                "b": 59
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
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[36, 22]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 36,
                "b": 22
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
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[77, 82]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 77,
                "b": 82
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
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[63, 29]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 63,
                "b": 29
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
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[25, 44]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 25,
                "b": 44
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
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"multiply_numbers\": {\"name\": \"multiply_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": []}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply_numbers'\"}, \"types\": {}}}}",
    "function": "multiply_numbers",
    "inputs": "[]",
    "args": "[12, 38]"
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
            "functionName": "multiply_numbers",
            "location": 1,
            "mem": {
                "a": 12,
                "b": 38
            },
            "isChecked": false
        }
    ]
}
```

</details>

