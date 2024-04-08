# Test Report

Time: 2024-04-08 09:44:04.492407

### Base Program

```py
def main():
	inner_list = [1, 2, 3, 4, 5]
	sum = inner_list[1] + inner_list[2] + inner_list[3]
	return sum
```

## Test Case 1

### Modified Program

```py
def main():
	inner_list = [5, 4, 3, 2, 1]
	sum = inner_list[3] + inner_list[2] + inner_list[1]
	return sum
```

<details>
<summary>feedback_error endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"inner_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"inner_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"sum\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"inner_list\": \"*\", \"sum\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"inner_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"inner_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"sum\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"inner_list\": \"*\", \"sum\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

Message: 
```
Feedback error endpoint failed
```

Actual Output: 
```json
[
    {
        "lineNumber": 2,
        "hintStrings": []
    }
]
```

</details>

