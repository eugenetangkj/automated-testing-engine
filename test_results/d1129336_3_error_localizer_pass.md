# Test Report

Time: 2024-03-31 15:03:54.594746

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
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[[56], [71], [17], [16], [48], [17], [11], [29], [44], [2]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

## Test Case 2

### Modified Program

```py
def double(var_0):
    d = float(var_0)
    return d + d
```

<details>
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_0\", \"val1\": \"*\", \"valueArray\": [\"var_0\", \"*\"], \"valueList\": [\"var_0\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[[56], [71], [17], [16], [48], [17], [11], [29], [44], [2]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

## Test Case 3

### Modified Program

```py
def double(var_1):
    d = float(var_1)
    return d + d
```

<details>
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"n\", \"val1\": \"*\", \"valueArray\": [\"n\", \"*\"], \"valueList\": [\"n\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"double\": {\"name\": \"double\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_1\", \"val1\": \"*\", \"valueArray\": [\"var_1\", \"*\"], \"valueList\": [\"var_1\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"d\", \"val1\": {\"name\": \"float\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"d\", {\"name\": \"float\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"d\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'double'\"}, \"types\": {\"d\": \"*\"}}}}",
    "function": "double",
    "inputs": "[]",
    "args": "[[56], [71], [17], [16], [48], [17], [11], [29], [44], [2]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

