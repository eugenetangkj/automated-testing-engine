# Test Report

Time: 2024-04-14 07:37:40.760330

### Base Program

```py
def product_of_two_numbers(x, y):
	return x * y
```

## Test Case 1

### Modified Program

```py
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[4, 19]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 4,
                "y": 19,
                "$ret'": 76,
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
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[76, 50]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 76,
                "y": 50,
                "$ret'": 3800,
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
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[15, 4]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 15,
                "y": 4,
                "$ret'": 60,
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
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[10, 44]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 10,
                "y": 44,
                "$ret'": 440,
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
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[32, 23]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 32,
                "y": 23,
                "$ret'": 736,
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
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[74, 5]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 74,
                "y": 5,
                "$ret'": 370,
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
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[12, 20]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 12,
                "y": 20,
                "$ret'": 240,
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
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[1, 8]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 1,
                "y": 8,
                "$ret'": 8,
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
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[25, 34]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 25,
                "y": 34,
                "$ret'": 850,
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
def product_of_two_numbers(x, y):
	return x * y
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"product_of_two_numbers\": {\"name\": \"product_of_two_numbers\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'product_of_two_numbers'\"}, \"types\": {}}}}",
    "function": "product_of_two_numbers",
    "inputs": "[]",
    "args": "[4, 73]"
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
            "functionName": "product_of_two_numbers",
            "location": 1,
            "mem": {
                "x": 4,
                "y": 73,
                "$ret'": 292,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

