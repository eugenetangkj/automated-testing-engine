# Test Report

Time: 2024-03-30 07:53:47.451035

### Base Program

```py
def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])
```

## Test Case 1

### Modified Program

```py

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[71, 41, 19, 30, 57, 19, 39, 55, 16, 11]]"
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

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[66, 24, 69, 48, 44, 59, 30, 77, 82, 91]]"
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

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[99, 80, 90, 56, 24, 79, 31, 53, 76, 2]]"
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

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[62, 98, 24, 85, 64, 76, 43, 96, 21, 41]]"
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

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[49, 33, 79, 39, 84, 49, 8, 47, 9, 39]]"
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

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[39, 11, 68, 14, 93, 4, 90, 8, 40, 29]]"
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

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[78, 31, 79, 58, 82, 44, 96, 17, 62, 94]]"
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

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[66, 100, 66, 94, 68, 51, 88, 76, 1, 18]]"
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

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[42, 4, 0, 74, 56, 60, 31, 69, 65, 44]]"
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

def min_partition_difference(nums):
    n = len(nums) // 2
    nums.sort(reverse=True)
    return sum(nums[:n]) - sum(nums[n:])


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"min_partition_difference\": {\"name\": \"min_partition_difference\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"nums\", \"val1\": \"*\", \"valueArray\": [\"nums\", \"*\"], \"valueList\": [\"nums\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"n\", \"val1\": {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"n\", {\"name\": \"FloorDiv\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"nums\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"nums\", {\"name\": \"sort\", \"args\": [{\"name\": \"nums\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"True\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$ret\", {\"name\": \"Sub\", \"args\": [{\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"sum\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"nums\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"Slice\", \"args\": [{\"name\": \"n\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}, {\"value\": \"None\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'min_partition_difference'\"}, \"types\": {\"n\": \"*\"}}}}",
    "function": "min_partition_difference",
    "inputs": "[]",
    "args": "[[57, 42, 84, 87, 85, 53, 25, 54, 5, 34]]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

