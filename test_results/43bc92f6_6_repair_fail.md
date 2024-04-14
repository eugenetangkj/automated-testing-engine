# Test Report

Time: 2024-04-14 07:02:06.238650

### Base Program

```py
def calculate_average(a, b, c):
	return (a + b + c) / 3
```

## Test Case 1

### Modified Program

```py
def calculate_average(a, b, c):
    return (a + b + c) / 3
```

<details>
<summary>repair endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_average\": {\"name\": \"calculate_average\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Div\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Div\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_average'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_average\": {\"name\": \"calculate_average\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Div\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Div\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_average'\"}, \"types\": {}}}}",
    "function": "calculate_average",
    "inputs": "[]",
    "args": "[[26, 90, 41], [79, 62, 48], [54, 56, 61], [100, 66, 1], [71, 100, 88], [14, 16, 65], [3, 20, 97], [9, 51, 31], [7, 77, 77], [13, 96, 47]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
[
    {
        "totalCost": 0.0,
        "localRepairs": []
    }
]
```

</details>

## Test Case 2

### Modified Program

```py
def calculate_average(a, b, c):
    (a, b, c) = (c, b, a)
    return (c + b + a) / 3
```

<details>
<summary>repair endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_average\": {\"name\": \"calculate_average\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Div\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Div\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_average'\"}, \"types\": {}}}}",
    "student_solution": "null",
    "function": "calculate_average",
    "inputs": "[]",
    "args": "[[26, 90, 41], [79, 62, 48], [54, 56, 61], [100, 66, 1], [71, 100, 88], [14, 16, 65], [3, 20, 97], [9, 51, 31], [7, 77, 77], [13, 96, 47]]"
}
```

Message: 
```
Exception
Error in making API call to https://its.comp.nus.edu.sg/cs3213/repair. (Retry 0 times)
Status code: 500.
Response: {"detail":"Output: sg.edu.nus.se.its.alignment.AlignmentException: Programs cannot be null\n\nError: sg.edu.nus.se.its.alignment.AlignmentException: Programs cannot be null\n\tat sg.edu.nus.se.its.alignment.CfgBasedStructuralAlignment.generateStructuralAlignment(CfgBasedStructuralAlignment.java:32)\n\tat sg.edu.nus.se.its.repair.RepairProgram.main(RepairProgram.java:164)\nException in thread \"main\" java.lang.RuntimeException: sg.edu.nus.se.its.alignment.AlignmentException: Programs cannot be null\n\tat sg.edu.nus.se.its.repair.RepairProgram.main(RepairProgram.java:185)\nCaused by: sg.edu.nus.se.its.alignment.AlignmentException: Programs cannot be null\n\tat sg.edu.nus.se.its.alignment.CfgBasedStructuralAlignment.generateStructuralAlignment(CfgBasedStructuralAlignment.java:32)\n\tat sg.edu.nus.se.its.repair.RepairProgram.main(RepairProgram.java:164)\n"}
```

Actual Output: None

</details>

