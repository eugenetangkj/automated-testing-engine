# Test Report

Time: 2024-03-30 08:53:19.997319

### Base Program

```py
def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count
```

## Test Case 1

### Modified Program

```py

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[34, 53, 64, 1, 37, 55, 13, 51, 41, 6]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 0,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    34,
                    53,
                    64,
                    1,
                    37,
                    55,
                    13,
                    51,
                    41,
                    6
                ],
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

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[75, 28, 15, 29, 45, 62, 29, 27, 36, 83]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 0,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    75,
                    28,
                    15,
                    29,
                    45,
                    62,
                    29,
                    27,
                    36,
                    83
                ],
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

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[71, 44, 29, 33, 81, 89, 11, 65, 46, 98]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 0,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    71,
                    44,
                    29,
                    33,
                    81,
                    89,
                    11,
                    65,
                    46,
                    98
                ],
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

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[54, 69, 11, 44, 0, 94, 36, 14, 36, 100]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 0,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    54,
                    69,
                    11,
                    44,
                    0,
                    94,
                    36,
                    14,
                    36,
                    100
                ],
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

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[57, 64, 86, 74, 69, 76, 9, 55, 60, 65]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 0,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    57,
                    64,
                    86,
                    74,
                    69,
                    76,
                    9,
                    55,
                    60,
                    65
                ],
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

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[9, 9, 71, 67, 7, 92, 66, 37, 86, 70]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 0,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    9,
                    9,
                    71,
                    67,
                    7,
                    92,
                    66,
                    37,
                    86,
                    70
                ],
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

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[100, 91, 2, 72, 17, 14, 6, 32, 29, 7]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 0,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    100,
                    91,
                    2,
                    72,
                    17,
                    14,
                    6,
                    32,
                    29,
                    7
                ],
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

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[23, 62, 84, 36, 83, 78, 99, 0, 87, 77]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 0,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    23,
                    62,
                    84,
                    36,
                    83,
                    78,
                    99,
                    0,
                    87,
                    77
                ],
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

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[2, 25, 29, 41, 99, 59, 77, 24, 49, 84]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 0,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 0,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 0,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 0,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 0,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    2,
                    25,
                    29,
                    41,
                    99,
                    59,
                    77,
                    24,
                    49,
                    84
                ],
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

def count_prefix_aligned(flips):
    count = 0
    for i in range(len(flips)):
        if flips[i] == i + 1:
            count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_prefix_aligned\": {\"name\": \"count_prefix_aligned\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"flips\", \"val1\": \"*\", \"valueArray\": [\"flips\", \"*\"], \"valueList\": [\"flips\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"flips\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_prefix_aligned'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"count\": \"*\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "count_prefix_aligned",
    "inputs": "[]",
    "args": "[[82, 94, 20, 19, 53, 20, 7, 38, 89, 8]]"
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
            "functionName": "count_prefix_aligned",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": "<undef>",
                "count'": 0,
                "iter#0": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
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
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
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
                "count": 0,
                "i": "<undef>",
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 1,
                "count": 0,
                "i": 0,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 2,
                "count": 0,
                "i": 1,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 3,
                "count": 0,
                "i": 2,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 4,
                "count": 0,
                "i": 3,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 5,
                "count": 0,
                "i": 4,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 6,
                "count": 0,
                "i": 5,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 1,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 7,
                "count": 1,
                "i": 6,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 8,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 1,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 8,
                "count": 1,
                "i": 7,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 9,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 1,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 4,
            "mem": {
                "ind#0'": 10,
                "$cond'": true,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 9,
                "count": 1,
                "i": 8,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
            "location": 2,
            "mem": {
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "ind#0": 10,
                "count": 1,
                "i": 9,
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
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "count_prefix_aligned",
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
                "count": 1,
                "i": 9,
                "$cond": false,
                "$ret": "<undef>",
                "ind#0'": 10,
                "$cond'": false,
                "flips": [
                    82,
                    94,
                    20,
                    19,
                    53,
                    20,
                    7,
                    38,
                    89,
                    8
                ],
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
                "i'": 9
            },
            "isChecked": false
        }
    ]
}
```

</details>

