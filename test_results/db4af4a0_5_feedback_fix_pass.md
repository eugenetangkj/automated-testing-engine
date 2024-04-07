# Test Report

Time: 2024-04-07 08:48:53.797237

### Base Program

```py
def main(a, b):
	sum = a + b
	return sum
```

## Test Case 1

### Modified Program

```py
def main(a, b):
    sum = a + b
    return sum
```

<details>
<summary>feedback_fix endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"sum\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"sum\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[19, 22], [31, 40], [86, 10], [11, 80], [97, 6], [39, 49], [51, 36], [68, 95], [60, 46], [34, 22]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
def main(a, b):
    a = a
    a = a
    a = a
    a = a
    a = a
    b = b
    b = b
    b = b
    b = b
    b = b
    sum = a + b
    return sum
```

<details>
<summary>feedback_fix endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"sum\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"a\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"a\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}, {\"val0\": \"b\", \"val1\": {\"name\": \"b\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"b\", {\"name\": \"b\", \"primed\": false, \"line\": 7}], \"valueList\": [\"b\", {\"name\": \"b\", \"primed\": false, \"line\": 7}]}, {\"val0\": \"sum\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12}], \"valueList\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 13}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"a\": \"*\", \"b\": \"*\", \"sum\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[19, 22], [31, 40], [86, 10], [11, 80], [97, 6], [39, 49], [51, 36], [68, 95], [60, 46], [34, 22]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

