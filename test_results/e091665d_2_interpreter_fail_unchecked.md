# Test Report

Time: 2024-03-30 08:32:01.272330

### Base Program

```py
from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1
```

## Test Case 1

### Modified Program

```py

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[55, 58, 13, 6, 29, 17, 38, 59, 87, 38], 54]"
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

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[74, 58, 39, 49, 48, 4, 80, 38, 33, 54], 24]"
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

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[59, 17, 74, 98, 63, 93, 22, 37, 6, 85], 8]"
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

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[80, 78, 27, 58, 13, 56, 26, 92, 12, 40], 21]"
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

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[100, 71, 0, 27, 3, 37, 66, 68, 71, 89], 33]"
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

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[3, 76, 83, 12, 17, 62, 13, 41, 87, 38], 16]"
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

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[8, 28, 75, 53, 32, 2, 80, 22, 94, 29], 100]"
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

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[16, 66, 68, 43, 43, 28, 90, 53, 63, 46], 93]"
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

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[17, 78, 8, 67, 7, 83, 45, 35, 64, 97], 13]"
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

from collections import Counter
import heapq

def findLeastNumOfUniqueInts(arr, k):
    count = Counter(arr)
    pq = list(count.values())
    heapq.heapify(pq)
    while k > 0:
        k -= heapq.heappop(pq)
    return len(pq) if k == 0 else len(pq) + 1


```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [\"from collections import Counter\", \"import heapq\"], \"fncs\": {\"findLeastNumOfUniqueInts\": {\"name\": \"findLeastNumOfUniqueInts\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"arr\", \"val1\": \"*\", \"valueArray\": [\"arr\", \"*\"], \"valueList\": [\"arr\", \"*\"]}, {\"val0\": \"k\", \"val1\": \"*\", \"valueArray\": [\"k\", \"*\"], \"valueList\": [\"k\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"count\", \"val1\": {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"count\", {\"name\": \"FuncCall\", \"args\": [{\"value\": \"Counter\", \"line\": 6, \"tokentype\": \"Constant\"}, {\"name\": \"arr\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"pq\", \"val1\": {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, \"valueArray\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}], \"valueList\": [\"pq\", {\"name\": \"list\", \"args\": [{\"name\": \"values\", \"args\": [{\"name\": \"count\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 9, \"tokentype\": \"Constant\"}], \"line\": 9}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}], \"valueList\": [\"$ret\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"len\", \"args\": [{\"name\": \"pq\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"value\": \"1\", \"line\": 11, \"tokentype\": \"Constant\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11}]}], \"4\": [{\"val0\": \"k\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}], \"valueList\": [\"k\", {\"name\": \"Sub\", \"args\": [{\"name\": \"k\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"FuncCall\", \"args\": [{\"value\": \"heappop\", \"line\": 10, \"tokentype\": \"Constant\"}, {\"name\": \"heapq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"name\": \"pq\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}], \"line\": 10, \"tokentype\": \"Operation\"}], \"line\": 10}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'findLeastNumOfUniqueInts'\", \"2\": \"the condition of the 'while' loop at line 9\", \"3\": \"*after* the 'while' loop starting at line 9\", \"4\": \"inside the body of the 'while' loop beginning at line 10\"}, \"types\": {\"pq\": \"*\", \"count\": \"*\", \"k\": \"*\"}}}}",
    "function": "findLeastNumOfUniqueInts",
    "inputs": "[]",
    "args": "[[15, 8, 12, 29, 99, 26, 35, 88, 72, 82], 75]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

