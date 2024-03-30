# Test Report

Time: 2024-03-30 08:57:56.683225

### Base Program

```py
def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count
```

## Test Case 1

### Modified Program

```py

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[95, 65, 2, 91, 69, 4, 75, 76, 64, 24]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    95,
                    65,
                    2,
                    91,
                    69,
                    4,
                    75,
                    76,
                    64,
                    24
                ],
                "i'": 10,
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

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[90, 76, 12, 94, 64, 92, 24, 15, 21, 19]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    90,
                    76,
                    12,
                    94,
                    64,
                    92,
                    24,
                    15,
                    21,
                    19
                ],
                "i'": 10,
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

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[88, 69, 94, 81, 26, 20, 16, 78, 33, 81]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    88,
                    69,
                    94,
                    81,
                    26,
                    20,
                    16,
                    78,
                    33,
                    81
                ],
                "i'": 10,
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

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[74, 68, 28, 82, 20, 13, 7, 17, 37, 4]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    74,
                    68,
                    28,
                    82,
                    20,
                    13,
                    7,
                    17,
                    37,
                    4
                ],
                "i'": 10,
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

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[13, 65, 76, 88, 77, 15, 99, 83, 50, 95]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    13,
                    65,
                    76,
                    88,
                    77,
                    15,
                    99,
                    83,
                    50,
                    95
                ],
                "i'": 10,
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

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[5, 52, 39, 62, 0, 26, 73, 7, 36, 92]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    5,
                    52,
                    39,
                    62,
                    0,
                    26,
                    73,
                    7,
                    36,
                    92
                ],
                "i'": 10,
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

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[59, 78, 54, 86, 73, 81, 14, 51, 22, 100]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    59,
                    78,
                    54,
                    86,
                    73,
                    81,
                    14,
                    51,
                    22,
                    100
                ],
                "i'": 10,
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

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[5, 57, 2, 72, 55, 17, 80, 69, 82, 8]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    5,
                    57,
                    2,
                    72,
                    55,
                    17,
                    80,
                    69,
                    82,
                    8
                ],
                "i'": 10,
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

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[65, 21, 28, 71, 41, 32, 51, 7, 95, 53]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    65,
                    21,
                    28,
                    71,
                    41,
                    32,
                    51,
                    7,
                    95,
                    53
                ],
                "i'": 10,
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

def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"smooth_descent_periods\": {\"name\": \"smooth_descent_periods\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"prices\", \"val1\": \"*\", \"valueArray\": [\"prices\", \"*\"], \"valueList\": [\"prices\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"count\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"count\", {\"value\": \"0\", \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"1\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"1\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"count\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}], \"valueList\": [\"$ret\", {\"name\": \"count\", \"primed\": false, \"line\": 12}]}], \"4\": [], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"$cond\", {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}], \"6\": [], \"7\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Eq\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"prices\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"8\": [{\"val0\": \"count\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"count\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"9\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"10\": [], \"11\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 5}, \"5\": {\"false\": 11, \"true\": 6}, \"6\": {\"true\": 7}, \"7\": {\"false\": 8, \"true\": 9}, \"8\": {\"true\": 10}, \"9\": {\"true\": 7}, \"10\": {\"true\": 2}, \"11\": {\"true\": 10}}, \"locdescs\": {\"1\": \"around the beginning of function 'smooth_descent_periods'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\", \"5\": \"the condition of the if-statement at line 6\", \"6\": \"inside the if-branch starting at line 7\", \"7\": \"the condition of the 'while' loop at line 7\", \"8\": \"*after* the 'while' loop starting at line 7\", \"9\": \"inside the body of the 'while' loop beginning at line 8\", \"10\": \"after the if-statement beginning at line 6\", \"11\": \"inside the else-branch starting at line 11\"}, \"types\": {\"count\": \"*\", \"i\": \"*\"}}}}",
    "function": "smooth_descent_periods",
    "inputs": "[]",
    "args": "[[10, 8, 86, 94, 26, 33, 13, 85, 13, 29]]"
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
            "functionName": "smooth_descent_periods",
            "location": 1,
            "mem": {
                "count": "<undef>",
                "i": "<undef>",
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 1,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 1,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 2,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 2,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 3,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 3,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 4,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 4,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 5,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 5,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 5,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 6,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 6,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 7,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 7,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 7,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 8,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 8,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 8,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 9,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 4,
            "mem": {
                "$cond'": true,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 5,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 11,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 9,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 10,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 2,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 10,
                "$cond": false
            },
            "isChecked": false
        },
        {
            "functionName": "smooth_descent_periods",
            "location": 3,
            "mem": {
                "$cond'": false,
                "count": 0,
                "i": 10,
                "count'": 0,
                "$ret'": 0,
                "prices": [
                    10,
                    8,
                    86,
                    94,
                    26,
                    33,
                    13,
                    85,
                    13,
                    29
                ],
                "i'": 10,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

