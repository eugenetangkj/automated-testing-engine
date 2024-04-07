# Test Report

Time: 2024-04-07 15:52:26.024916

### Base Program

```py
def main(g, h):
	diff = g - h
	return diff
```

## Test Case 1

### Modified Program

```py
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[48, 58]"
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
                "diff'": -10,
                "g": 48,
                "h": 58,
                "diff": "<undef>",
                "$ret'": -10,
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
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[14, 1]"
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
                "diff'": 13,
                "g": 14,
                "h": 1,
                "diff": "<undef>",
                "$ret'": 13,
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
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[39, 97]"
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
                "diff'": -58,
                "g": 39,
                "h": 97,
                "diff": "<undef>",
                "$ret'": -58,
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
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[75, 65]"
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
                "diff'": 10,
                "g": 75,
                "h": 65,
                "diff": "<undef>",
                "$ret'": 10,
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
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[35, 92]"
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
                "diff'": -57,
                "g": 35,
                "h": 92,
                "diff": "<undef>",
                "$ret'": -57,
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
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[26, 68]"
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
                "diff'": -42,
                "g": 26,
                "h": 68,
                "diff": "<undef>",
                "$ret'": -42,
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
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[79, 37]"
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
                "diff'": 42,
                "g": 79,
                "h": 37,
                "diff": "<undef>",
                "$ret'": 42,
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
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[63, 13]"
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
                "diff'": 50,
                "g": 63,
                "h": 13,
                "diff": "<undef>",
                "$ret'": 50,
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
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[57, 40]"
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
                "diff'": 17,
                "g": 57,
                "h": 40,
                "diff": "<undef>",
                "$ret'": 17,
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
def main(g, h):
	diff = g - h
	return diff
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"g\", \"val1\": \"*\", \"valueArray\": [\"g\", \"*\"], \"valueList\": [\"g\", \"*\"]}, {\"val0\": \"h\", \"val1\": \"*\", \"valueArray\": [\"h\", \"*\"], \"valueList\": [\"h\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"g\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"h\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[100, 32]"
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
                "diff'": 68,
                "g": 100,
                "h": 32,
                "diff": "<undef>",
                "$ret'": 68,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

