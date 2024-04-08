# Test Report

Time: 2024-04-08 07:53:40.213461

### Base Program

```py
def main():
	return 1
```

## Test Case 1

### Modified Program

```py
def main():
	try:
		return 1
	except:
		return 0
```

<details>
<summary>feedback_fix endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"$ret\", {\"value\": \"1\", \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"$ret\", {\"value\": \"0\", \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

Message: 
```
Feedback fix endpoint failed
```

Actual Output: 
```json
[
    {
        "lineNumber": 5,
        "oldExpr": "0",
        "newExpr": "1",
        "repairStrings": [
            "Wrong assignment. Change return 0 to return 1"
        ]
    }
]
```

</details>

