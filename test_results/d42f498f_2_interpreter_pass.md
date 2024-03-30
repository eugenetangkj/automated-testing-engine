# Test Report

Time: 2024-03-30 07:52:30.204748

### Base Program

```py
def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result
```

## Test Case 1

### Modified Program

```py

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[40]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 40
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 40,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 40,
                "$cond": true,
                "x'": 4
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 4,
                "x'": 4,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 4,
                "rev": 0,
                "$cond'": true,
                "x": 4,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 4,
                "rev": 4,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 4,
                "rev": 4,
                "$cond'": false,
                "x": 0,
                "$ret'": 4,
                "x'": 0,
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

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[10]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 10
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 10,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 10,
                "$cond": true,
                "x'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 1,
                "x'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 1,
                "rev": 0,
                "$cond'": true,
                "x": 1,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 1,
                "rev": 1,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 1,
                "rev": 1,
                "$cond'": false,
                "x": 0,
                "$ret'": 1,
                "x'": 0,
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

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[34]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 34
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 34,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 4,
                "rev": 0,
                "$cond'": true,
                "x": 34,
                "$cond": true,
                "x'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 4,
                "rev": 4,
                "$cond'": true,
                "x": 3,
                "x'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 43,
                "rev": 4,
                "$cond'": true,
                "x": 3,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 43,
                "rev": 43,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 43,
                "rev": 43,
                "$cond'": false,
                "x": 0,
                "$ret'": 43,
                "x'": 0,
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

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[68]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 68
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 68,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 8,
                "rev": 0,
                "$cond'": true,
                "x": 68,
                "$cond": true,
                "x'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 8,
                "rev": 8,
                "$cond'": true,
                "x": 6,
                "x'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 86,
                "rev": 8,
                "$cond'": true,
                "x": 6,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 86,
                "rev": 86,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 86,
                "rev": 86,
                "$cond'": false,
                "x": 0,
                "$ret'": 86,
                "x'": 0,
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

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[18]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 18
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 18,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 8,
                "rev": 0,
                "$cond'": true,
                "x": 18,
                "$cond": true,
                "x'": 1
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 8,
                "rev": 8,
                "$cond'": true,
                "x": 1,
                "x'": 1,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 81,
                "rev": 8,
                "$cond'": true,
                "x": 1,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 81,
                "rev": 81,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 81,
                "rev": 81,
                "$cond'": false,
                "x": 0,
                "$ret'": 81,
                "x'": 0,
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

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[62]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 62
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 62,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 2,
                "rev": 0,
                "$cond'": true,
                "x": 62,
                "$cond": true,
                "x'": 6
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 2,
                "rev": 2,
                "$cond'": true,
                "x": 6,
                "x'": 6,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 26,
                "rev": 2,
                "$cond'": true,
                "x": 6,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 26,
                "rev": 26,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 26,
                "rev": 26,
                "$cond'": false,
                "x": 0,
                "$ret'": 26,
                "x'": 0,
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

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[92]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 92
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 92,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 2,
                "rev": 0,
                "$cond'": true,
                "x": 92,
                "$cond": true,
                "x'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 2,
                "rev": 2,
                "$cond'": true,
                "x": 9,
                "x'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 29,
                "rev": 2,
                "$cond'": true,
                "x": 9,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 29,
                "rev": 29,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 29,
                "rev": 29,
                "$cond'": false,
                "x": 0,
                "$ret'": 29,
                "x'": 0,
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

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[96]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 96
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 96,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 6,
                "rev": 0,
                "$cond'": true,
                "x": 96,
                "$cond": true,
                "x'": 9
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 6,
                "rev": 6,
                "$cond'": true,
                "x": 9,
                "x'": 9,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 69,
                "rev": 6,
                "$cond'": true,
                "x": 9,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 69,
                "rev": 69,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 69,
                "rev": 69,
                "$cond'": false,
                "x": 0,
                "$ret'": 69,
                "x'": 0,
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

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[20]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 20
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 20,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 20,
                "$cond": true,
                "x'": 2
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 2,
                "x'": 2,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 2,
                "rev": 0,
                "$cond'": true,
                "x": 2,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 2,
                "rev": 2,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 2,
                "rev": 2,
                "$cond'": false,
                "x": 0,
                "$ret'": 2,
                "x'": 0,
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

def reverse(x):
    rev = 0

    while x != 0:
        rev = rev * 10 + x % 10
        x = x // 10

    return rev

def count_nice_pairs(nums):
    MOD = 1_000_000_007
    count = {}
    result = 0

    for num in nums:
        diff = num - reverse(num)
        count[diff] = count.get(diff, 0) + 1

    for val in count.values():
        result = (result + ((val * (val - 1)) // 2) % MOD) % MOD

    return result


```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"count_nice_pairs\": {\"name\": \"count_nice_pairs\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"MOD\", \"val1\": {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}, \"valueArray\": [\"MOD\", {\"value\": \"1\", \"line\": 12}], \"valueList\": [\"MOD\", {\"value\": \"1\", \"line\": 12}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 13, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}], \"valueList\": [\"count\", {\"name\": \"DictInit\", \"args\": [], \"line\": 13}]}, {\"val0\": \"result\", \"val1\": {\"value\": \"0\", \"line\": 14, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"0\", \"line\": 14}], \"valueList\": [\"result\", {\"value\": \"0\", \"line\": 14}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"nums\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}], \"valueList\": [\"iter#0\", {\"name\": \"nums\", \"primed\": false, \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 16}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"3\": [{\"val0\": \"iter#1\", \"val1\": {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"iter#1\", {\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 20, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 20}]}], \"4\": [{\"val0\": \"num\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"num\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"reverse\", \"args\": [{\"name\": \"num\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17}]}, {\"val0\": \"count\", \"val1\": {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}], \"valueList\": [\"count\", {\"name\": \"AssignElement\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"get\", \"args\": [{\"name\": \"count\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"name\": \"diff\", \"primed\": true, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}], \"line\": 18}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}], \"line\": 20}]}], \"6\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 23, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 23}]}], \"7\": [{\"val0\": \"val\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}], \"valueList\": [\"val\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}], \"line\": 20}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 20, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 20, \"tokentype\": \"Constant\"}], \"line\": 20}]}, {\"val0\": \"result\", \"val1\": {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}], \"valueList\": [\"result\", {\"name\": \"Mod\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"name\": \"Sub\", \"args\": [{\"name\": \"val\", \"primed\": true, \"line\": 21, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 21, \"tokentype\": \"Constant\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21, \"tokentype\": \"Operation\"}], \"line\": 21, \"tokentype\": \"Operation\"}, {\"name\": \"MOD\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}], \"line\": 21}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 5}, \"4\": {\"true\": 2}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {}, \"7\": {\"true\": 5}}, \"locdescs\": {\"1\": \"around the beginning of function 'count_nice_pairs'\", \"2\": \"the condition of the 'for' loop at line 16\", \"3\": \"*after* the 'for' loop starting at line 16\", \"4\": \"inside the body of the 'for' loop beginning at line 17\", \"5\": \"the condition of the 'for' loop at line 20\", \"6\": \"*after* the 'for' loop starting at line 20\", \"7\": \"inside the body of the 'for' loop beginning at line 21\"}, \"types\": {\"result\": \"*\", \"val\": \"*\", \"MOD\": \"*\", \"ind#1\": \"int\", \"ind#0\": \"int\", \"num\": \"*\", \"count\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"diff\": \"*\"}}, \"reverse\": {\"name\": \"reverse\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"rev\", \"val1\": {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"rev\", {\"value\": \"0\", \"line\": 3}], \"valueList\": [\"rev\", {\"value\": \"0\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"rev\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"rev\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"rev\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}], \"valueList\": [\"rev\", {\"name\": \"Add\", \"args\": [{\"name\": \"Mult\", \"args\": [{\"name\": \"rev\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"Mod\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}], \"valueList\": [\"x\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"10\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'reverse'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"rev\": \"*\", \"x\": \"*\"}}}}",
    "function": "reverse",
    "inputs": "[]",
    "args": "[32]"
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
            "functionName": "reverse",
            "location": 1,
            "mem": {
                "rev'": 0,
                "rev": "<undef>",
                "x": 32
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 0,
                "rev": 0,
                "$cond'": true,
                "x": 32,
                "$cond": "<undef>"
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 2,
                "rev": 0,
                "$cond'": true,
                "x": 32,
                "$cond": true,
                "x'": 3
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 2,
                "rev": 2,
                "$cond'": true,
                "x": 3,
                "x'": 3,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 4,
            "mem": {
                "rev'": 23,
                "rev": 2,
                "$cond'": true,
                "x": 3,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 2,
            "mem": {
                "rev'": 23,
                "rev": 23,
                "$cond'": false,
                "x": 0,
                "x'": 0,
                "$cond": true
            },
            "isChecked": false
        },
        {
            "functionName": "reverse",
            "location": 3,
            "mem": {
                "rev'": 23,
                "rev": 23,
                "$cond'": false,
                "x": 0,
                "$ret'": 23,
                "x'": 0,
                "$cond": false,
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

