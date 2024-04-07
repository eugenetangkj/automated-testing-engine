# Test Report

Time: 2024-04-07 08:17:25.985356

### Base Program

```py
def main(y):
	return y
```

## Test Case 1

### Modified Program

```py
def main(y):
	y = y
	y = y
	y = y
	y = y
	y = y
	return y
```

<details>
<summary>error_localizer endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"y\", \"primed\": false, \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"y\", \"primed\": false, \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"y\", \"val1\": {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"y\", {\"name\": \"y\", \"primed\": false, \"line\": 2}], \"valueList\": [\"y\", {\"name\": \"y\", \"primed\": false, \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"y\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"y\", \"primed\": true, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"y\", \"primed\": true, \"line\": 7}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"y\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[56], [39], [82], [25], [61], [62], [71], [7], [70], [22]]"
}
```

Message: 
```
Exception
Error in making API call to https://its.comp.nus.edu.sg/cs3213/errorlocalizer. (Retry 0 times)
Status code: 500.
Response: Internal Server Error
```

Actual Output: None

</details>

