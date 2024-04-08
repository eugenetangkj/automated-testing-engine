# Test Report

Time: 2024-04-07 08:46:45.702682

### Base Program

```py
def main(a):
	return a
```

## Test Case 1

### Modified Program

```py
def main(a):
    return a
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[50], [27], [100], [91], [21], [100], [10], [7], [52], [84]]"
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
def main(a):
    a = a
    a = a
    a = a
    a = a
    a = a
    return a
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"a\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"a\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"a\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"a\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"a\", \"primed\": true, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"a\", \"primed\": true, \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"a\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[50], [27], [100], [91], [21], [100], [10], [7], [52], [84]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

