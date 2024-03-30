# Test Report

Time: 2024-03-30 07:49:25.710167

### Base Program

```py
def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr
```

## Test Case 1

### Modified Program

```py

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[77, 97, 36, 15, 17, 71, 36, 37, 86, 65]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    86,
                    65
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    86,
                    65
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    86,
                    65
                ],
                "temp'": 65,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    86,
                    -1
                ],
                "maxElement'": 65,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    86,
                    -1
                ],
                "temp'": 65,
                "temp": 65,
                "maxElement": 65,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    86,
                    -1
                ],
                "maxElement'": 65,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    86,
                    -1
                ],
                "temp'": 86,
                "temp": 65,
                "maxElement": 65,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    65,
                    -1
                ],
                "temp'": 86,
                "temp": 86,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    37,
                    65,
                    -1
                ],
                "temp'": 37,
                "temp": 86,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    86,
                    65,
                    -1
                ],
                "temp'": 37,
                "temp": 37,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    36,
                    86,
                    65,
                    -1
                ],
                "temp'": 36,
                "temp": 37,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 36,
                "temp": 36,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    71,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 71,
                "temp": 36,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 71,
                "temp": 71,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    17,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 17,
                "temp": 71,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 17,
                "temp": 17,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    77,
                    97,
                    36,
                    15,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    15,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 15,
                "temp": 17,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    77,
                    97,
                    36,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 15,
                "temp": 15,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    77,
                    97,
                    36,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    97,
                    36,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 36,
                "temp": 15,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    77,
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 36,
                "temp": 36,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    77,
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 86,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 97,
                "temp": 36,
                "maxElement": 86,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    77,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 97,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    77,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 97,
                "temp": 97,
                "maxElement": 97,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    77,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 97,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    77,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 77,
                "temp": 97,
                "maxElement": 97,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 97,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 77,
                "temp": 77,
                "maxElement": 97,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 97,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "temp'": 77,
                "temp": 77,
                "maxElement": 97,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "maxElement'": 97,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    97,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    86,
                    65,
                    -1
                ],
                "i'": 0
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

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[71, 42, 99, 49, 67, 14, 46, 37, 34, 31]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    34,
                    31
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    34,
                    31
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    34,
                    31
                ],
                "temp'": 31,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    34,
                    -1
                ],
                "maxElement'": 31,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    34,
                    -1
                ],
                "temp'": 31,
                "temp": 31,
                "maxElement": 31,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    34,
                    -1
                ],
                "maxElement'": 31,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    34,
                    -1
                ],
                "temp'": 34,
                "temp": 31,
                "maxElement": 31,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    31,
                    -1
                ],
                "maxElement'": 34,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    31,
                    -1
                ],
                "temp'": 34,
                "temp": 34,
                "maxElement": 34,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    31,
                    -1
                ],
                "maxElement'": 34,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    37,
                    31,
                    -1
                ],
                "temp'": 37,
                "temp": 34,
                "maxElement": 34,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    34,
                    31,
                    -1
                ],
                "temp'": 37,
                "temp": 37,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    46,
                    34,
                    31,
                    -1
                ],
                "temp'": 46,
                "temp": 37,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 46,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 46,
                "temp": 46,
                "maxElement": 46,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 46,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    14,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 14,
                "temp": 46,
                "maxElement": 46,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 46,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 14,
                "temp": 14,
                "maxElement": 46,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 46,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    67,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 67,
                "temp": 14,
                "maxElement": 46,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 67,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 67,
                "temp": 67,
                "maxElement": 67,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    71,
                    42,
                    99,
                    49,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 67,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    49,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 49,
                "temp": 67,
                "maxElement": 67,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    71,
                    42,
                    99,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 67,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 49,
                "temp": 49,
                "maxElement": 67,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    71,
                    42,
                    99,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 67,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    42,
                    99,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 99,
                "temp": 49,
                "maxElement": 67,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    71,
                    42,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 99,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    42,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 99,
                "temp": 99,
                "maxElement": 99,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    71,
                    42,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 99,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    42,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 42,
                "temp": 99,
                "maxElement": 99,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    71,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 99,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    71,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 42,
                "temp": 42,
                "maxElement": 99,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    71,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 99,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    71,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 71,
                "temp": 42,
                "maxElement": 99,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    99,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 99,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    99,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 71,
                "temp": 71,
                "maxElement": 99,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    99,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 99,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    99,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "temp'": 71,
                "temp": 71,
                "maxElement": 99,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    99,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "maxElement'": 99,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    99,
                    99,
                    67,
                    67,
                    46,
                    46,
                    37,
                    34,
                    31,
                    -1
                ],
                "i'": 0
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

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[55, 2, 35, 14, 52, 16, 12, 5, 16, 51]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    16,
                    51
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    16,
                    51
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    16,
                    51
                ],
                "temp'": 51,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    16,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    16,
                    -1
                ],
                "temp'": 51,
                "temp": 51,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    16,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    16,
                    -1
                ],
                "temp'": 16,
                "temp": 51,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    51,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    51,
                    -1
                ],
                "temp'": 16,
                "temp": 16,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    51,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    5,
                    51,
                    -1
                ],
                "temp'": 5,
                "temp": 16,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    51,
                    51,
                    -1
                ],
                "temp'": 5,
                "temp": 5,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    12,
                    51,
                    51,
                    -1
                ],
                "temp'": 12,
                "temp": 5,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 12,
                "temp": 12,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    16,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 16,
                "temp": 12,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 16,
                "temp": 16,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 51,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    52,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 52,
                "temp": 16,
                "maxElement": 51,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 52,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 52,
                "temp": 52,
                "maxElement": 52,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    55,
                    2,
                    35,
                    14,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 52,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    14,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 14,
                "temp": 52,
                "maxElement": 52,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    55,
                    2,
                    35,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 52,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 14,
                "temp": 14,
                "maxElement": 52,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    55,
                    2,
                    35,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 52,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    2,
                    35,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 35,
                "temp": 14,
                "maxElement": 52,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    55,
                    2,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 52,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    2,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 35,
                "temp": 35,
                "maxElement": 52,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    55,
                    2,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 52,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    2,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 2,
                "temp": 35,
                "maxElement": 52,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    55,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 52,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    55,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 2,
                "temp": 2,
                "maxElement": 52,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    55,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 52,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    55,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 55,
                "temp": 2,
                "maxElement": 52,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    52,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 55,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    52,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 55,
                "temp": 55,
                "maxElement": 55,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    52,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 55,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    52,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "temp'": 55,
                "temp": 55,
                "maxElement": 55,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    52,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "maxElement'": 55,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    52,
                    52,
                    52,
                    52,
                    51,
                    51,
                    51,
                    51,
                    51,
                    -1
                ],
                "i'": 0
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

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[90, 36, 77, 44, 84, 98, 28, 85, 20, 100]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    20,
                    100
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    20,
                    100
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    20,
                    100
                ],
                "temp'": 100,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    20,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    20,
                    -1
                ],
                "temp'": 100,
                "temp": 100,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    20,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    20,
                    -1
                ],
                "temp'": 20,
                "temp": 100,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    100,
                    -1
                ],
                "temp'": 20,
                "temp": 20,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    85,
                    100,
                    -1
                ],
                "temp'": 85,
                "temp": 20,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    100,
                    100,
                    -1
                ],
                "temp'": 85,
                "temp": 85,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    28,
                    100,
                    100,
                    -1
                ],
                "temp'": 28,
                "temp": 85,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 28,
                "temp": 28,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    98,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 98,
                "temp": 28,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 98,
                "temp": 98,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    84,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 84,
                "temp": 98,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 84,
                "temp": 84,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    90,
                    36,
                    77,
                    44,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    44,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 44,
                "temp": 84,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    90,
                    36,
                    77,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 44,
                "temp": 44,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    90,
                    36,
                    77,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    36,
                    77,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 77,
                "temp": 44,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    90,
                    36,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    36,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 77,
                "temp": 77,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    90,
                    36,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    36,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 36,
                "temp": 77,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    90,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    90,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 36,
                "temp": 36,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    90,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    90,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 90,
                "temp": 36,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 90,
                "temp": 90,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "temp'": 90,
                "temp": 90,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    -1
                ],
                "i'": 0
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

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[35, 45, 0, 15, 96, 87, 58, 100, 90, 61]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    90,
                    61
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    90,
                    61
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    90,
                    61
                ],
                "temp'": 61,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    90,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    90,
                    -1
                ],
                "temp'": 61,
                "temp": 61,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    90,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    90,
                    -1
                ],
                "temp'": 90,
                "temp": 61,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    61,
                    -1
                ],
                "maxElement'": 90,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    61,
                    -1
                ],
                "temp'": 90,
                "temp": 90,
                "maxElement": 90,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    61,
                    -1
                ],
                "maxElement'": 90,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    100,
                    61,
                    -1
                ],
                "temp'": 100,
                "temp": 90,
                "maxElement": 90,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    90,
                    61,
                    -1
                ],
                "temp'": 100,
                "temp": 100,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    58,
                    90,
                    61,
                    -1
                ],
                "temp'": 58,
                "temp": 100,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 58,
                "temp": 58,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    87,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 87,
                "temp": 58,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 87,
                "temp": 87,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    96,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 96,
                "temp": 87,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 96,
                "temp": 96,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    35,
                    45,
                    0,
                    15,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    15,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 15,
                "temp": 96,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    35,
                    45,
                    0,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 15,
                "temp": 15,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    35,
                    45,
                    0,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    45,
                    0,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 0,
                "temp": 15,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    35,
                    45,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    45,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 0,
                "temp": 0,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    35,
                    45,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    45,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 45,
                "temp": 0,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    35,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    35,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 45,
                "temp": 45,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    35,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    35,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 35,
                "temp": 45,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 35,
                "temp": 35,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "temp'": 35,
                "temp": 35,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    100,
                    90,
                    61,
                    -1
                ],
                "i'": 0
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

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[25, 88, 78, 16, 77, 74, 41, 64, 26, 82]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    26,
                    82
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    26,
                    82
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    26,
                    82
                ],
                "temp'": 82,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    26,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    26,
                    -1
                ],
                "temp'": 82,
                "temp": 82,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    26,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    26,
                    -1
                ],
                "temp'": 26,
                "temp": 82,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    82,
                    -1
                ],
                "temp'": 26,
                "temp": 26,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    64,
                    82,
                    -1
                ],
                "temp'": 64,
                "temp": 26,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    82,
                    82,
                    -1
                ],
                "temp'": 64,
                "temp": 64,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    41,
                    82,
                    82,
                    -1
                ],
                "temp'": 41,
                "temp": 64,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 41,
                "temp": 41,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    74,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 74,
                "temp": 41,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 74,
                "temp": 74,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    77,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 77,
                "temp": 74,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 77,
                "temp": 77,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    25,
                    88,
                    78,
                    16,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    16,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 16,
                "temp": 77,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    25,
                    88,
                    78,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 16,
                "temp": 16,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    25,
                    88,
                    78,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    88,
                    78,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 78,
                "temp": 16,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    25,
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 78,
                "temp": 78,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    25,
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 82,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 88,
                "temp": 78,
                "maxElement": 82,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    25,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 88,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    25,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 88,
                "temp": 88,
                "maxElement": 88,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    25,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 88,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    25,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 25,
                "temp": 88,
                "maxElement": 88,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 88,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 25,
                "temp": 25,
                "maxElement": 88,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 88,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "temp'": 25,
                "temp": 25,
                "maxElement": 88,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "maxElement'": 88,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    88,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    82,
                    -1
                ],
                "i'": 0
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

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[16, 76, 100, 69, 54, 22, 70, 37, 17, 6]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    17,
                    6
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    17,
                    6
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    17,
                    6
                ],
                "temp'": 6,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    17,
                    -1
                ],
                "maxElement'": 6,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    17,
                    -1
                ],
                "temp'": 6,
                "temp": 6,
                "maxElement": 6,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    17,
                    -1
                ],
                "maxElement'": 6,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    17,
                    -1
                ],
                "temp'": 17,
                "temp": 6,
                "maxElement": 6,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    6,
                    -1
                ],
                "maxElement'": 17,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    6,
                    -1
                ],
                "temp'": 17,
                "temp": 17,
                "maxElement": 17,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    6,
                    -1
                ],
                "maxElement'": 17,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    37,
                    6,
                    -1
                ],
                "temp'": 37,
                "temp": 17,
                "maxElement": 17,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    17,
                    6,
                    -1
                ],
                "temp'": 37,
                "temp": 37,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    70,
                    17,
                    6,
                    -1
                ],
                "temp'": 70,
                "temp": 37,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 70,
                "temp": 70,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    22,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 22,
                "temp": 70,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 22,
                "temp": 22,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    54,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 54,
                "temp": 22,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 54,
                "temp": 54,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    16,
                    76,
                    100,
                    69,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    69,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 69,
                "temp": 54,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    16,
                    76,
                    100,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 69,
                "temp": 69,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    16,
                    76,
                    100,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    76,
                    100,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 100,
                "temp": 69,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    16,
                    76,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    76,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 100,
                "temp": 100,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    16,
                    76,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    76,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 76,
                "temp": 100,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    16,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    16,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 76,
                "temp": 76,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    16,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    16,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 16,
                "temp": 76,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    100,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    100,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 16,
                "temp": 16,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    100,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    100,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "temp'": 16,
                "temp": 16,
                "maxElement": 100,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    100,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "maxElement'": 100,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    100,
                    100,
                    70,
                    70,
                    70,
                    70,
                    37,
                    17,
                    6,
                    -1
                ],
                "i'": 0
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

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[28, 80, 23, 48, 33, 4, 34, 37, 30, 33]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    30,
                    33
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    30,
                    33
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    30,
                    33
                ],
                "temp'": 33,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    30,
                    -1
                ],
                "maxElement'": 33,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    30,
                    -1
                ],
                "temp'": 33,
                "temp": 33,
                "maxElement": 33,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    30,
                    -1
                ],
                "maxElement'": 33,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    30,
                    -1
                ],
                "temp'": 30,
                "temp": 33,
                "maxElement": 33,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    33,
                    -1
                ],
                "maxElement'": 33,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    33,
                    -1
                ],
                "temp'": 30,
                "temp": 30,
                "maxElement": 33,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    33,
                    -1
                ],
                "maxElement'": 33,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    37,
                    33,
                    -1
                ],
                "temp'": 37,
                "temp": 30,
                "maxElement": 33,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    33,
                    33,
                    -1
                ],
                "temp'": 37,
                "temp": 37,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    34,
                    33,
                    33,
                    -1
                ],
                "temp'": 34,
                "temp": 37,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 34,
                "temp": 34,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    4,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 4,
                "temp": 34,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 4,
                "temp": 4,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    33,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 33,
                "temp": 4,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 33,
                "temp": 33,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    28,
                    80,
                    23,
                    48,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 37,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    48,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 48,
                "temp": 33,
                "maxElement": 37,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    28,
                    80,
                    23,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 48,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 48,
                "temp": 48,
                "maxElement": 48,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    28,
                    80,
                    23,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 48,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    80,
                    23,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 23,
                "temp": 48,
                "maxElement": 48,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    28,
                    80,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 48,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    80,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 23,
                "temp": 23,
                "maxElement": 48,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    28,
                    80,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 48,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    80,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 80,
                "temp": 23,
                "maxElement": 48,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    28,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 80,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    28,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 80,
                "temp": 80,
                "maxElement": 80,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    28,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 80,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    28,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 28,
                "temp": 80,
                "maxElement": 80,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    80,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 80,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    80,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 28,
                "temp": 28,
                "maxElement": 80,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    80,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 80,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    80,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "temp'": 28,
                "temp": 28,
                "maxElement": 80,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    80,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "maxElement'": 80,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    80,
                    48,
                    48,
                    37,
                    37,
                    37,
                    37,
                    33,
                    33,
                    -1
                ],
                "i'": 0
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

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[23, 25, 25, 19, 26, 53, 61, 9, 60, 44]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    60,
                    44
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    60,
                    44
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    60,
                    44
                ],
                "temp'": 44,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    60,
                    -1
                ],
                "maxElement'": 44,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    60,
                    -1
                ],
                "temp'": 44,
                "temp": 44,
                "maxElement": 44,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    60,
                    -1
                ],
                "maxElement'": 44,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    60,
                    -1
                ],
                "temp'": 60,
                "temp": 44,
                "maxElement": 44,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    44,
                    -1
                ],
                "maxElement'": 60,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    44,
                    -1
                ],
                "temp'": 60,
                "temp": 60,
                "maxElement": 60,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    44,
                    -1
                ],
                "maxElement'": 60,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    9,
                    44,
                    -1
                ],
                "temp'": 9,
                "temp": 60,
                "maxElement": 60,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 60,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    60,
                    44,
                    -1
                ],
                "temp'": 9,
                "temp": 9,
                "maxElement": 60,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 60,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    61,
                    60,
                    44,
                    -1
                ],
                "temp'": 61,
                "temp": 9,
                "maxElement": 60,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 61,
                "temp": 61,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    53,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 53,
                "temp": 61,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 53,
                "temp": 53,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    26,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 26,
                "temp": 53,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 26,
                "temp": 26,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    23,
                    25,
                    25,
                    19,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    19,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 19,
                "temp": 26,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    23,
                    25,
                    25,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 19,
                "temp": 19,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    23,
                    25,
                    25,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    25,
                    25,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 25,
                "temp": 19,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    23,
                    25,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    25,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 25,
                "temp": 25,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    23,
                    25,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    25,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 25,
                "temp": 25,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    23,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    23,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 25,
                "temp": 25,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    23,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    23,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 23,
                "temp": 25,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    61,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    61,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 23,
                "temp": 23,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    61,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    61,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "temp'": 23,
                "temp": 23,
                "maxElement": 61,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    61,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "maxElement'": 61,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    61,
                    61,
                    61,
                    61,
                    61,
                    61,
                    60,
                    60,
                    44,
                    -1
                ],
                "i'": 0
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

def replaceElements(arr):
    n = len(arr)
    maxElement = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = maxElement
        maxElement = max(maxElement, temp)
    return arr


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"replaceElements\": {\"name\": \"replaceElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"maxElement\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 5}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"arr\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"arr\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"temp\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"temp\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"arr\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"arr\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"arr\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"maxElement\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"maxElement\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxElement\", {\"name\": \"max\", \"args\": [{\"name\": \"maxElement\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"temp\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'replaceElements'\", \"2\": \"the condition of the 'for' loop at line 5\", \"3\": \"*after* the 'for' loop starting at line 5\", \"4\": \"inside the body of the 'for' loop beginning at line 6\"}, \"types\": {\"temp\": \"*\", \"maxElement\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "replaceElements",
    "inputs": "[]",
    "args": "[[47, 35, 47, 68, 82, 94, 83, 70, 47, 3]]"
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
            "functionName": "replaceElements",
            "location": 1,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    47,
                    3
                ],
                "maxElement": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxElement'": -1,
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    47,
                    3
                ],
                "maxElement": -1,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "maxElement'": -1,
                "n": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    47,
                    3
                ],
                "temp'": 3,
                "temp": "<undef>",
                "maxElement": -1,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": "<undef>",
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    47,
                    -1
                ],
                "maxElement'": 3,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    47,
                    -1
                ],
                "temp'": 3,
                "temp": 3,
                "maxElement": 3,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    47,
                    -1
                ],
                "maxElement'": 3,
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    47,
                    -1
                ],
                "temp'": 47,
                "temp": 3,
                "maxElement": 3,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 9,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    3,
                    -1
                ],
                "maxElement'": 47,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    3,
                    -1
                ],
                "temp'": 47,
                "temp": 47,
                "maxElement": 47,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    3,
                    -1
                ],
                "maxElement'": 47,
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    70,
                    3,
                    -1
                ],
                "temp'": 70,
                "temp": 47,
                "maxElement": 47,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 8,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    47,
                    3,
                    -1
                ],
                "temp'": 70,
                "temp": 70,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 70,
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    83,
                    47,
                    3,
                    -1
                ],
                "temp'": 83,
                "temp": 70,
                "maxElement": 70,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 7,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 83,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 83,
                "temp": 83,
                "maxElement": 83,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 83,
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    94,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 94,
                "temp": 83,
                "maxElement": 83,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 6,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 94,
                "temp": 94,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    82,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 82,
                "temp": 94,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 5,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 82,
                "temp": 82,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    47,
                    35,
                    47,
                    68,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    68,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 68,
                "temp": 82,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 4,
                "arr'": [
                    47,
                    35,
                    47,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 68,
                "temp": 68,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    47,
                    35,
                    47,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    35,
                    47,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 47,
                "temp": 68,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 3,
                "arr'": [
                    47,
                    35,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    35,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 47,
                "temp": 47,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    47,
                    35,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    35,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 35,
                "temp": 47,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 2,
                "arr'": [
                    47,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    47,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 35,
                "temp": 35,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    47,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 4,
            "mem": {
                "arr": [
                    47,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 47,
                "temp": 35,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 1,
                "arr'": [
                    94,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 2,
            "mem": {
                "arr": [
                    94,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 47,
                "temp": 47,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    94,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "replaceElements",
            "location": 3,
            "mem": {
                "arr": [
                    94,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "temp'": 47,
                "temp": 47,
                "maxElement": 94,
                "iter#0'": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "i": 0,
                "arr'": [
                    94,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "maxElement'": 94,
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    9,
                    8,
                    7,
                    6,
                    5,
                    4,
                    3,
                    2,
                    1,
                    0
                ],
                "$ret'": [
                    94,
                    94,
                    94,
                    94,
                    94,
                    83,
                    70,
                    47,
                    3,
                    -1
                ],
                "i'": 0
            },
            "isChecked": false
        }
    ]
}
```

</details>

