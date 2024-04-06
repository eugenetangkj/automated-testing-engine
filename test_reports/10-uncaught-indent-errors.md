# Issue 10: Uncaught Indent Errors

## Description
We believe that the parser removes whitespace. Thus, when the parser intermediates of base and modified programs are put into the `error_localizer`, `feedback_error`, `feedback_fix` and `repair` endpoints, the endpoints detect that both programs are equivalent, despite the modified program having indentation error. In Python, the modified programs should raise an `IndentationError` instead of being deemed as syntatically correct.

### Base Program

```py
def main():
	x = 2
	return x
```

### Modified Program
```py
def main():
	x = 2
		return x
```

### Input
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

### Output

#### Error Localizer
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

#### Feedback Error
```json
None
```

#### Feedback Fix
```json
None
```

#### Repair
```json
[
    {
        "totalCost": 0.0,
        "localRepairs": []
    }
]
```

## Related Test Reports
Refer to Test Report ID 4564d0fe.