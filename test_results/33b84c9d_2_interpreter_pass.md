# Test Report

Time: 2024-04-14 07:31:31.728755

### Base Program

```py
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

## Test Case 1

### Modified Program

```py
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[86]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 86,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 86,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 86,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": false,
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
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
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[91]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 4,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 3,
                "i": 4,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 4,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 3,
                "i": 4,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 5,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 4,
                "i": 5,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 5,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 4,
                "i": 5,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 6,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 5,
                "i": 6,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "i'": 6,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 91,
                "ind#0": 5,
                "i": 6,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": false,
                "i'": 7,
                "$ret": "<undef>",
                "$cond": true
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
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[66]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 66,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 66,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 66,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": false,
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
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
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[11]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3
                ],
                "num": 11,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3
                ],
                "num": 11,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3
                ],
                "num": 11,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3
                ],
                "num": 11,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3
                ],
                "num": 11,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 2,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3
                ],
                "num": 11,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 6,
            "mem": {
                "ind#0'": 2,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3
                ],
                "num": 11,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3
                ],
                "$ret'": true,
                "i'": 3,
                "$ret": "<undef>",
                "$cond": false
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
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[90]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 90,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 90,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 90,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": false,
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
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
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[52]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 52,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 52,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 52,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": false,
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
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
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[71]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 4,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 3,
                "i": 4,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 4,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 3,
                "i": 4,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 5,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 4,
                "i": 5,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 5,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 4,
                "i": 5,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 6,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 5,
                "i": 6,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 6,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 5,
                "i": 6,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 7,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 6,
                "i": 7,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 7,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 6,
                "i": 7,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 8,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 7,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 7,
                "i": 8,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 8,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 6,
            "mem": {
                "ind#0'": 7,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 7,
                "i": 8,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": true,
                "i'": 8,
                "$ret": "<undef>",
                "$cond": false
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
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[59]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 4,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 3,
                "i": 4,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 4,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 3,
                "i": 4,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 5,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 4,
                "i": 5,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 5,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 4,
                "i": 5,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 6,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 5,
                "i": 6,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 6,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 5,
                "i": 6,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 7,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 6,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 6,
                "i": 7,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": "<undef>",
                "i'": 7,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 6,
            "mem": {
                "ind#0'": 6,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "num": 59,
                "ind#0": 6,
                "i": 7,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7
                ],
                "$ret'": true,
                "i'": 7,
                "$ret": "<undef>",
                "$cond": false
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
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[94]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 94,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 94,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "num": 94,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9
                ],
                "$ret'": false,
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
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
def prime_check(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"prime_check\": {\"name\": \"prime_check\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"num\", \"val1\": \"*\", \"valueArray\": [\"num\", \"*\"], \"valueList\": [\"num\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"iter#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}], \"valueList\": [\"iter#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"name\": \"range\", \"args\": [{\"value\": \"2\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"int\", \"args\": [{\"name\": \"Pow\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0.5\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}], \"valueList\": [\"ind#0\", {\"name\": \"ite\", \"args\": [{\"name\": \"Not\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"originalExpr\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 2}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"True\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"True\", \"line\": 7}], \"valueList\": [\"$ret\", {\"value\": \"True\", \"line\": 7}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"i\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"num\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"False\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"$ret\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'prime_check'\", \"5\": \"the condition of the 'for' loop at line 4\", \"6\": \"*after* the 'for' loop starting at line 4\", \"7\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"ind#0\": \"int\", \"i\": \"*\", \"iter#0\": \"int\"}}}}",
    "function": "prime_check",
    "inputs": "[]",
    "args": "[71]"
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
            "functionName": "prime_check",
            "location": 1,
            "mem": {
                "ind#0'": 0,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "$ret'": "<undef>",
                "$ret": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 0,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 0,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "$ret": "<undef>",
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 0,
                "i": "<undef>",
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 1,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 2,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 1,
                "i": 2,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 2,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 3,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 2,
                "i": 3,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 4,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 3,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 3,
                "i": 4,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 4,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 3,
                "i": 4,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 5,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 4,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 4,
                "i": 5,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 5,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 4,
                "i": 5,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 6,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 5,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 5,
                "i": 6,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 6,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 5,
                "i": 6,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 7,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 6,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 6,
                "i": 7,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 7,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 7,
            "mem": {
                "ind#0'": 7,
                "$cond'": true,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 6,
                "i": 7,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 8,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 5,
            "mem": {
                "ind#0'": 7,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 7,
                "i": 8,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": "<undef>",
                "i'": 8,
                "$ret": "<undef>",
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "prime_check",
            "location": 6,
            "mem": {
                "ind#0'": 7,
                "$cond'": false,
                "iter#0'": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "num": 71,
                "ind#0": 7,
                "i": 8,
                "iter#0": [
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8
                ],
                "$ret'": true,
                "i'": 8,
                "$ret": "<undef>",
                "$cond": false
            },
            "isChecked": false
        }
    ]
}
```

</details>

