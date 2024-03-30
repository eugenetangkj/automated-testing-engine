# Test Report

Time: 2024-03-30 07:08:57.847199

### Base Program

```py
def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count
```

## Test Case 1

### Modified Program

```py

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[30, 16, 29, 7, 43, 68, 68, 58, 34, 35], [93, 11, 52, 20, 50, 95, 30, 9, 56, 29], 92]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 92,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 1,
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
                "query_time": 92,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 0,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 1,
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
                "i'": 0,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 0,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 1,
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
                "i'": 1,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 1,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 1,
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
                "i'": 1,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 1,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 1,
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
                "i'": 2,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 2,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 1,
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
                "i'": 2,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 2,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 1,
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
                "i'": 3,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 3,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 1,
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
                "i'": 3,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 3,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 1,
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
                "i'": 4,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 4,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 1,
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
                "i'": 4,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 1,
                "i": 4,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 2,
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
                "i'": 5,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 5,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 2,
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
                "i'": 5,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 5,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 2,
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
                "i'": 6,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 6,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 2,
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
                "i'": 6,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 6,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 2,
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
                "i'": 7,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 7,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 2,
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
                "i'": 7,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 7,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 2,
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
                "i'": 8,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 8,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 2,
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
                "i'": 8,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 8,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 2,
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
                "i'": 9,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 9,
                "$cond": true,
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 2,
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
                "i'": 9,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    93,
                    11,
                    52,
                    20,
                    50,
                    95,
                    30,
                    9,
                    56,
                    29
                ],
                "count": 2,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    30,
                    16,
                    29,
                    7,
                    43,
                    68,
                    68,
                    58,
                    34,
                    35
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 2,
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
                "$ret'": 2,
                "i'": 9,
                "query_time": 92
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

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[57, 55, 72, 31, 49, 62, 57, 32, 35, 53], [90, 20, 84, 61, 19, 50, 15, 63, 26, 66], 7]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 7,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
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
                "query_time": 7,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 0,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 1,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 1,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 2,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 2,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 3,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 3,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 4,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 4,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 5,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 5,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 6,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 6,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 7,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
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
                "i'": 7,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
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
                "i'": 8,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 8,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
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
                "i'": 8,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 8,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
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
                "i'": 9,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 9,
                "$cond": true,
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
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
                "i'": 9,
                "query_time": 7
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    90,
                    20,
                    84,
                    61,
                    19,
                    50,
                    15,
                    63,
                    26,
                    66
                ],
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    57,
                    55,
                    72,
                    31,
                    49,
                    62,
                    57,
                    32,
                    35,
                    53
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
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
                "$ret'": 0,
                "i'": 9,
                "query_time": 7
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

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[22, 30, 10, 15, 37, 20, 74, 38, 7, 70], [84, 31, 87, 33, 45, 94, 2, 27, 66, 24], 28]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 28,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 1,
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
                "query_time": 28,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 1,
                "i": 0,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 1,
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
                "i'": 0,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 1,
                "i": 0,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 1,
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
                "i'": 1,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 1,
                "i": 1,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 1,
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
                "i'": 1,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 1,
                "i": 1,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 2,
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
                "i'": 2,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 2,
                "i": 2,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 2,
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
                "i'": 2,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 2,
                "i": 2,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 3,
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
                "i'": 3,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 3,
                "i": 3,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 3,
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
                "i'": 3,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 3,
                "i": 3,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 3,
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
                "i'": 4,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 3,
                "i": 4,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 3,
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
                "i'": 4,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 3,
                "i": 4,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 4,
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
                "i'": 5,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 4,
                "i": 5,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 4,
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
                "i'": 5,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 4,
                "i": 5,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 4,
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
                "i'": 6,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 4,
                "i": 6,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 4,
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
                "i'": 6,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 4,
                "i": 6,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 4,
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
                "i'": 7,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 4,
                "i": 7,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 4,
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
                "i'": 7,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 4,
                "i": 7,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 5,
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
                "i'": 8,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 5,
                "i": 8,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 5,
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
                "i'": 8,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 5,
                "i": 8,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 5,
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
                "i'": 9,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 5,
                "i": 9,
                "$cond": true,
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 5,
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
                "i'": 9,
                "query_time": 28
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    84,
                    31,
                    87,
                    33,
                    45,
                    94,
                    2,
                    27,
                    66,
                    24
                ],
                "count": 5,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    22,
                    30,
                    10,
                    15,
                    37,
                    20,
                    74,
                    38,
                    7,
                    70
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 5,
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
                "$ret'": 5,
                "i'": 9,
                "query_time": 28
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

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[89, 18, 13, 93, 73, 74, 86, 91, 44, 83], [59, 3, 100, 58, 24, 66, 55, 26, 14, 32], 10]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
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
                "query_time": 10,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 0,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 1,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 1,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 2,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 2,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 3,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 3,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 4,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 4,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 5,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 5,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 6,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 6,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 7,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
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
                "i'": 7,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
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
                "i'": 8,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 8,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
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
                "i'": 8,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 8,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
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
                "i'": 9,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 9,
                "$cond": true,
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
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
                "i'": 9,
                "query_time": 10
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    59,
                    3,
                    100,
                    58,
                    24,
                    66,
                    55,
                    26,
                    14,
                    32
                ],
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    89,
                    18,
                    13,
                    93,
                    73,
                    74,
                    86,
                    91,
                    44,
                    83
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
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
                "$ret'": 0,
                "i'": 9,
                "query_time": 10
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

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[65, 80, 91, 86, 33, 20, 7, 34, 79, 59], [3, 86, 74, 60, 17, 20, 19, 59, 96, 66], 78]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 78,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
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
                "query_time": 78,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 0,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 1,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 1,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 2,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 2,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 3,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 3,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 4,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 4,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 5,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 5,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 6,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 6,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 7,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
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
                "i'": 7,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
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
                "i'": 8,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 8,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
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
                "i'": 8,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 8,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
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
                "i'": 9,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 9,
                "$cond": true,
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
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
                "i'": 9,
                "query_time": 78
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    3,
                    86,
                    74,
                    60,
                    17,
                    20,
                    19,
                    59,
                    96,
                    66
                ],
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    65,
                    80,
                    91,
                    86,
                    33,
                    20,
                    7,
                    34,
                    79,
                    59
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
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
                "$ret'": 0,
                "i'": 9,
                "query_time": 78
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

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[29, 87, 92, 2, 100, 34, 30, 31, 91, 20], [67, 10, 48, 37, 2, 40, 96, 52, 89, 61], 15]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 15,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
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
                "query_time": 15,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 0,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 1,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 1,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 2,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 2,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 1,
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
                "i'": 3,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 3,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 1,
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
                "i'": 3,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 3,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 1,
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
                "i'": 4,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 4,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 1,
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
                "i'": 4,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 4,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 1,
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
                "i'": 5,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 5,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 1,
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
                "i'": 5,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 5,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 1,
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
                "i'": 6,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 6,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 1,
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
                "i'": 6,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 6,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 1,
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
                "i'": 7,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 7,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 1,
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
                "i'": 7,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 7,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 1,
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
                "i'": 8,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 8,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 1,
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
                "i'": 8,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 8,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 1,
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
                "i'": 9,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 9,
                "$cond": true,
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 1,
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
                "i'": 9,
                "query_time": 15
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    67,
                    10,
                    48,
                    37,
                    2,
                    40,
                    96,
                    52,
                    89,
                    61
                ],
                "count": 1,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    29,
                    87,
                    92,
                    2,
                    100,
                    34,
                    30,
                    31,
                    91,
                    20
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 1,
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
                "$ret'": 1,
                "i'": 9,
                "query_time": 15
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

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[42, 6, 8, 47, 75, 18, 100, 28, 8, 78], [37, 69, 83, 38, 75, 90, 89, 20, 66, 55], 34]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 34,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
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
                "query_time": 34,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 0,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 1,
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
                "i'": 1,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 1,
                "i": 1,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 1,
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
                "i'": 1,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 1,
                "i": 1,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 2,
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
                "i'": 2,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 2,
                "i": 2,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 2,
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
                "i'": 2,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 2,
                "i": 2,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 2,
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
                "i'": 3,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 2,
                "i": 3,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 2,
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
                "i'": 3,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 2,
                "i": 3,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 2,
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
                "i'": 4,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 2,
                "i": 4,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 2,
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
                "i'": 4,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 2,
                "i": 4,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 3,
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
                "i'": 5,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 3,
                "i": 5,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 3,
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
                "i'": 5,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 3,
                "i": 5,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 3,
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
                "i'": 6,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 3,
                "i": 6,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 3,
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
                "i'": 6,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 3,
                "i": 6,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 3,
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
                "i'": 7,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 3,
                "i": 7,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 3,
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
                "i'": 7,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 3,
                "i": 7,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 4,
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
                "i'": 8,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 4,
                "i": 8,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 4,
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
                "i'": 8,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 4,
                "i": 8,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 4,
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
                "i'": 9,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 4,
                "i": 9,
                "$cond": true,
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 4,
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
                "i'": 9,
                "query_time": 34
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    37,
                    69,
                    83,
                    38,
                    75,
                    90,
                    89,
                    20,
                    66,
                    55
                ],
                "count": 4,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    42,
                    6,
                    8,
                    47,
                    75,
                    18,
                    100,
                    28,
                    8,
                    78
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 4,
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
                "i'": 9,
                "query_time": 34
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

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[4, 45, 90, 9, 88, 44, 93, 78, 21, 68], [74, 39, 52, 78, 5, 37, 9, 14, 80, 25], 17]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 17,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 1,
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
                "query_time": 17,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 1,
                "i": 0,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 1,
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
                "i'": 0,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 1,
                "i": 0,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 1,
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
                "i'": 1,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 1,
                "i": 1,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 1,
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
                "i'": 1,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 1,
                "i": 1,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 1,
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
                "i'": 2,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 1,
                "i": 2,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 1,
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
                "i'": 2,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 1,
                "i": 2,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 2,
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
                "i'": 3,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 3,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 2,
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
                "i'": 3,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 3,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 2,
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
                "i'": 4,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 4,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 2,
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
                "i'": 4,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 4,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 2,
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
                "i'": 5,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 5,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 2,
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
                "i'": 5,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 5,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 2,
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
                "i'": 6,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 6,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 2,
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
                "i'": 6,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 6,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 2,
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
                "i'": 7,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 7,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 2,
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
                "i'": 7,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 7,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 2,
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
                "i'": 8,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 8,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 2,
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
                "i'": 8,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 8,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 2,
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
                "i'": 9,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 9,
                "$cond": true,
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 2,
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
                "i'": 9,
                "query_time": 17
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    74,
                    39,
                    52,
                    78,
                    5,
                    37,
                    9,
                    14,
                    80,
                    25
                ],
                "count": 2,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    4,
                    45,
                    90,
                    9,
                    88,
                    44,
                    93,
                    78,
                    21,
                    68
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 2,
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
                "$ret'": 2,
                "i'": 9,
                "query_time": 17
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

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[14, 40, 28, 100, 89, 56, 40, 87, 74, 84], [10, 82, 11, 58, 38, 17, 41, 69, 20, 36], 92]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 92,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
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
                "query_time": 92,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 0,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 1,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 1,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 2,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 2,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 3,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 3,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 4,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 4,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 5,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 5,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 6,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 6,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 7,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
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
                "i'": 7,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
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
                "i'": 8,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 8,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
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
                "i'": 8,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 8,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
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
                "i'": 9,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 9,
                "$cond": true,
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
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
                "i'": 9,
                "query_time": 92
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    10,
                    82,
                    11,
                    58,
                    38,
                    17,
                    41,
                    69,
                    20,
                    36
                ],
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    14,
                    40,
                    28,
                    100,
                    89,
                    56,
                    40,
                    87,
                    74,
                    84
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
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
                "$ret'": 0,
                "i'": 9,
                "query_time": 92
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

def busy_student(start_time, end_time, query_time):
    count = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"busy_student\": {\"name\": \"busy_student\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"start_time\", \"val1\": \"*\", \"valueArray\": [\"start_time\", \"*\"], \"valueList\": [\"start_time\", \"*\"]}, {\"val0\": \"end_time\", \"val1\": \"*\", \"valueArray\": [\"end_time\", \"*\"], \"valueList\": [\"end_time\", \"*\"]}, {\"val0\": \"query_time\", \"val1\": \"*\", \"valueArray\": [\"query_time\", \"*\"], \"valueList\": [\"query_time\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"start_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"query_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"end_time\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'busy_student'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "busy_student",
    "inputs": "[]",
    "args": "[[74, 35, 49, 49, 42, 86, 38, 16, 3, 18], [19, 33, 24, 57, 14, 15, 37, 1, 46, 6], 40]"
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
            "functionName": "busy_student",
            "location": 1,
            "mem": {
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
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
                "ind#0": "<undef>",
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>",
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 0,
                "$cond'": true,
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
                "ind#0": 0,
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "count'": 0,
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
                "query_time": 40,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": "<undef>",
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
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
                "query_time": 40,
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 0,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 0,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
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
                "i'": 1,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 1,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 1,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
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
                "i'": 2,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 2,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 2,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
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
                "i'": 3,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 3,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 3,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
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
                "i'": 4,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 4,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 4,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
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
                "i'": 5,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 5,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 5,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
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
                "i'": 6,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 6,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 6,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
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
                "i'": 7,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
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
                "i'": 7,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 0,
                "i": 7,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 1,
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
                "i'": 8,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 1,
                "i": 8,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 1,
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
                "i'": 8,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 4,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 1,
                "i": 8,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 1,
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
                "i'": 9,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 2,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 1,
                "i": 9,
                "$cond": true,
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 1,
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
                "i'": 9,
                "query_time": 40
            },
            "isChecked": false
        },
        {
            "functionName": "busy_student",
            "location": 3,
            "mem": {
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
                "end_time": [
                    19,
                    33,
                    24,
                    57,
                    14,
                    15,
                    37,
                    1,
                    46,
                    6
                ],
                "count": 1,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "start_time": [
                    74,
                    35,
                    49,
                    49,
                    42,
                    86,
                    38,
                    16,
                    3,
                    18
                ],
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 1,
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
                "$ret'": 1,
                "i'": 9,
                "query_time": 40
            },
            "isChecked": false
        }
    ]
}
```

</details>

