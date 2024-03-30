# Test Report

Time: 2024-03-30 08:32:26.855172

### Base Program

```py
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

## Test Case 1

### Modified Program

```py

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[25, 55, 56, 12, 84, 7, 67, 87, 30, 26]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": false,
                "nums": [
                    25,
                    55,
                    56,
                    12,
                    84,
                    7,
                    67,
                    87,
                    30,
                    26
                ],
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

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[42, 91, 45, 94, 53, 93, 5, 31, 18, 81]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": false,
                "nums": [
                    42,
                    91,
                    45,
                    94,
                    53,
                    93,
                    5,
                    31,
                    18,
                    81
                ],
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

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[83, 18, 94, 15, 1, 64, 20, 81, 92, 83]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": true,
                "nums": [
                    83,
                    18,
                    94,
                    15,
                    1,
                    64,
                    20,
                    81,
                    92,
                    83
                ],
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

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[51, 90, 26, 43, 0, 84, 63, 78, 68, 29]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": false,
                "nums": [
                    51,
                    90,
                    26,
                    43,
                    0,
                    84,
                    63,
                    78,
                    68,
                    29
                ],
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

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[27, 34, 9, 1, 69, 72, 36, 79, 94, 69]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": true,
                "nums": [
                    27,
                    34,
                    9,
                    1,
                    69,
                    72,
                    36,
                    79,
                    94,
                    69
                ],
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

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[57, 57, 32, 13, 53, 52, 12, 65, 35, 14]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": true,
                "nums": [
                    57,
                    57,
                    32,
                    13,
                    53,
                    52,
                    12,
                    65,
                    35,
                    14
                ],
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

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[55, 14, 83, 96, 91, 16, 89, 48, 70, 86]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": false,
                "nums": [
                    55,
                    14,
                    83,
                    96,
                    91,
                    16,
                    89,
                    48,
                    70,
                    86
                ],
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

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[65, 19, 15, 3, 77, 35, 29, 38, 100, 78]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": false,
                "nums": [
                    65,
                    19,
                    15,
                    3,
                    77,
                    35,
                    29,
                    38,
                    100,
                    78
                ],
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

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[86, 67, 8, 56, 59, 86, 22, 66, 1, 23]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": true,
                "nums": [
                    86,
                    67,
                    8,
                    56,
                    59,
                    86,
                    22,
                    66,
                    1,
                    23
                ],
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

def containsDuplicate(nums):
    return len(nums) != len(set(nums))



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"containsDuplicate\": {\"name\": \"containsDuplicate\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"NotEq\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"set\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'containsDuplicate'\"}, \"types\": {}}}}",
    "function": "containsDuplicate",
    "inputs": "[]",
    "args": "[[30, 14, 78, 4, 52, 4, 21, 82, 69, 36]]"
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
            "functionName": "containsDuplicate",
            "location": 1,
            "mem": {
                "$ret'": true,
                "nums": [
                    30,
                    14,
                    78,
                    4,
                    52,
                    4,
                    21,
                    82,
                    69,
                    36
                ],
                "$ret": "<undef>"
            },
            "isChecked": false
        }
    ]
}
```

</details>

