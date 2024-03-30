# Test Report

Time: 2024-03-30 08:22:38.617898

### Base Program

```py
def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))
```

## Test Case 1

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[47, 46, 91, 72, 72, 91, 36, 68, 89, 91], 34]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[71, 96, 82, 14, 22, 12, 22, 86, 92, 44], 94]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[9, 54, 0, 74, 51, 64, 14, 46, 4, 75], 52]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[50, 48, 46, 94, 73, 94, 41, 81, 36, 100], 64]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 5

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[86, 84, 90, 29, 59, 3, 71, 48, 47, 35], 79]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 6

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[56, 17, 42, 94, 72, 21, 52, 82, 8, 5], 20]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 7

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[68, 8, 85, 18, 31, 93, 48, 95, 97, 94], 36]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 8

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[63, 85, 75, 71, 0, 22, 2, 46, 79, 79], 24]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 9

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[16, 35, 32, 22, 14, 33, 74, 0, 7, 61], 14]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

## Test Case 10

### Modified Program

```py

def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_append_k_sum\": {\"name\": \"min_append_k_sum\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"max_elem\", \"val1\": {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"max_elem\", {\"name\": \"max\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"args\": [{\"name\": \"range\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"max_elem\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"k\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_append_k_sum'\"}, \"types\": {\"max_elem\": \"*\"}}}}",
    "function": "min_append_k_sum",
    "inputs": "[]",
    "args": "[[89, 67, 4, 92, 100, 70, 94, 32, 33, 47], 11]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

