# Test Report

Time: 2024-03-30 08:23:08.116498

### Base Program

```py
def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist
```

## Test Case 1

### Modified Program

```py

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[50, 73, 83, 73, 83, 72, 61, 79, 8, 15]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 0,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 10,
                "seats": [
                    50,
                    73,
                    83,
                    73,
                    83,
                    72,
                    61,
                    79,
                    8,
                    15
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 10,
                "i'": 9
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

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[71, 84, 17, 86, 1, 39, 24, 94, 37, 1]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 4,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 4,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 5,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 5,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 6,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 6,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 7,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 7,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": 4,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 8,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": 9,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 4,
                "i": 8,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": 9,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 9,
                "i": 9,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": 9,
                "maxDist": 4,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": 9,
                "i": 9,
                "maxDist'": 4,
                "seats": [
                    71,
                    84,
                    17,
                    86,
                    1,
                    39,
                    24,
                    94,
                    37,
                    1
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 4,
                "i'": 9
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

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[24, 85, 4, 48, 30, 61, 28, 29, 4, 81]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 0,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 10,
                "seats": [
                    24,
                    85,
                    4,
                    48,
                    30,
                    61,
                    28,
                    29,
                    4,
                    81
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 10,
                "i'": 9
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

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[86, 50, 75, 77, 79, 94, 91, 95, 51, 56]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 0,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 10,
                "seats": [
                    86,
                    50,
                    75,
                    77,
                    79,
                    94,
                    91,
                    95,
                    51,
                    56
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 10,
                "i'": 9
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

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[92, 67, 23, 10, 31, 56, 43, 61, 70, 17]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 0,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 10,
                "seats": [
                    92,
                    67,
                    23,
                    10,
                    31,
                    56,
                    43,
                    61,
                    70,
                    17
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 10,
                "i'": 9
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

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[90, 37, 77, 28, 20, 63, 68, 34, 33, 93]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 0,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 10,
                "seats": [
                    90,
                    37,
                    77,
                    28,
                    20,
                    63,
                    68,
                    34,
                    33,
                    93
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 10,
                "i'": 9
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

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[58, 68, 79, 24, 59, 66, 18, 63, 14, 44]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 0,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 10,
                "seats": [
                    58,
                    68,
                    79,
                    24,
                    59,
                    66,
                    18,
                    63,
                    14,
                    44
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 10,
                "i'": 9
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

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[70, 64, 27, 48, 81, 68, 71, 50, 35, 24]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 0,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 10,
                "seats": [
                    70,
                    64,
                    27,
                    48,
                    81,
                    68,
                    71,
                    50,
                    35,
                    24
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 10,
                "i'": 9
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

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[20, 92, 22, 59, 22, 77, 19, 73, 74, 56]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 0,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 10,
                "seats": [
                    20,
                    92,
                    22,
                    59,
                    22,
                    77,
                    19,
                    73,
                    74,
                    56
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 10,
                "i'": 9
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

def maxDistToClosest(seats):
    n = len(seats)
    maxDist = 0
    lastPerson = -1

    for i in range(n):
        if seats[i] == 1:
            if lastPerson == -1:
                maxDist = i
            else:
                maxDist = max(maxDist, (i - lastPerson) // 2)
            lastPerson = i

    maxDist = max(maxDist, n - 1 - lastPerson)
    return maxDist


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxDistToClosest\": {\"name\": \"maxDistToClosest\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"seats\", \"val1\": \"*\", \"valueArray\": [\"seats\", \"*\"], \"valueList\": [\"seats\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"len\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"maxDist\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"maxDist\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"lastPerson\", {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"3\": [{\"val0\": \"maxDist\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}], \"valueList\": [\"maxDist\", {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"n\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 15, \"tokentype\": \"Constant\"}], \"line\": 15, \"tokentype\": \"Operation\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 15, \"tokentype\": \"Variable\"}], \"line\": 15, \"tokentype\": \"Operation\"}], \"line\": 15}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"maxDist\", \"primed\": true, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}], \"valueList\": [\"$ret\", {\"name\": \"maxDist\", \"primed\": true, \"line\": 16}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"maxDist\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"maxDist\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"lastPerson\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"USub\", \"args\": [{\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"max\", \"args\": [{\"name\": \"maxDist\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 12, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 12, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"maxDist\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"lastPerson\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"lastPerson\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"seats\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": true, \"line\": 13, \"tokentype\": \"Variable\"}, {\"name\": \"lastPerson\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxDistToClosest'\", \"2\": \"the condition of the 'for' loop at line 7\", \"3\": \"*after* the 'for' loop starting at line 7\", \"4\": \"inside the body of the 'for' loop beginning at line 8\"}, \"types\": {\"maxDist\": \"*\", \"lastPerson\": \"*\", \"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\", \"n\": \"*\"}}}}",
    "function": "maxDistToClosest",
    "inputs": "[]",
    "args": "[[50, 42, 69, 15, 23, 50, 73, 60, 63, 4]]"
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
            "functionName": "maxDistToClosest",
            "location": 1,
            "mem": {
                "lastPerson'": -1,
                "maxDist": "<undef>",
                "ind#0'": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": "<undef>",
                "ind#0": "<undef>",
                "n'": 10,
                "iter#0": "<undef>",
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": "<undef>",
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": "<undef>",
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 0,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 1,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 2,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 3,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 4,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 5
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 5,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 6,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 7
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 7,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 8
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 4,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 8,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 2,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 0,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": true,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "i'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "maxDistToClosest",
            "location": 3,
            "mem": {
                "lastPerson'": -1,
                "maxDist": 0,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "lastPerson": -1,
                "i": 9,
                "maxDist'": 10,
                "seats": [
                    50,
                    42,
                    69,
                    15,
                    23,
                    50,
                    73,
                    60,
                    63,
                    4
                ],
                "n": 10,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "n'": 10,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": 10,
                "i'": 9
            },
            "isChecked": false
        }
    ]
}
```

</details>

