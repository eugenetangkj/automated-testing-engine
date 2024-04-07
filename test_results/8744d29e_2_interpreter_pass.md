# Test Report

Time: 2024-04-07 07:40:14.856207

### Base Program

```py
def main(v):
	v = v + 5
	return v
```

## Test Case 1

### Modified Program

```py
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[30]"
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
                "v'": 35,
                "v": 30,
                "$ret'": 35,
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
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
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
                "v'": 31,
                "v": 26,
                "$ret'": 31,
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
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[63]"
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
                "v'": 68,
                "v": 63,
                "$ret'": 68,
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
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
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
                "v'": 64,
                "v": 59,
                "$ret'": 64,
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
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[53]"
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
                "v'": 58,
                "v": 53,
                "$ret'": 58,
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
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
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
                "v'": 73,
                "v": 68,
                "$ret'": 73,
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
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
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
                "v'": 67,
                "v": 62,
                "$ret'": 67,
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
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
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
                "v'": 57,
                "v": 52,
                "$ret'": 57,
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
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
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
                "v'": 71,
                "v": 66,
                "$ret'": 71,
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
def main(v):
	v = v + 5
	return v
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
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
                "v'": 64,
                "v": 59,
                "$ret'": 64,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

