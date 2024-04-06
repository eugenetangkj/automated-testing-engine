# Test Report

Time: 2024-04-06 15:16:44.602757

### Base Program

```py
def test_string():
	return ('Part 1'
	'Part 2'
	'Part 3')
```

## Test Case 1

### Modified Program

```py
def test_string():
	return 'Part 1' + 'Part 2' + 'Part 3'
```

<details>
<summary>feedback_fix endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"test_string\": {\"name\": \"test_string\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_string'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"test_string\": {\"name\": \"test_string\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"\\\"Part 1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"Part 2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"\\\"Part 3\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"\\\"Part 1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"Part 2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"\\\"Part 3\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"\\\"Part 1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"Part 2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"\\\"Part 3\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_string'\"}, \"types\": {}}}}",
    "function": "test_string",
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
        "lineNumber": 2,
        "oldExpr": "return ((\"Part 1\" + \"Part 2\") + \"Part 3\")",
        "newExpr": "return {}",
        "repairStrings": [
            "Wrong expression. Change return ((\"Part 1\" + \"Part 2\") + \"Part 3\"); to return {};"
        ]
    }
]
```

</details>

