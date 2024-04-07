# Test Report

Time: 2024-04-07 07:43:46.235614

### Base Program

```py
def main(p):
	p = p + 5
	return p
```

## Test Case 1

### Modified Program

```py
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[1]"
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
                "p": 1,
                "p'": 6,
                "$ret'": 6,
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
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
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
                "p": 85,
                "p'": 90,
                "$ret'": 90,
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
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[72]"
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
                "p": 72,
                "p'": 77,
                "$ret'": 77,
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
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[42]"
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
                "p": 42,
                "p'": 47,
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
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
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
                "p": 62,
                "p'": 67,
                "$ret'": 67,
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
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
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
                "p": 92,
                "p'": 97,
                "$ret'": 97,
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
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[8]"
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
                "p": 8,
                "p'": 13,
                "$ret'": 13,
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
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[89]"
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
                "p": 89,
                "p'": 94,
                "$ret'": 94,
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
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[12]"
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
                "p": 12,
                "p'": 17,
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
def main(p):
	p = p + 5
	return p
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"p\", \"val1\": \"*\", \"valueArray\": [\"p\", \"*\"], \"valueList\": [\"p\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"p\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"p\", {\"name\": \"Add\", \"args\": [{\"name\": \"p\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"p\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"p\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"p\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[75]"
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
                "p": 75,
                "p'": 80,
                "$ret'": 80,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

