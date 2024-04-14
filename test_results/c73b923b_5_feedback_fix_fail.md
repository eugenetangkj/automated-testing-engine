# Test Report

Time: 2024-04-14 07:29:54.028223

### Base Program

```py
def calculate_circle_area(radius):
    return 3.14159 * (radius ** 2)
```

## Test Case 1

### Modified Program

```py
def calculate_circle_area(radius):
    return 3.14159 * radius ** 2
```

<details>
<summary>feedback_fix endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[[-89.19263419000734], [-83.25105550910557], [-44.52011180453588], [40.83277828554273], [-37.39021677568468], [-62.42810615265433], [-43.83553026936231], [35.70472252683649], [60.53767146101029], [8.23968652102856]]"
}
```

Message: 
```
Exception
Error in making API call to https://its.comp.nus.edu.sg/cs3213/feedback_fix. (Retry 0 times)
Status code: 500.
Response: Internal Server Error
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
def calculate_circle_area(radius):
    if True:
        return 3.14159 * radius ** 2
```

<details>
<summary>feedback_fix endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"calculate_circle_area\": {\"name\": \"calculate_circle_area\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"radius\", \"val1\": \"*\", \"valueArray\": [\"radius\", \"*\"], \"valueList\": [\"radius\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"value\": \"True\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3.14159\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"Pow\", \"args\": [{\"name\": \"radius\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'calculate_circle_area'\"}, \"types\": {}}}}",
    "function": "calculate_circle_area",
    "inputs": "[]",
    "args": "[[-89.19263419000734], [-83.25105550910557], [-44.52011180453588], [40.83277828554273], [-37.39021677568468], [-62.42810615265433], [-43.83553026936231], [35.70472252683649], [60.53767146101029], [8.23968652102856]]"
}
```

Message: 
```
Exception
Error in making API call to https://its.comp.nus.edu.sg/cs3213/feedback_fix. (Retry 0 times)
Status code: 500.
Response: Internal Server Error
```

Actual Output: None

</details>

