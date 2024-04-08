# Test Report

Time: 2024-04-08 07:48:46.309533

### Base Program

```py
def main():
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

## Test Case 1

### Modified Program

```py
def main():
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
                "$ret'": true,
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
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
                "$ret'": true,
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
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
                "$ret'": true,
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
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
                "$ret'": true,
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
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
                "$ret'": true,
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
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
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
def main():
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
                "$ret'": true,
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
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
                "$ret'": true,
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
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
                "$ret'": true,
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
	curr_string = 'Hello World'
	if 'Hello' in curr_string:
		return True
	return False
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"curr_string\", \"val1\": {\"value\": \"\\\"Hello World\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}], \"valueList\": [\"curr_string\", {\"value\": \"\\\"Hello World\\\"\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"In\", \"args\": [{\"value\": \"\\\"Hello\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"curr_string\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"value\": \"False\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"curr_string\": \"*\"}}}}",
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
                "curr_string'": "Hello World",
                "curr_string": "<undef>",
                "$ret'": true,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

