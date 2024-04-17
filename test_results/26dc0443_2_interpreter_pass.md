# Test Report

Time: 2024-04-17 10:16 PM

### Base Program

```py
def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count
```

## Test Case 1

### Modified Program

```py

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[54, 30]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 54,
                "count": "<undef>",
                "count'": 0,
                "num2": 30
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 54,
                "count": 0,
                "count'": 0,
                "num2": 30,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 54,
                "count": 0,
                "num1'": 24,
                "count'": 1,
                "num2": 30,
                "$cond": true,
                "num2'": 30
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 24,
                "num1'": 24,
                "count": 1,
                "count'": 1,
                "num2": 30,
                "num2'": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 24,
                "num1'": 24,
                "count": 1,
                "count'": 2,
                "num2": 30,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 24,
                "num1'": 24,
                "count": 2,
                "count'": 2,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 24,
                "num1'": 18,
                "count": 2,
                "count'": 3,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 18,
                "count": 3,
                "count'": 3,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 12,
                "count": 3,
                "count'": 4,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 12,
                "num1'": 12,
                "count": 4,
                "count'": 4,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 12,
                "num1'": 6,
                "count": 4,
                "count'": 5,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 6,
                "num1'": 6,
                "count": 5,
                "count'": 5,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 6,
                "num1'": 0,
                "count": 5,
                "count'": 6,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 6,
                "count'": 6,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 6,
                "count'": 6,
                "$ret'": 6,
                "num2": 6,
                "num2'": 6,
                "$cond": false,
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

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[18, 67]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 18,
                "count": "<undef>",
                "count'": 0,
                "num2": 67
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "count": 0,
                "count'": 0,
                "num2": 67,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "count": 0,
                "num1'": 18,
                "count'": 1,
                "num2": 67,
                "$cond": true,
                "num2'": 49
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 18,
                "count": 1,
                "count'": 1,
                "num2": 49,
                "num2'": 49,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 18,
                "count": 1,
                "count'": 2,
                "num2": 49,
                "num2'": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 18,
                "count": 2,
                "count'": 2,
                "num2": 31,
                "num2'": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 18,
                "count": 2,
                "count'": 3,
                "num2": 31,
                "num2'": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 18,
                "count": 3,
                "count'": 3,
                "num2": 13,
                "num2'": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 5,
                "count": 3,
                "count'": 4,
                "num2": 13,
                "num2'": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 4,
                "count'": 4,
                "num2": 13,
                "num2'": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 4,
                "count'": 5,
                "num2": 13,
                "num2'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 5,
                "count'": 5,
                "num2": 8,
                "num2'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 5,
                "count'": 6,
                "num2": 8,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 6,
                "count'": 6,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 2,
                "count": 6,
                "count'": 7,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 2,
                "count": 7,
                "count'": 7,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 2,
                "count": 7,
                "count'": 8,
                "num2": 3,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 2,
                "count": 8,
                "count'": 8,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 1,
                "count": 8,
                "count'": 9,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 1,
                "count": 9,
                "count'": 9,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 0,
                "count": 9,
                "count'": 10,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 10,
                "count'": 10,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 10,
                "count'": 10,
                "$ret'": 10,
                "num2": 1,
                "num2'": 1,
                "$cond": false,
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

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[11, 46]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 11,
                "count": "<undef>",
                "count'": 0,
                "num2": 46
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "count": 0,
                "count'": 0,
                "num2": 46,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "count": 0,
                "num1'": 11,
                "count'": 1,
                "num2": 46,
                "$cond": true,
                "num2'": 35
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 11,
                "count": 1,
                "count'": 1,
                "num2": 35,
                "num2'": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 11,
                "count": 1,
                "count'": 2,
                "num2": 35,
                "num2'": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 11,
                "count": 2,
                "count'": 2,
                "num2": 24,
                "num2'": 24,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 11,
                "count": 2,
                "count'": 3,
                "num2": 24,
                "num2'": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 11,
                "count": 3,
                "count'": 3,
                "num2": 13,
                "num2'": 13,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 11,
                "count": 3,
                "count'": 4,
                "num2": 13,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 11,
                "count": 4,
                "count'": 4,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 9,
                "count": 4,
                "count'": 5,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 5,
                "count'": 5,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 7,
                "count": 5,
                "count'": 6,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 7,
                "num1'": 7,
                "count": 6,
                "count'": 6,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 7,
                "num1'": 5,
                "count": 6,
                "count'": 7,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 7,
                "count'": 7,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 3,
                "count": 7,
                "count'": 8,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 3,
                "count": 8,
                "count'": 8,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 1,
                "count": 8,
                "count'": 9,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 1,
                "count": 9,
                "count'": 9,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 1,
                "count": 9,
                "count'": 10,
                "num2": 2,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 1,
                "count": 10,
                "count'": 10,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 0,
                "count": 10,
                "count'": 11,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 11,
                "count'": 11,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 11,
                "count'": 11,
                "$ret'": 11,
                "num2": 1,
                "num2'": 1,
                "$cond": false,
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

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[26, 100]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 26,
                "count": "<undef>",
                "count'": 0,
                "num2": 100
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 26,
                "count": 0,
                "count'": 0,
                "num2": 100,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 26,
                "count": 0,
                "num1'": 26,
                "count'": 1,
                "num2": 100,
                "$cond": true,
                "num2'": 74
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 26,
                "num1'": 26,
                "count": 1,
                "count'": 1,
                "num2": 74,
                "num2'": 74,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 26,
                "num1'": 26,
                "count": 1,
                "count'": 2,
                "num2": 74,
                "num2'": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 26,
                "num1'": 26,
                "count": 2,
                "count'": 2,
                "num2": 48,
                "num2'": 48,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 26,
                "num1'": 26,
                "count": 2,
                "count'": 3,
                "num2": 48,
                "num2'": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 26,
                "num1'": 26,
                "count": 3,
                "count'": 3,
                "num2": 22,
                "num2'": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 26,
                "num1'": 4,
                "count": 3,
                "count'": 4,
                "num2": 22,
                "num2'": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 4,
                "count'": 4,
                "num2": 22,
                "num2'": 22,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 4,
                "count'": 5,
                "num2": 22,
                "num2'": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 5,
                "count'": 5,
                "num2": 18,
                "num2'": 18,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 5,
                "count'": 6,
                "num2": 18,
                "num2'": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 6,
                "count'": 6,
                "num2": 14,
                "num2'": 14,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 6,
                "count'": 7,
                "num2": 14,
                "num2'": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 7,
                "count'": 7,
                "num2": 10,
                "num2'": 10,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 7,
                "count'": 8,
                "num2": 10,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 8,
                "count'": 8,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 8,
                "count'": 9,
                "num2": 6,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 9,
                "count'": 9,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 2,
                "count": 9,
                "count'": 10,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 2,
                "count": 10,
                "count'": 10,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 0,
                "count": 10,
                "count'": 11,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 11,
                "count'": 11,
                "num2": 2,
                "num2'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 11,
                "count'": 11,
                "$ret'": 11,
                "num2": 2,
                "num2'": 2,
                "$cond": false,
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

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[21, 3]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 21,
                "count": "<undef>",
                "count'": 0,
                "num2": 3
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 21,
                "count": 0,
                "count'": 0,
                "num2": 3,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 21,
                "count": 0,
                "num1'": 18,
                "count'": 1,
                "num2": 3,
                "$cond": true,
                "num2'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 18,
                "count": 1,
                "count'": 1,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 18,
                "num1'": 15,
                "count": 1,
                "count'": 2,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 15,
                "count": 2,
                "count'": 2,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 12,
                "count": 2,
                "count'": 3,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 12,
                "num1'": 12,
                "count": 3,
                "count'": 3,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 12,
                "num1'": 9,
                "count": 3,
                "count'": 4,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 4,
                "count'": 4,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 6,
                "count": 4,
                "count'": 5,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 6,
                "num1'": 6,
                "count": 5,
                "count'": 5,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 6,
                "num1'": 3,
                "count": 5,
                "count'": 6,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 3,
                "count": 6,
                "count'": 6,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 0,
                "count": 6,
                "count'": 7,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 7,
                "count'": 7,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 7,
                "count'": 7,
                "$ret'": 7,
                "num2": 3,
                "num2'": 3,
                "$cond": false,
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

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[99, 80]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 99,
                "count": "<undef>",
                "count'": 0,
                "num2": 80
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 99,
                "count": 0,
                "count'": 0,
                "num2": 80,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 99,
                "count": 0,
                "num1'": 19,
                "count'": 1,
                "num2": 80,
                "$cond": true,
                "num2'": 80
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 19,
                "count": 1,
                "count'": 1,
                "num2": 80,
                "num2'": 80,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 19,
                "count": 1,
                "count'": 2,
                "num2": 80,
                "num2'": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 19,
                "count": 2,
                "count'": 2,
                "num2": 61,
                "num2'": 61,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 19,
                "count": 2,
                "count'": 3,
                "num2": 61,
                "num2'": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 19,
                "count": 3,
                "count'": 3,
                "num2": 42,
                "num2'": 42,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 19,
                "count": 3,
                "count'": 4,
                "num2": 42,
                "num2'": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 19,
                "count": 4,
                "count'": 4,
                "num2": 23,
                "num2'": 23,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 19,
                "count": 4,
                "count'": 5,
                "num2": 23,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 19,
                "count": 5,
                "count'": 5,
                "num2": 4,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 19,
                "num1'": 15,
                "count": 5,
                "count'": 6,
                "num2": 4,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 15,
                "count": 6,
                "count'": 6,
                "num2": 4,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 11,
                "count": 6,
                "count'": 7,
                "num2": 4,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 11,
                "count": 7,
                "count'": 7,
                "num2": 4,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 11,
                "num1'": 7,
                "count": 7,
                "count'": 8,
                "num2": 4,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 7,
                "num1'": 7,
                "count": 8,
                "count'": 8,
                "num2": 4,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 7,
                "num1'": 3,
                "count": 8,
                "count'": 9,
                "num2": 4,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 3,
                "count": 9,
                "count'": 9,
                "num2": 4,
                "num2'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 3,
                "count": 9,
                "count'": 10,
                "num2": 4,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 3,
                "count": 10,
                "count'": 10,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 2,
                "count": 10,
                "count'": 11,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 2,
                "count": 11,
                "count'": 11,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 1,
                "count": 11,
                "count'": 12,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 1,
                "count": 12,
                "count'": 12,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 0,
                "count": 12,
                "count'": 13,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 13,
                "count'": 13,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 13,
                "count'": 13,
                "$ret'": 13,
                "num2": 1,
                "num2'": 1,
                "$cond": false,
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

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[10, 75]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 10,
                "count": "<undef>",
                "count'": 0,
                "num2": 75
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "count": 0,
                "count'": 0,
                "num2": 75,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "count": 0,
                "num1'": 10,
                "count'": 1,
                "num2": 75,
                "$cond": true,
                "num2'": 65
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 1,
                "count'": 1,
                "num2": 65,
                "num2'": 65,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 1,
                "count'": 2,
                "num2": 65,
                "num2'": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 2,
                "count'": 2,
                "num2": 55,
                "num2'": 55,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 2,
                "count'": 3,
                "num2": 55,
                "num2'": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 3,
                "count'": 3,
                "num2": 45,
                "num2'": 45,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 3,
                "count'": 4,
                "num2": 45,
                "num2'": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 4,
                "count'": 4,
                "num2": 35,
                "num2'": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 4,
                "count'": 5,
                "num2": 35,
                "num2'": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 5,
                "count'": 5,
                "num2": 25,
                "num2'": 25,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 5,
                "count'": 6,
                "num2": 25,
                "num2'": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 6,
                "count'": 6,
                "num2": 15,
                "num2'": 15,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 6,
                "count'": 7,
                "num2": 15,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 7,
                "count'": 7,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 5,
                "count": 7,
                "count'": 8,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 8,
                "count'": 8,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 0,
                "count": 8,
                "count'": 9,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 9,
                "count'": 9,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 9,
                "count'": 9,
                "$ret'": 9,
                "num2": 5,
                "num2'": 5,
                "$cond": false,
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

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[9, 48]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 9,
                "count": "<undef>",
                "count'": 0,
                "num2": 48
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "count": 0,
                "count'": 0,
                "num2": 48,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "count": 0,
                "num1'": 9,
                "count'": 1,
                "num2": 48,
                "$cond": true,
                "num2'": 39
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 1,
                "count'": 1,
                "num2": 39,
                "num2'": 39,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 1,
                "count'": 2,
                "num2": 39,
                "num2'": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 2,
                "count'": 2,
                "num2": 30,
                "num2'": 30,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 2,
                "count'": 3,
                "num2": 30,
                "num2'": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 3,
                "count'": 3,
                "num2": 21,
                "num2'": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 3,
                "count'": 4,
                "num2": 21,
                "num2'": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 4,
                "count'": 4,
                "num2": 12,
                "num2'": 12,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 4,
                "count'": 5,
                "num2": 12,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 9,
                "count": 5,
                "count'": 5,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 9,
                "num1'": 6,
                "count": 5,
                "count'": 6,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 6,
                "num1'": 6,
                "count": 6,
                "count'": 6,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 6,
                "num1'": 3,
                "count": 6,
                "count'": 7,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 3,
                "count": 7,
                "count'": 7,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 0,
                "count": 7,
                "count'": 8,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 8,
                "count'": 8,
                "num2": 3,
                "num2'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 8,
                "count'": 8,
                "$ret'": 8,
                "num2": 3,
                "num2'": 3,
                "$cond": false,
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

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[5, 61]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 5,
                "count": "<undef>",
                "count'": 0,
                "num2": 61
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "count": 0,
                "count'": 0,
                "num2": 61,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "count": 0,
                "num1'": 5,
                "count'": 1,
                "num2": 61,
                "$cond": true,
                "num2'": 56
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 1,
                "count'": 1,
                "num2": 56,
                "num2'": 56,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 1,
                "count'": 2,
                "num2": 56,
                "num2'": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 2,
                "count'": 2,
                "num2": 51,
                "num2'": 51,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 2,
                "count'": 3,
                "num2": 51,
                "num2'": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 3,
                "count'": 3,
                "num2": 46,
                "num2'": 46,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 3,
                "count'": 4,
                "num2": 46,
                "num2'": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 4,
                "count'": 4,
                "num2": 41,
                "num2'": 41,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 4,
                "count'": 5,
                "num2": 41,
                "num2'": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 5,
                "count'": 5,
                "num2": 36,
                "num2'": 36,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 5,
                "count'": 6,
                "num2": 36,
                "num2'": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 6,
                "count'": 6,
                "num2": 31,
                "num2'": 31,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 6,
                "count'": 7,
                "num2": 31,
                "num2'": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 7,
                "count'": 7,
                "num2": 26,
                "num2'": 26,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 7,
                "count'": 8,
                "num2": 26,
                "num2'": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 8,
                "count'": 8,
                "num2": 21,
                "num2'": 21,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 8,
                "count'": 9,
                "num2": 21,
                "num2'": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 9,
                "count'": 9,
                "num2": 16,
                "num2'": 16,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 9,
                "count'": 10,
                "num2": 16,
                "num2'": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 10,
                "count'": 10,
                "num2": 11,
                "num2'": 11,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 10,
                "count'": 11,
                "num2": 11,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 11,
                "count'": 11,
                "num2": 6,
                "num2'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 11,
                "count'": 12,
                "num2": 6,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 12,
                "count'": 12,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 4,
                "count": 12,
                "count'": 13,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 4,
                "count": 13,
                "count'": 13,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 4,
                "num1'": 3,
                "count": 13,
                "count'": 14,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 3,
                "count": 14,
                "count'": 14,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 3,
                "num1'": 2,
                "count": 14,
                "count'": 15,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 2,
                "count": 15,
                "count'": 15,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 2,
                "num1'": 1,
                "count": 15,
                "count'": 16,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 1,
                "count": 16,
                "count'": 16,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 1,
                "num1'": 0,
                "count": 16,
                "count'": 17,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 17,
                "count'": 17,
                "num2": 1,
                "num2'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 17,
                "count'": 17,
                "$ret'": 17,
                "num2": 1,
                "num2'": 1,
                "$cond": false,
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

def operations(num1, num2):
    count = 0
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"operations\": {\"name\": \"operations\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num1\", \"val1\": \"*\", \"valueArray\": [\"num1\", \"*\"], \"valueList\": [\"num1\", \"*\"]}, {\"val0\": \"num2\", \"val1\": \"*\", \"valueArray\": [\"num2\", \"*\"], \"valueList\": [\"num2\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"NotEq\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"NotEq\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 10}]}], \"4\": [{\"val0\": \"num1\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"num1\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"num2\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"num2\", {\"name\": \"ite\", \"args\": [{\"name\": \"GtE\", \"args\": [{\"name\": \"num1\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"num2\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"num2\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"num1\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 5}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'operations'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"count\": \"*\", \"num1\": \"*\", \"num2\": \"*\"}}}}",
    "function": "operations",
    "inputs": "[]",
    "args": "[65, 50]"
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
            "functionName": "operations",
            "location": 1,
            "mem": {
                "num1": 65,
                "count": "<undef>",
                "count'": 0,
                "num2": 50
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 65,
                "count": 0,
                "count'": 0,
                "num2": 50,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 65,
                "count": 0,
                "num1'": 15,
                "count'": 1,
                "num2": 50,
                "$cond": true,
                "num2'": 50
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 15,
                "count": 1,
                "count'": 1,
                "num2": 50,
                "num2'": 50,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 15,
                "count": 1,
                "count'": 2,
                "num2": 50,
                "num2'": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 15,
                "count": 2,
                "count'": 2,
                "num2": 35,
                "num2'": 35,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 15,
                "count": 2,
                "count'": 3,
                "num2": 35,
                "num2'": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 15,
                "count": 3,
                "count'": 3,
                "num2": 20,
                "num2'": 20,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 15,
                "count": 3,
                "count'": 4,
                "num2": 20,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 15,
                "count": 4,
                "count'": 4,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 15,
                "num1'": 10,
                "count": 4,
                "count'": 5,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 10,
                "count": 5,
                "count'": 5,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 10,
                "num1'": 5,
                "count": 5,
                "count'": 6,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 5,
                "count": 6,
                "count'": 6,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 4,
            "mem": {
                "$cond'": true,
                "num1": 5,
                "num1'": 0,
                "count": 6,
                "count'": 7,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 2,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 7,
                "count'": 7,
                "num2": 5,
                "num2'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "operations",
            "location": 3,
            "mem": {
                "$cond'": false,
                "num1": 0,
                "num1'": 0,
                "count": 7,
                "count'": 7,
                "$ret'": 7,
                "num2": 5,
                "num2'": 5,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

