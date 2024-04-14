# Test Report

Time: 2024-04-13 16:10:30.728945

### Base Program

```py
def random_calculation(a, b, c):
    result = 2*a + 3*b - 4*c
    return result
```

## Test Case 1

### Modified Program

```py
def random_calculation(a, b, c):
    result = 2 * a + 3 * b - 4 * c
    return result
```

<details>
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[[91, 20, 80], [77, 63, 58], [81, 54, 19], [6, 76, 52], [8, 75, 82], [19, 87, 25], [37, 48, 52], [58, 49, 32], [59, 38, 31], [47, 37, 25]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

## Test Case 2

### Modified Program

```py
def random_calculation(var_0, var_1, var_2):
    result = 2 * var_0 + 3 * var_1 - 4 * var_2
    return result
```

<details>
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_0\", \"val1\": \"*\", \"valueArray\": [\"var_0\", \"*\"], \"valueList\": [\"var_0\", \"*\"]}, {\"val0\": \"var_1\", \"val1\": \"*\", \"valueArray\": [\"var_1\", \"*\"], \"valueList\": [\"var_1\", \"*\"]}, {\"val0\": \"var_2\", \"val1\": \"*\", \"valueArray\": [\"var_2\", \"*\"], \"valueList\": [\"var_2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[[91, 20, 80], [77, 63, 58], [81, 54, 19], [6, 76, 52], [8, 75, 82], [19, 87, 25], [37, 48, 52], [58, 49, 32], [59, 38, 31], [47, 37, 25]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

## Test Case 3

### Modified Program

```py
def random_calculation(a, b, c):
    result = b * 3 + a * 2 + -(c * 4)
    return result
```

<details>
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[[91, 20, 80], [77, 63, 58], [81, 54, 19], [6, 76, 52], [8, 75, 82], [19, 87, 25], [37, 48, 52], [58, 49, 32], [59, 38, 31], [47, 37, 25]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

## Test Case 4

### Modified Program

```py
def random_calculation(var_3, var_4, var_5):
    result = var_4 * 3 + var_3 * 2 + -(var_5 * 4)
    return result
```

<details>
<summary>error_localizer endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}, {\"val0\": \"c\", \"val1\": \"*\", \"valueArray\": [\"c\", \"*\"], \"valueList\": [\"c\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"name\": \"c\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"random_calculation\": {\"name\": \"random_calculation\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_3\", \"val1\": \"*\", \"valueArray\": [\"var_3\", \"*\"], \"valueList\": [\"var_3\", \"*\"]}, {\"val0\": \"var_4\", \"val1\": \"*\", \"valueArray\": [\"var_4\", \"*\"], \"valueList\": [\"var_4\", \"*\"]}, {\"val0\": \"var_5\", \"val1\": \"*\", \"valueArray\": [\"var_5\", \"*\"], \"valueList\": [\"var_5\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"var_4\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"var_5\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"var_4\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"var_5\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}], \"valueList\": [\"result\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"var_4\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"Mult\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"var_5\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'random_calculation'\"}, \"types\": {\"result\": \"*\"}}}}",
    "function": "random_calculation",
    "inputs": "[]",
    "args": "[[91, 20, 80], [77, 63, 58], [81, 54, 19], [6, 76, 52], [8, 75, 82], [19, 87, 25], [37, 48, 52], [58, 49, 32], [59, 38, 31], [47, 37, 25]]"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

</details>

