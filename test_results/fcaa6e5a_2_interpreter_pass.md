# Test Report

Time: 2024-04-06 15:51:15.591557

### Base Program

```py
def main():
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

## Test Case 1

### Modified Program

```py
def main():
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
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
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
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
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
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
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
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
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
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
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
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
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
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
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
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
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
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
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
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
                "original_list": "<undef>",
                "ind#0'": 0,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": "<undef>",
                "ind#0": "<undef>",
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "ind#0'": 0,
                "$cond'": true,
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": "<undef>",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [],
                "$cond": true,
                "number": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2
                ],
                "$cond": true,
                "number": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": true,
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "number'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "original_list": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "original_list'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list'": [
                    2,
                    4
                ],
                "iter#0'": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "filtered_list": [
                    2,
                    4
                ],
                "$cond": false,
                "$ret": "<undef>",
                "number": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    1,
                    2,
                    3,
                    4,
                    5
                ],
                "$ret'": [
                    2,
                    4
                ],
                "number'": 5
            },
            "isChecked": false
        }
    ]
}
```

</details>

