# Test Report

Time: 2024-04-06 10:21:37.682803

### Base Program

```py
def main():
	 return {'key1': 1, 'key2': 2 }
```

## Test Case 1

### Modified Program

```py
def main():
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
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
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
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
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
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
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
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
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
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
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
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
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
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
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
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
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
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
	 return {'key1': 1, 'key2': 2 }
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [{\"value\": \"\\\"key1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"key2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
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
                "$ret'": {
                    "key1": 1,
                    "key2": 2
                },
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

