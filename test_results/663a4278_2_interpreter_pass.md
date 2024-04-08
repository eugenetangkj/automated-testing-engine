# Test Report

Time: 2024-04-07 07:37:26.525831

### Base Program

```py
def main(z):
	z = z + 5
	return z
```

## Test Case 1

### Modified Program

```py
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[46]"
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
                "z": 46,
                "$ret'": 51,
                "z'": 51,
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
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[97]"
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
                "z": 97,
                "$ret'": 102,
                "z'": 102,
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
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[79]"
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
                "z": 79,
                "$ret'": 84,
                "z'": 84,
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
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[56]"
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
                "z": 56,
                "$ret'": 61,
                "z'": 61,
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
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
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
                "z": 21,
                "$ret'": 26,
                "z'": 26,
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
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
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
                "z": 100,
                "$ret'": 105,
                "z'": 105,
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
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[98]"
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
                "z": 98,
                "$ret'": 103,
                "z'": 103,
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
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[26]"
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
                "z": 26,
                "$ret'": 31,
                "z'": 31,
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
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[48]"
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
                "z": 48,
                "$ret'": 53,
                "z'": 53,
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
def main(z):
	z = z + 5
	return z
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"z\", \"val1\": \"*\", \"valueArray\": [\"z\", \"*\"], \"valueList\": [\"z\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"z\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"z\", {\"name\": \"Add\", \"args\": [{\"name\": \"z\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"z\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"z\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"z\": \"*\"}}}}",
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
                "z": 100,
                "$ret'": 105,
                "z'": 105,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

