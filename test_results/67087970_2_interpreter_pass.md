# Test Report

Time: 2024-04-08 09:16:27.091296

### Base Program

```py
def main():
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

## Test Case 1

### Modified Program

```py
def main():
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
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
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
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
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
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
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
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
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
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
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
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
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
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
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
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
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
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
	inner_string = 'Hello'
	new_string = ''
	for char in inner_string:
		new_string = char + new_string
	return new_string
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_string\", \"val1\": {\"value\": \"\\\"Hello\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}], \"valueList\": [\"inner_string\", {\"value\": \"\\\"Hello\\\"\", \"line\": 2}]}, {\"val0\": \"new_string\", \"val1\": {\"value\": \"\\\"\\\"\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}], \"valueList\": [\"new_string\", {\"value\": \"\\\"\\\"\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"inner_string\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"inner_string\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"new_string\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"new_string\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"char\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"char\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"new_string\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"new_string\", {\"name\": \"Add\", \"args\": [{\"name\": \"char\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"new_string\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"inner_string\": \"*\", \"ind#0\": \"int\", \"char\": \"*\", \"iter#0\": \"int\", \"new_string\": \"*\"}}}}",
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
                "inner_string": "<undef>",
                "new_string'": "",
                "ind#0'": 0,
                "iter#0'": "Hello",
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "inner_string'": "Hello",
                "new_string": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "",
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": "Hello",
                "ind#0": 0,
                "iter#0": "Hello",
                "inner_string'": "Hello",
                "new_string": "",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "char": "<undef>",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "H",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "H",
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "H",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "char": "H",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "eH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "e",
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "eH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "char": "e",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "leH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "leH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "lleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "l",
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 4,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "lleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "char": "l",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 2,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": true,
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "inner_string'": "Hello"
            },
            "isChecked": false
        },
        {
            "functionName": "main",
            "location": 3,
            "mem": {
                "inner_string": "Hello",
                "new_string'": "olleH",
                "iter#0'": "Hello",
                "new_string": "olleH",
                "$cond": false,
                "$ret": "<undef>",
                "char'": "o",
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "char": "o",
                "iter#0": "Hello",
                "$ret'": "olleH",
                "inner_string'": "Hello"
            },
            "isChecked": false
        }
    ]
}
```

</details>

