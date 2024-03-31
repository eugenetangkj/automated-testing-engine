# Test Report

Time: 2024-03-31 15:03:49.785862

### Base Program

```py
def double(n):
	d = float(n)
	return d + d
```

## Test Case 1

### Modified Program

```py
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 56.0,
                "d": "<undef>",
                "$ret'": 112.0,
                "n": 56,
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
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[71]"
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 71.0,
                "d": "<undef>",
                "$ret'": 142.0,
                "n": 71,
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
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[17]"
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 17.0,
                "d": "<undef>",
                "$ret'": 34.0,
                "n": 17,
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
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[16]"
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 16.0,
                "d": "<undef>",
                "$ret'": 32.0,
                "n": 16,
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
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 48.0,
                "d": "<undef>",
                "$ret'": 96.0,
                "n": 48,
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
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[17]"
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 17.0,
                "d": "<undef>",
                "$ret'": 34.0,
                "n": 17,
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
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[11]"
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 11.0,
                "d": "<undef>",
                "$ret'": 22.0,
                "n": 11,
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
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[29]"
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 29.0,
                "d": "<undef>",
                "$ret'": 58.0,
                "n": 29,
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
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[44]"
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 44.0,
                "d": "<undef>",
                "$ret'": 88.0,
                "n": 44,
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
def double(n):
	d = float(n)
	return d + d

```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[2]"
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
            "functionName": "double",
            "location": 1,
            "mem": {
                "d'": 2.0,
                "d": "<undef>",
                "$ret'": 4.0,
                "n": 2,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

