# Test Report

Time: 2024-04-08 07:38:38.492500

### Base Program

```py
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

## Test Case 1

### Modified Program

```py
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
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
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 68,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
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
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[9]"
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
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 9,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
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
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
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
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 68,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
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
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[77]"
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
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 77,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
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
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
    "function": "main",
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
            "functionName": "main",
            "location": 1,
            "mem": {
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 17,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
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
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[93]"
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
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 93,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
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
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[76]"
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
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 76,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
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
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
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
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 62,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
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
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[96]"
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
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 96,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
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
def main(y):
	original_list = [1, 2, 3, 4, 5]
	new_list = original_list[0:5]
	return new_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"new_list\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"new_list\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"new_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"new_list\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"original_list\": \"*\", \"new_list\": \"*\"}}}}",
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
                "original_list": "<undef>",
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "y": 91,
                "new_list": "<undef>",
                "new_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

