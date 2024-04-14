# Test Report

Time: 2024-04-14 07:36:14.578213

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
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[38.27629989064698, 44.689572303153966]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": 0.019165386,
                "weight": 38.2763,
                "$ret'": 0.019165386,
                "height": 44.68957,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 2

### Modified Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[30.85855166175142, -1.2191643237577665]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": 20.761131,
                "weight": 30.858551,
                "$ret'": 20.761131,
                "height": -1.2191644,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 3

### Modified Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[72.68117157505284, -16.499935180476697]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": 0.26696694,
                "weight": 72.681175,
                "$ret'": 0.26696694,
                "height": -16.499935,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 4

### Modified Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[-29.676098740138173, 87.15805481509216]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": -0.0039065345,
                "weight": -29.676098,
                "$ret'": -0.0039065345,
                "height": 87.15806,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 5

### Modified Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[-56.105927014225074, 53.26845269786284]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": -0.01977282,
                "weight": -56.105927,
                "$ret'": -0.01977282,
                "height": 53.26845,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 6

### Modified Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[14.753989804668507, 21.286244668297357]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": 0.03256202,
                "weight": 14.75399,
                "$ret'": 0.03256202,
                "height": 21.286245,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 7

### Modified Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[77.12368405890811, 92.17216554503335]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": 0.009077959,
                "weight": 77.12369,
                "$ret'": 0.009077959,
                "height": 92.172165,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 8

### Modified Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[94.59019225416964, 71.93388651229878]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": 0.018280122,
                "weight": 94.590195,
                "$ret'": 0.018280122,
                "height": 71.93388,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 9

### Modified Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[-87.95977471948262, -63.81785017259239]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": -0.021597315,
                "weight": -87.95978,
                "$ret'": -0.021597315,
                "height": -63.817852,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

## Test Case 10

### Modified Program

```py
def calculate_bmi(weight, height):
	bmi = weight / (height ** 2)
	return bmi
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"calculate_bmi\": {\"name\": \"calculate_bmi\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"weight\", \"val1\": \"*\", \"valueArray\": [\"weight\", \"*\"], \"valueList\": [\"weight\", \"*\"]}, {\"val0\": \"height\", \"val1\": \"*\", \"valueArray\": [\"height\", \"*\"], \"valueList\": [\"height\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"bmi\", \"val1\": {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"bmi\", {\"name\": \"Div\", \"args\": [{\"name\": \"weight\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"height\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"bmi\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"bmi\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_bmi'\"}, \"types\": {\"bmi\": \"*\"}}}}",
    "function": "calculate_bmi",
    "inputs": "[]",
    "args": "[91.19295871859518, -95.11294389559512]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "entries": [
        {
            "functionName": "calculate_bmi",
            "location": 1,
            "mem": {
                "bmi'": 0.010080499,
                "weight": 91.192955,
                "$ret'": 0.010080499,
                "height": -95.112946,
                "bmi": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

