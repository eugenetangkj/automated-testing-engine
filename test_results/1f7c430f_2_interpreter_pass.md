# Test Report

Time: 2024-04-07 07:22:19.325498

### Base Program

```py
def main(x):
	x = x + 5
	return x
```

## Test Case 1

### Modified Program

```py
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[66]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 66,
                "$ret'": 71,
                "x'": 71,
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
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[59]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 59,
                "$ret'": 64,
                "x'": 64,
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
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[64]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 64,
                "$ret'": 69,
                "x'": 69,
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
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[24]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 24,
                "$ret'": 29,
                "x'": 29,
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
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[85]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 85,
                "$ret'": 90,
                "x'": 90,
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
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[62]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 62,
                "$ret'": 67,
                "x'": 67,
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
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[68]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 68,
                "$ret'": 73,
                "x'": 73,
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
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[47]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 47,
                "$ret'": 52,
                "x'": 52,
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
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[92]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 92,
                "$ret'": 97,
                "x'": 97,
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
def main(x):
	x = x + 5
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"x\", {\"name\": \"Add\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[36]"
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "x": 36,
                "$ret'": 41,
                "x'": 41,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

