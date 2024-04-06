# Test Report

Time: 2024-04-06 12:59:15.092452

### Base Program

```py
def main():
	x = 2
	return x
```

## Test Case 1

### Modified Program

```py
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
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
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
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
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
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
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
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
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
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
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
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
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
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
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
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
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
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
def main():
	x = 2
	return x
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[]"
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
                "x": "<undef>",
                "$ret'": 2,
                "x'": 2,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

