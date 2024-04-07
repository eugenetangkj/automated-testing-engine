# Test Report

Time: 2024-04-07 08:46:39.367864

### Base Program

```py
def main(a):
	return a
```

## Test Case 1

### Modified Program

```py
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[50]"
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
                "a": 50,
                "$ret'": 50,
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
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "a": 27,
                "$ret'": 27,
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
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[100]"
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
                "a": 100,
                "$ret'": 100,
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
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[91]"
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
                "a": 91,
                "$ret'": 91,
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
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "a": 21,
                "$ret'": 21,
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
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[100]"
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
                "a": 100,
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
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[10]"
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
                "a": 10,
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
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[7]"
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
                "a": 7,
                "$ret'": 7,
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
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[52]"
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
                "a": 52,
                "$ret'": 52,
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
def main(a):
	return a
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "a": 84,
                "$ret'": 84,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

