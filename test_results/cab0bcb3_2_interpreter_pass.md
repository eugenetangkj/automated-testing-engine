# Test Report

Time: 2024-03-30 08:36:04.355528

### Base Program

```py
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

## Test Case 1

### Modified Program

```py

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[34, 67, 69, 79, 45, 96, 78, 23, 48, 37]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 0,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 34,
                "num'": 34,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 34,
                "result'": 34,
                "num'": 34,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 1,
                "num": 34,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 34,
                "result'": 97,
                "num'": 67,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 1,
                "num": 34,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 97,
                "result'": 97,
                "num'": 67,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 2,
                "num": 67,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 97,
                "result'": 36,
                "num'": 69,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 2,
                "num": 67,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 36,
                "result'": 36,
                "num'": 69,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 3,
                "num": 69,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 36,
                "result'": 107,
                "num'": 79,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 3,
                "num": 69,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 107,
                "result'": 107,
                "num'": 79,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 4,
                "num": 79,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 107,
                "result'": 70,
                "num'": 45,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 4,
                "num": 79,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 70,
                "result'": 70,
                "num'": 45,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 5,
                "num": 45,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 70,
                "result'": 38,
                "num'": 96,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 5,
                "num": 45,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 38,
                "result'": 38,
                "num'": 96,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 6,
                "num": 96,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 38,
                "result'": 104,
                "num'": 78,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 6,
                "num": 96,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 104,
                "result'": 104,
                "num'": 78,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 7,
                "num": 78,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 104,
                "result'": 127,
                "num'": 23,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 7,
                "num": 78,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 127,
                "result'": 127,
                "num'": 23,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 8,
                "num": 23,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 127,
                "result'": 79,
                "num'": 48,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 8,
                "num": 23,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 79,
                "result'": 79,
                "num'": 48,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 9,
                "num": 48,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 79,
                "result'": 106,
                "num'": 37,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 9,
                "num": 48,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 106,
                "result'": 106,
                "num'": 37,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "ind#0": 10,
                "num": 37,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 106,
                "iter#0'": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "num": 37,
                "$cond": false,
                "$ret": "<undef>",
                "result": 106,
                "num'": 37,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ],
                "$ret'": 106,
                "nums": [
                    34,
                    67,
                    69,
                    79,
                    45,
                    96,
                    78,
                    23,
                    48,
                    37
                ]
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

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[11, 68, 54, 85, 83, 81, 68, 71, 5, 37]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 0,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 11,
                "num'": 11,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 11,
                "result'": 11,
                "num'": 11,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 1,
                "num": 11,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 11,
                "result'": 79,
                "num'": 68,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 1,
                "num": 11,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 79,
                "result'": 79,
                "num'": 68,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 2,
                "num": 68,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 79,
                "result'": 121,
                "num'": 54,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 2,
                "num": 68,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 121,
                "result'": 121,
                "num'": 54,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 3,
                "num": 54,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 121,
                "result'": 44,
                "num'": 85,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 3,
                "num": 54,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 44,
                "result'": 44,
                "num'": 85,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 4,
                "num": 85,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 44,
                "result'": 127,
                "num'": 83,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 4,
                "num": 85,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 127,
                "result'": 127,
                "num'": 83,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 5,
                "num": 83,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 127,
                "result'": 46,
                "num'": 81,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 5,
                "num": 83,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 46,
                "result'": 46,
                "num'": 81,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 6,
                "num": 81,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 46,
                "result'": 106,
                "num'": 68,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 6,
                "num": 81,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 106,
                "result'": 106,
                "num'": 68,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 7,
                "num": 68,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 106,
                "result'": 45,
                "num'": 71,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 7,
                "num": 68,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 45,
                "result'": 45,
                "num'": 71,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 8,
                "num": 71,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 45,
                "result'": 40,
                "num'": 5,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 8,
                "num": 71,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 40,
                "result'": 40,
                "num'": 5,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 9,
                "num": 5,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 40,
                "result'": 13,
                "num'": 37,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 9,
                "num": 5,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 13,
                "result'": 13,
                "num'": 37,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "ind#0": 10,
                "num": 37,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 13,
                "iter#0'": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "num": 37,
                "$cond": false,
                "$ret": "<undef>",
                "result": 13,
                "num'": 37,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ],
                "$ret'": 13,
                "nums": [
                    11,
                    68,
                    54,
                    85,
                    83,
                    81,
                    68,
                    71,
                    5,
                    37
                ]
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

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[17, 12, 72, 98, 30, 91, 57, 83, 8, 16]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 0,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 17,
                "num'": 17,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 17,
                "result'": 17,
                "num'": 17,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 1,
                "num": 17,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 17,
                "result'": 29,
                "num'": 12,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 1,
                "num": 17,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 29,
                "result'": 29,
                "num'": 12,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 2,
                "num": 12,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 29,
                "result'": 85,
                "num'": 72,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 2,
                "num": 12,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 85,
                "result'": 85,
                "num'": 72,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 3,
                "num": 72,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 85,
                "result'": 55,
                "num'": 98,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 3,
                "num": 72,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 55,
                "result'": 55,
                "num'": 98,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 4,
                "num": 98,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 55,
                "result'": 41,
                "num'": 30,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 4,
                "num": 98,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 41,
                "result'": 41,
                "num'": 30,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 5,
                "num": 30,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 41,
                "result'": 114,
                "num'": 91,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 5,
                "num": 30,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 114,
                "result'": 114,
                "num'": 91,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 6,
                "num": 91,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 114,
                "result'": 75,
                "num'": 57,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 6,
                "num": 91,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 75,
                "result'": 75,
                "num'": 57,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 7,
                "num": 57,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 75,
                "result'": 24,
                "num'": 83,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 7,
                "num": 57,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 24,
                "result'": 24,
                "num'": 83,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 8,
                "num": 83,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 24,
                "result'": 16,
                "num'": 8,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 8,
                "num": 83,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 16,
                "result'": 16,
                "num'": 8,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 9,
                "num": 8,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 16,
                "result'": 0,
                "num'": 16,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 9,
                "num": 8,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "num'": 16,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "ind#0": 10,
                "num": 16,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 0,
                "iter#0'": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "num": 16,
                "$cond": false,
                "$ret": "<undef>",
                "result": 0,
                "num'": 16,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ],
                "$ret'": 0,
                "nums": [
                    17,
                    12,
                    72,
                    98,
                    30,
                    91,
                    57,
                    83,
                    8,
                    16
                ]
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

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[85, 91, 93, 27, 83, 70, 12, 33, 77, 87]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 0,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 85,
                "num'": 85,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 85,
                "result'": 85,
                "num'": 85,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 1,
                "num": 85,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 85,
                "result'": 14,
                "num'": 91,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 1,
                "num": 85,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 14,
                "result'": 14,
                "num'": 91,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 2,
                "num": 91,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 14,
                "result'": 83,
                "num'": 93,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 2,
                "num": 91,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 83,
                "result'": 83,
                "num'": 93,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 3,
                "num": 93,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 83,
                "result'": 72,
                "num'": 27,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 3,
                "num": 93,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 72,
                "result'": 72,
                "num'": 27,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 4,
                "num": 27,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 72,
                "result'": 27,
                "num'": 83,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 4,
                "num": 27,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 27,
                "result'": 27,
                "num'": 83,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 5,
                "num": 83,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 27,
                "result'": 93,
                "num'": 70,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 5,
                "num": 83,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 93,
                "result'": 93,
                "num'": 70,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 6,
                "num": 70,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 93,
                "result'": 81,
                "num'": 12,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 6,
                "num": 70,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 81,
                "result'": 81,
                "num'": 12,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 7,
                "num": 12,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 81,
                "result'": 112,
                "num'": 33,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 7,
                "num": 12,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 112,
                "result'": 112,
                "num'": 33,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 8,
                "num": 33,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 112,
                "result'": 61,
                "num'": 77,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 8,
                "num": 33,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 61,
                "result'": 61,
                "num'": 77,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 9,
                "num": 77,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 61,
                "result'": 106,
                "num'": 87,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 9,
                "num": 77,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 106,
                "result'": 106,
                "num'": 87,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "ind#0": 10,
                "num": 87,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 106,
                "iter#0'": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "num": 87,
                "$cond": false,
                "$ret": "<undef>",
                "result": 106,
                "num'": 87,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ],
                "$ret'": 106,
                "nums": [
                    85,
                    91,
                    93,
                    27,
                    83,
                    70,
                    12,
                    33,
                    77,
                    87
                ]
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

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[46, 59, 20, 73, 53, 29, 4, 88, 10, 22]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 0,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 46,
                "num'": 46,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 46,
                "result'": 46,
                "num'": 46,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 1,
                "num": 46,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 46,
                "result'": 21,
                "num'": 59,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 1,
                "num": 46,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 21,
                "result'": 21,
                "num'": 59,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 2,
                "num": 59,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 21,
                "result'": 1,
                "num'": 20,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 2,
                "num": 59,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 1,
                "result'": 1,
                "num'": 20,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 3,
                "num": 20,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 1,
                "result'": 72,
                "num'": 73,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 3,
                "num": 20,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 72,
                "result'": 72,
                "num'": 73,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 4,
                "num": 73,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 72,
                "result'": 125,
                "num'": 53,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 4,
                "num": 73,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 125,
                "result'": 125,
                "num'": 53,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 5,
                "num": 53,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 125,
                "result'": 96,
                "num'": 29,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 5,
                "num": 53,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 96,
                "result'": 96,
                "num'": 29,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 6,
                "num": 29,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 96,
                "result'": 100,
                "num'": 4,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 6,
                "num": 29,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 100,
                "result'": 100,
                "num'": 4,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 7,
                "num": 4,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 100,
                "result'": 60,
                "num'": 88,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 7,
                "num": 4,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 60,
                "result'": 60,
                "num'": 88,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 8,
                "num": 88,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 60,
                "result'": 54,
                "num'": 10,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 8,
                "num": 88,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 54,
                "result'": 54,
                "num'": 10,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 9,
                "num": 10,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 54,
                "result'": 32,
                "num'": 22,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 9,
                "num": 10,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 32,
                "result'": 32,
                "num'": 22,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "ind#0": 10,
                "num": 22,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 32,
                "iter#0'": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "num": 22,
                "$cond": false,
                "$ret": "<undef>",
                "result": 32,
                "num'": 22,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ],
                "$ret'": 32,
                "nums": [
                    46,
                    59,
                    20,
                    73,
                    53,
                    29,
                    4,
                    88,
                    10,
                    22
                ]
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

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[99, 11, 23, 44, 17, 91, 86, 34, 73, 99]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 0,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 99,
                "num'": 99,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 99,
                "result'": 99,
                "num'": 99,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 1,
                "num": 99,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 99,
                "result'": 104,
                "num'": 11,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 1,
                "num": 99,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 104,
                "result'": 104,
                "num'": 11,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 2,
                "num": 11,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 104,
                "result'": 127,
                "num'": 23,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 2,
                "num": 11,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 127,
                "result'": 127,
                "num'": 23,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 3,
                "num": 23,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 127,
                "result'": 83,
                "num'": 44,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 3,
                "num": 23,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 83,
                "result'": 83,
                "num'": 44,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 4,
                "num": 44,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 83,
                "result'": 66,
                "num'": 17,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 4,
                "num": 44,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 66,
                "result'": 66,
                "num'": 17,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 5,
                "num": 17,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 66,
                "result'": 25,
                "num'": 91,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 5,
                "num": 17,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 25,
                "result'": 25,
                "num'": 91,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 6,
                "num": 91,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 25,
                "result'": 79,
                "num'": 86,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 6,
                "num": 91,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 79,
                "result'": 79,
                "num'": 86,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 7,
                "num": 86,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 79,
                "result'": 109,
                "num'": 34,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 7,
                "num": 86,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 109,
                "result'": 109,
                "num'": 34,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 8,
                "num": 34,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 109,
                "result'": 36,
                "num'": 73,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 8,
                "num": 34,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 36,
                "result'": 36,
                "num'": 73,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 9,
                "num": 73,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 36,
                "result'": 71,
                "num'": 99,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 9,
                "num": 73,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 71,
                "result'": 71,
                "num'": 99,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "ind#0": 10,
                "num": 99,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 71,
                "iter#0'": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "num": 99,
                "$cond": false,
                "$ret": "<undef>",
                "result": 71,
                "num'": 99,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ],
                "$ret'": 71,
                "nums": [
                    99,
                    11,
                    23,
                    44,
                    17,
                    91,
                    86,
                    34,
                    73,
                    99
                ]
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

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[72, 59, 53, 27, 5, 31, 39, 29, 49, 26]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 0,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 72,
                "num'": 72,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 72,
                "result'": 72,
                "num'": 72,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 1,
                "num": 72,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 72,
                "result'": 115,
                "num'": 59,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 1,
                "num": 72,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 115,
                "result'": 115,
                "num'": 59,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 2,
                "num": 59,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 115,
                "result'": 70,
                "num'": 53,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 2,
                "num": 59,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 70,
                "result'": 70,
                "num'": 53,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 3,
                "num": 53,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 70,
                "result'": 93,
                "num'": 27,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 3,
                "num": 53,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 93,
                "result'": 93,
                "num'": 27,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 4,
                "num": 27,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 93,
                "result'": 88,
                "num'": 5,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 4,
                "num": 27,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 88,
                "result'": 88,
                "num'": 5,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 5,
                "num": 5,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 88,
                "result'": 71,
                "num'": 31,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 5,
                "num": 5,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 71,
                "result'": 71,
                "num'": 31,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 6,
                "num": 31,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 71,
                "result'": 96,
                "num'": 39,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 6,
                "num": 31,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 96,
                "result'": 96,
                "num'": 39,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 7,
                "num": 39,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 96,
                "result'": 125,
                "num'": 29,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 7,
                "num": 39,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 125,
                "result'": 125,
                "num'": 29,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 8,
                "num": 29,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 125,
                "result'": 76,
                "num'": 49,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 8,
                "num": 29,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 76,
                "result'": 76,
                "num'": 49,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 9,
                "num": 49,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 76,
                "result'": 86,
                "num'": 26,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 9,
                "num": 49,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 86,
                "result'": 86,
                "num'": 26,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "ind#0": 10,
                "num": 26,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 86,
                "iter#0'": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "num": 26,
                "$cond": false,
                "$ret": "<undef>",
                "result": 86,
                "num'": 26,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ],
                "$ret'": 86,
                "nums": [
                    72,
                    59,
                    53,
                    27,
                    5,
                    31,
                    39,
                    29,
                    49,
                    26
                ]
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

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[71, 51, 99, 19, 43, 64, 53, 60, 22, 72]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 0,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 71,
                "num'": 71,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 71,
                "result'": 71,
                "num'": 71,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 1,
                "num": 71,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 71,
                "result'": 116,
                "num'": 51,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 1,
                "num": 71,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 116,
                "result'": 116,
                "num'": 51,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 2,
                "num": 51,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 116,
                "result'": 23,
                "num'": 99,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 2,
                "num": 51,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 23,
                "result'": 23,
                "num'": 99,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 3,
                "num": 99,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 23,
                "result'": 4,
                "num'": 19,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 3,
                "num": 99,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 4,
                "result'": 4,
                "num'": 19,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 4,
                "num": 19,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 4,
                "result'": 47,
                "num'": 43,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 4,
                "num": 19,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 47,
                "result'": 47,
                "num'": 43,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 5,
                "num": 43,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 47,
                "result'": 111,
                "num'": 64,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 5,
                "num": 43,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 111,
                "result'": 111,
                "num'": 64,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 6,
                "num": 64,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 111,
                "result'": 90,
                "num'": 53,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 6,
                "num": 64,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 90,
                "result'": 90,
                "num'": 53,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 7,
                "num": 53,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 90,
                "result'": 102,
                "num'": 60,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 7,
                "num": 53,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 102,
                "result'": 102,
                "num'": 60,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 8,
                "num": 60,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 102,
                "result'": 112,
                "num'": 22,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 8,
                "num": 60,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 112,
                "result'": 112,
                "num'": 22,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 9,
                "num": 22,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 112,
                "result'": 56,
                "num'": 72,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 9,
                "num": 22,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 56,
                "result'": 56,
                "num'": 72,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "ind#0": 10,
                "num": 72,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 56,
                "iter#0'": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "num": 72,
                "$cond": false,
                "$ret": "<undef>",
                "result": 56,
                "num'": 72,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ],
                "$ret'": 56,
                "nums": [
                    71,
                    51,
                    99,
                    19,
                    43,
                    64,
                    53,
                    60,
                    22,
                    72
                ]
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

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[23, 83, 53, 90, 59, 7, 14, 76, 72, 70]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 0,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 23,
                "num'": 23,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 23,
                "result'": 23,
                "num'": 23,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 1,
                "num": 23,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 23,
                "result'": 68,
                "num'": 83,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 1,
                "num": 23,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 68,
                "result'": 68,
                "num'": 83,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 2,
                "num": 83,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 68,
                "result'": 113,
                "num'": 53,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 2,
                "num": 83,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 113,
                "result'": 113,
                "num'": 53,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 3,
                "num": 53,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 113,
                "result'": 43,
                "num'": 90,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 3,
                "num": 53,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 43,
                "result'": 43,
                "num'": 90,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 4,
                "num": 90,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 43,
                "result'": 16,
                "num'": 59,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 4,
                "num": 90,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 16,
                "result'": 16,
                "num'": 59,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 5,
                "num": 59,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 16,
                "result'": 23,
                "num'": 7,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 5,
                "num": 59,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 23,
                "result'": 23,
                "num'": 7,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 6,
                "num": 7,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 23,
                "result'": 25,
                "num'": 14,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 6,
                "num": 7,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 25,
                "result'": 25,
                "num'": 14,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 7,
                "num": 14,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 25,
                "result'": 85,
                "num'": 76,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 7,
                "num": 14,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 85,
                "result'": 85,
                "num'": 76,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 8,
                "num": 76,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 85,
                "result'": 29,
                "num'": 72,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 8,
                "num": 76,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 29,
                "result'": 29,
                "num'": 72,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 9,
                "num": 72,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 29,
                "result'": 91,
                "num'": 70,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 9,
                "num": 72,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 91,
                "result'": 91,
                "num'": 70,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "ind#0": 10,
                "num": 70,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 91,
                "iter#0'": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "num": 70,
                "$cond": false,
                "$ret": "<undef>",
                "result": 91,
                "num'": 70,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ],
                "$ret'": 91,
                "nums": [
                    23,
                    83,
                    53,
                    90,
                    59,
                    7,
                    14,
                    76,
                    72,
                    70
                ]
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

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"singleNumber\": {\"name\": \"singleNumber\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"BitXor\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'singleNumber'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "singleNumber",
    "inputs": "[]",
    "args": "[[62, 94, 44, 7, 32, 69, 41, 42, 53, 75]]"
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
            "functionName": "singleNumber",
            "location": 1,
            "mem": {
                "result": "<undef>",
                "result'": 0,
                "ind#0'": 0,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 0,
                "result'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 0,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 0,
                "result'": 62,
                "num'": 62,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 0,
                "num": "<undef>",
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 62,
                "result'": 62,
                "num'": 62,
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 1,
                "num": 62,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 62,
                "result'": 96,
                "num'": 94,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 1,
                "num": 62,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 96,
                "result'": 96,
                "num'": 94,
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 2,
                "num": 94,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 96,
                "result'": 76,
                "num'": 44,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 2,
                "num": 94,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 76,
                "result'": 76,
                "num'": 44,
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 3,
                "num": 44,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 76,
                "result'": 75,
                "num'": 7,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 3,
                "num": 44,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 75,
                "result'": 75,
                "num'": 7,
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 4,
                "num": 7,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 75,
                "result'": 107,
                "num'": 32,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 4,
                "num": 7,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 107,
                "result'": 107,
                "num'": 32,
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 5,
                "num": 32,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 107,
                "result'": 46,
                "num'": 69,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 5,
                "num": 32,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 46,
                "result'": 46,
                "num'": 69,
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 6,
                "num": 69,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 46,
                "result'": 7,
                "num'": 41,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 6,
                "num": 69,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 7,
                "result'": 7,
                "num'": 41,
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 7,
                "num": 41,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 7,
                "result'": 45,
                "num'": 42,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 7,
                "num": 41,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 45,
                "result'": 45,
                "num'": 42,
                "ind#0'": 8,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 8,
                "num": 42,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 45,
                "result'": 24,
                "num'": 53,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 8,
                "num": 42,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 24,
                "result'": 24,
                "num'": 53,
                "ind#0'": 9,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 9,
                "num": 53,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 4,
            "mem": {
                "result": 24,
                "result'": 83,
                "num'": 75,
                "ind#0'": 10,
                "$cond'": true,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 9,
                "num": 53,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 2,
            "mem": {
                "result": 83,
                "result'": 83,
                "num'": 75,
                "ind#0'": 10,
                "$cond'": false,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "ind#0": 10,
                "num": 75,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "singleNumber",
            "location": 3,
            "mem": {
                "result'": 83,
                "iter#0'": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "num": 75,
                "$cond": false,
                "$ret": "<undef>",
                "result": 83,
                "num'": 75,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "iter#0": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ],
                "$ret'": 83,
                "nums": [
                    62,
                    94,
                    44,
                    7,
                    32,
                    69,
                    41,
                    42,
                    53,
                    75
                ]
            },
            "isChecked": false
        }
    ]
}
```

</details>

