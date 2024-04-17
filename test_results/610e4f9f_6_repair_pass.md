# Test Report

Time: 2024-04-14 07:37:13.622999

### Base Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

## Test Case 1

### Modified Program

```py
def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return bmi
```

<details>
<summary>repair endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[[38.27629989064698, 44.689572303153966], [30.85855166175142, -1.2191643237577665], [72.68117157505284, -16.499935180476697], [-29.676098740138173, 87.15805481509216], [-56.105927014225074, 53.26845269786284], [14.753989804668507, 21.286244668297357], [77.12368405890811, 92.17216554503335], [94.59019225416964, 71.93388651229878], [-87.95977471948262, -63.81785017259239], [91.19295871859518, -95.11294389559512]]"
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
def calculate_bmi(weight, height):
    if True:
        bmi = weight / height ** 2
        return bmi
```

<details>
<summary>repair endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"bmi\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"bmi\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"bmi\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[[38.27629989064698, 44.689572303153966], [30.85855166175142, -1.2191643237577665], [72.68117157505284, -16.499935180476697], [-29.676098740138173, 87.15805481509216], [-56.105927014225074, 53.26845269786284], [14.753989804668507, 21.286244668297357], [77.12368405890811, 92.17216554503335], [94.59019225416964, 71.93388651229878], [-87.95977471948262, -63.81785017259239], [91.19295871859518, -95.11294389559512]]"
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
