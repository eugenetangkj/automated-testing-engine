# Test Report

Time: 2024-03-30 07:45:30.746846

### Base Program

```py
def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count
```

## Test Case 1

### Modified Program

```py

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[51, 98, 100, 99, 13, 47, 89, 25, 98, 86]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 51,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 51,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 51,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 51,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 98,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 98,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 98,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 98,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 100,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 100,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 100,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 100,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 99,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 99,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 99,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 99,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 13,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 13,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 13,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 13,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 47,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 47,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 47,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 47,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 89,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 89,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 89,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 89,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 25,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 25,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 25,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 25,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 98,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 98,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 98,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 98,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 86,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 86,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 86,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "num": 86,
                "count": 0,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 86,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
                ],
                "$ret'": 0,
                "nums": [
                    51,
                    98,
                    100,
                    99,
                    13,
                    47,
                    89,
                    25,
                    98,
                    86
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

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[65, 69, 67, 50, 49, 51, 29, 16, 35, 31]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 65,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 65,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 65,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 65,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 69,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 69,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 69,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 69,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 67,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 67,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 67,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 67,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 50,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 50,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 50,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 50,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 49,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 49,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 49,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 49,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 51,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 51,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 51,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 51,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 29,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 29,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 29,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 29,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 16,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 16,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 16,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 16,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 35,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 35,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 35,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 35,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 31,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 31,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 31,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "num": 31,
                "count": 0,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 31,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
                ],
                "$ret'": 0,
                "nums": [
                    65,
                    69,
                    67,
                    50,
                    49,
                    51,
                    29,
                    16,
                    35,
                    31
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

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[61, 65, 84, 98, 69, 15, 77, 70, 26, 47]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 61,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 61,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 61,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 61,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 65,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 65,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 65,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 65,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 84,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 84,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 84,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 84,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 98,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 98,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 98,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 98,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 69,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 69,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 69,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 69,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 15,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 15,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 15,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 15,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 77,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 77,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 77,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 77,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 70,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 70,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 70,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 70,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 26,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 26,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 26,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 26,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 47,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 47,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 47,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "num": 47,
                "count": 0,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 47,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
                ],
                "$ret'": 0,
                "nums": [
                    61,
                    65,
                    84,
                    98,
                    69,
                    15,
                    77,
                    70,
                    26,
                    47
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

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[34, 84, 99, 51, 27, 8, 39, 99, 41, 2]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 34,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 34,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 34,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 34,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 84,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 84,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 84,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 84,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 99,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 99,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 99,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 99,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 51,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 51,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 51,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 51,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 27,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 27,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 27,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 27,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 8,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 8,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 8,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 8,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 39,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 39,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 39,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 39,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 99,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 99,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 99,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 99,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 41,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 41,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 41,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 41,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 2,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 2,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 2,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "num": 2,
                "count": 0,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 2,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
                ],
                "$ret'": 0,
                "nums": [
                    34,
                    84,
                    99,
                    51,
                    27,
                    8,
                    39,
                    99,
                    41,
                    2
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

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[78, 29, 33, 89, 26, 60, 38, 77, 24, 3]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 78,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 78,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 78,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 78,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 29,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 29,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 29,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 29,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 33,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 33,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 33,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 33,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 89,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 89,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 89,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 89,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 26,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 26,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 26,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 26,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 60,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 60,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 60,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 60,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 38,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 38,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 38,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 38,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 77,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 77,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 77,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 77,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 24,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 24,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 24,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 24,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 3,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 3,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 3,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "num": 3,
                "count": 0,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 3,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
                ],
                "$ret'": 0,
                "nums": [
                    78,
                    29,
                    33,
                    89,
                    26,
                    60,
                    38,
                    77,
                    24,
                    3
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

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[36, 58, 85, 88, 84, 23, 62, 59, 63, 79]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 36,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 36,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 36,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 36,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 58,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 58,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 58,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 58,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 85,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 85,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 85,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 85,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 88,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 88,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 88,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 88,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 84,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 84,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 84,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 84,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 23,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 23,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 23,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 23,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 62,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 62,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 62,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 62,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 59,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 59,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 59,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 59,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 63,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 63,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 63,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 63,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 79,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 79,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 79,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "num": 79,
                "count": 0,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 79,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
                ],
                "$ret'": 0,
                "nums": [
                    36,
                    58,
                    85,
                    88,
                    84,
                    23,
                    62,
                    59,
                    63,
                    79
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

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[53, 26, 68, 18, 89, 82, 22, 95, 99, 96]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 53,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 53,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 53,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 53,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 26,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 26,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 26,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 26,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 68,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 68,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 68,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 68,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 18,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 18,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 18,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 18,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 89,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 89,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 89,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 89,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 82,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 82,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 82,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 82,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 22,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 22,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 22,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 22,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 95,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 95,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 95,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 95,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 99,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 99,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 99,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 99,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 96,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 96,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 96,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "num": 96,
                "count": 0,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 96,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
                ],
                "$ret'": 0,
                "nums": [
                    53,
                    26,
                    68,
                    18,
                    89,
                    82,
                    22,
                    95,
                    99,
                    96
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

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[44, 19, 88, 33, 45, 48, 6, 92, 68, 62]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 44,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 44,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 44,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 44,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 19,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 19,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 19,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 19,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 88,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 88,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 88,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 88,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 33,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 33,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 33,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 33,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 45,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 45,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 45,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 45,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 48,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 48,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 48,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 48,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 6,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 6,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 6,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 6,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 92,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 92,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 92,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 92,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 68,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 68,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 68,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 68,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 62,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 62,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 62,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "num": 62,
                "count": 0,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 62,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
                ],
                "$ret'": 0,
                "nums": [
                    44,
                    19,
                    88,
                    33,
                    45,
                    48,
                    6,
                    92,
                    68,
                    62
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

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[54, 97, 95, 85, 8, 12, 41, 33, 10, 87]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 54,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 54,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 54,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 54,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 97,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 97,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 97,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 97,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 95,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 95,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 95,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 95,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 85,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 85,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 85,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 85,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 8,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 8,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 8,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 8,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 12,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 12,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 12,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 12,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 41,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 41,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 41,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 41,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 33,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 33,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 33,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 33,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 10,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 10,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 10,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 10,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 87,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 87,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 87,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "num": 87,
                "count": 0,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 87,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 0,
                "iter#0": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
                ],
                "$ret'": 0,
                "nums": [
                    54,
                    97,
                    95,
                    85,
                    8,
                    12,
                    41,
                    33,
                    10,
                    87
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

def numberOfSubarraysWithZeroes(nums):
    count = 0
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
            count += zero_count
        else:
            zero_count = 0

    return count



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"numberOfSubarraysWithZeroes\": {\"name\": \"numberOfSubarraysWithZeroes\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"zero_count\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"zero_count\", {\"value\": \"0\", \"line\": 4}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 6}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 13}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}, {\"val0\": \"zero_count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"zero_count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 7}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}], \"valueList\": [\"count\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"zero_count\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"count\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'numberOfSubarraysWithZeroes'\", \"2\": \"the condition of the 'for' loop at line 6\", \"3\": \"*after* the 'for' loop starting at line 6\", \"4\": \"inside the body of the 'for' loop beginning at line 7\"}, \"types\": {\"zero_count\": \"*\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "numberOfSubarraysWithZeroes",
    "inputs": "[]",
    "args": "[[10, 0, 24, 70, 45, 8, 95, 31, 9, 3]]"
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
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "zero_count": "<undef>",
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "ind#0": "<undef>",
                "count": "<undef>",
                "count'": 0,
                "zero_count'": 0,
                "iter#0": "<undef>",
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "ind#0": 0,
                "count": 0,
                "zero_count'": 0,
                "count'": 0,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": "<undef>",
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 10,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "count'": 0,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 10,
                "count": 0,
                "zero_count'": 0,
                "$cond": true,
                "num'": 10,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "count'": 0,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 10,
                "count": 0,
                "zero_count'": 1,
                "$cond": true,
                "num'": 0,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 1,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 0,
                "count": 1,
                "zero_count'": 1,
                "$cond": true,
                "num'": 0,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 1,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 0,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 24,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 24,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 24,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 24,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 70,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 70,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 70,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 70,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 45,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 45,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 45,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 45,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 8,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 8,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 8,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 8,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 95,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 95,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 95,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 7,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 95,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 31,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 7,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 31,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 31,
                "ind#0'": 8,
                "$cond'": true,
                "ind#0": 8,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 31,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 9,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 8,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 9,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 9,
                "ind#0'": 9,
                "$cond'": true,
                "ind#0": 9,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 4,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 9,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 3,
                "ind#0'": 10,
                "$cond'": true,
                "ind#0": 9,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 2,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 3,
                "count": 1,
                "zero_count'": 0,
                "$cond": true,
                "num'": 3,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "numberOfSubarraysWithZeroes",
            "location": 3,
            "mem": {
                "zero_count": 0,
                "iter#0'": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "num": 3,
                "count": 1,
                "zero_count'": 0,
                "$cond": false,
                "$ret": "<undef>",
                "num'": 3,
                "ind#0'": 10,
                "$cond'": false,
                "ind#0": 10,
                "count'": 1,
                "iter#0": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ],
                "$ret'": 1,
                "nums": [
                    10,
                    0,
                    24,
                    70,
                    45,
                    8,
                    95,
                    31,
                    9,
                    3
                ]
            },
            "isChecked": false
        }
    ]
}
```

</details>

