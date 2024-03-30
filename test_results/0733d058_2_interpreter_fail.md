# Test Report

Time: 2024-03-30 07:57:22.854169

### Base Program

```py
def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit
```

## Test Case 1

### Modified Program

```py

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[59, 71, 86, 79, 64, 47, 31, 54, 9, 34], 64, 29]"
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

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[0, 4, 96, 60, 21, 98, 51, 21, 61, 30], 94, 1]"
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

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[21, 95, 20, 33, 57, 37, 82, 51, 75, 98], 52, 68]"
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

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[11, 85, 75, 12, 29, 66, 19, 33, 95, 47], 13, 92]"
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

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[94, 83, 42, 35, 72, 70, 98, 30, 40, 83], 94, 100]"
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

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[97, 95, 55, 37, 16, 13, 3, 8, 24, 57], 37, 77]"
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

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[18, 11, 29, 90, 90, 95, 49, 87, 26, 47], 82, 93]"
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

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[18, 98, 88, 59, 39, 5, 47, 24, 50, 70], 100, 38]"
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

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[76, 83, 68, 12, 18, 23, 75, 62, 98, 64], 41, 3]"
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

def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"minElements\": {\"name\": \"minElements\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}, {\"val0\": \"limit\", \"val1\": \"*\", \"valueArray\": [\"limit\", \"*\"], \"valueList\": [\"limit\", \"*\"]}, {\"val0\": \"goal\", \"val1\": \"*\", \"valueArray\": [\"goal\", \"*\"], \"valueList\": [\"goal\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"sum_nums\", \"val1\": {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"sum_nums\", {\"name\": \"sum\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"diff\", {\"name\": \"abs\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"goal\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"sum_nums\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"Sub\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"diff\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"limit\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'minElements'\"}, \"types\": {\"diff\": \"*\", \"sum_nums\": \"*\"}}}}",
    "function": "minElements",
    "inputs": "[]",
    "args": "[[73, 22, 48, 15, 6, 50, 88, 23, 59, 16], 77, 97]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

