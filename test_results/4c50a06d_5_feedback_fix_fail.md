# Test Report

Time: 2024-04-08 04:56:18.666567

### Base Program

```py
def main():
	my_list = [1, 2, 3, 4, 5]
	total = 1 + 2 + 3 + 4 + 5
	return total
```

## Test Case 1

### Modified Program

```py
def main():
	my_list = [1, 2, 3, 4, 5]
	total = 0
	total = my_list[0]
	total += my_list[1]
	total += my_list[2]
	total += my_list[3]
	total += my_list[4]
	return total
```

<details>
<summary>feedback_fix endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"my_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"total\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"4\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"total\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"4\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"total\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"4\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"total\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"total\": \"*\", \"my_list\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"my_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"total\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"total\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"total\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"total\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 9}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"total\": \"*\", \"my_list\": \"*\"}}}}",
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
        "lineNumber": 2,
        "oldExpr": "my_list = [1, 2, 3, 4, 5]",
        "newExpr": "my_list = ((((1 + 2) + 3) + 4) + 5)",
        "repairStrings": [
            "Wrong expression. Change my_list = [1, 2, 3, 4, 5]; to my_list = ((((1 + 2) + 3) + 4) + 5);"
        ]
    },
    {
        "lineNumber": 8,
        "oldExpr": "total = AssAdd(AssAdd(AssAdd(GetElement(my_list', 0), GetElement(my_list', 1)), GetElement(my_list', 2)), GetElement(my_list', 3)) += my_list[4]",
        "newExpr": "total = [1, 2, 3, 4, 5]",
        "repairStrings": [
            "Wrong Expression. total = AssAdd(AssAdd(AssAdd(GetElement(my_list', 0), GetElement(my_list', 1)), GetElement(my_list', 2)), GetElement(my_list', 3)) += my_list[4]; to total = [1, 2, 3, 4, 5];"
        ]
    },
    {
        "lineNumber": 9,
        "oldExpr": null,
        "newExpr": null,
        "repairStrings": []
    }
]
```

</details>

