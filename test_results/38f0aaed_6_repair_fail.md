# Test Report

Time: 2024-04-07 15:48:01.652753

### Base Program

```py
def main(x, y):
	diff = x- y
	return diff
```

## Test Case 1

### Modified Program

```py
def main(x, y):
    diff = x - y
    return diff
```

<details>
<summary>repair endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[87, 93], [66, 9], [87, 12], [51, 8], [51, 68], [83, 2], [98, 82], [96, 30], [96, 74], [84, 13]]"
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
def main(x, y):
    (x, y) = (y, x)
    diff = y - x
    return diff
```

<details>
<summary>repair endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "student_solution": "null",
    "function": "main",
    "inputs": "[]",
    "args": "[[87, 93], [66, 9], [87, 12], [51, 8], [51, 68], [83, 2], [98, 82], [96, 30], [96, 74], [84, 13]]"
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

