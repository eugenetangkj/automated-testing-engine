# Test Report

Time: 2024-03-30 06:30:21.748007

### Base Program

```py
def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt
```

## Test Case 1

### Modified Program

```py

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[19, 86, 70, 6, 27, 87, 40, 80, 21, 35], [47, 88, 24, 72, 18, 23, 83, 60, 82, 38], 99, 75]"
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

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[55, 27, 77, 97, 2, 17, 62, 39, 9, 55], [65, 18, 88, 81, 70, 74, 37, 21, 76, 89], 18, 81]"
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

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[77, 18, 11, 72, 54, 75, 18, 32, 65, 24], [55, 58, 33, 91, 83, 17, 49, 52, 51, 24], 56, 79]"
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

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[4, 46, 71, 56, 39, 15, 68, 6, 3, 13], [18, 80, 84, 81, 35, 84, 68, 42, 42, 14], 52, 6]"
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

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[50, 95, 50, 31, 0, 22, 17, 74, 34, 91], [63, 62, 12, 11, 50, 23, 42, 62, 34, 20], 44, 47]"
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

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[2, 16, 82, 61, 36, 30, 8, 96, 90, 75], [20, 25, 93, 33, 52, 58, 61, 54, 24, 84], 33, 80]"
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

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[91, 62, 92, 21, 0, 27, 2, 36, 65, 31], [85, 73, 78, 61, 49, 87, 14, 53, 51, 91], 7, 99]"
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
            "functionName": "maxTasks",
            "location": 1,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": "<undef>",
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": "<undef>",
                "cnt'": 0,
                "ind#0'": 0,
                "ind#0": "<undef>",
                "iter#0": "<undef>",
                "workers": [
                    85,
                    73,
                    78,
                    61,
                    49,
                    87,
                    14,
                    53,
                    51,
                    91
                ],
                "tasks": [
                    91,
                    62,
                    92,
                    21,
                    0,
                    27,
                    2,
                    36,
                    65,
                    31
                ],
                "i'": 0
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 2,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 0,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 0,
                "$cond": "<undef>",
                "cnt'": 0,
                "ind#0'": 0,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 0,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 4,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 0,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 0,
                "j": "<undef>",
                "$cond": true,
                "cnt'": 0,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 0,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "j'": 0,
                "i'": 0,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 5,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 0,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 0,
                "j": 0,
                "$cond": true,
                "cnt'": 0,
                "ind#0'": 1,
                "$cond'": false,
                "ind#0": 1,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 0,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 0,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 6,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 0,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 0,
                "j": 0,
                "$cond": false,
                "cnt'": 1,
                "ind#0'": 1,
                "$cond'": false,
                "ind#0": 1,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 0,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 1,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 2,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 1,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 1,
                "j": 0,
                "$cond": false,
                "cnt'": 1,
                "ind#0'": 1,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 0,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 1,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 4,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 1,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 1,
                "j": 0,
                "$cond": true,
                "cnt'": 1,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 1,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 1,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 1,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 5,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 1,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 1,
                "j": 1,
                "$cond": true,
                "cnt'": 1,
                "ind#0'": 2,
                "$cond'": false,
                "ind#0": 2,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 1,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 1,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 6,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 1,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 1,
                "j": 1,
                "$cond": false,
                "cnt'": 2,
                "ind#0'": 2,
                "$cond'": false,
                "ind#0": 2,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 1,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 2,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 2,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 2,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 2,
                "j": 1,
                "$cond": false,
                "cnt'": 2,
                "ind#0'": 2,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 1,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 2,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 4,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 2,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 2,
                "j": 1,
                "$cond": true,
                "cnt'": 2,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 2,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 2,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 2,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 5,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 2,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 2,
                "j": 2,
                "$cond": true,
                "cnt'": 2,
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 2,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 2,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 6,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 2,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 2,
                "j": 2,
                "$cond": false,
                "cnt'": 3,
                "ind#0'": 3,
                "$cond'": false,
                "ind#0": 3,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 2,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 3,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 2,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 3,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 3,
                "j": 2,
                "$cond": false,
                "cnt'": 3,
                "ind#0'": 3,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 2,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 3,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 4,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 3,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 3,
                "j": 2,
                "$cond": true,
                "cnt'": 3,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 3,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 3,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 3,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 5,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 3,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 3,
                "j": 3,
                "$cond": true,
                "cnt'": 3,
                "ind#0'": 4,
                "$cond'": false,
                "ind#0": 4,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 3,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 3,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 6,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 3,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 3,
                "j": 3,
                "$cond": false,
                "cnt'": 4,
                "ind#0'": 4,
                "$cond'": false,
                "ind#0": 4,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 3,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 4,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 2,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 4,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 4,
                "j": 3,
                "$cond": false,
                "cnt'": 4,
                "ind#0'": 4,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 3,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 4,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 4,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 4,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 4,
                "j": 3,
                "$cond": true,
                "cnt'": 4,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 4,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 4,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 4,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 5,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 4,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 4,
                "j": 4,
                "$cond": true,
                "cnt'": 4,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 4,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 4,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 6,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 4,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 4,
                "j": 4,
                "$cond": false,
                "cnt'": 5,
                "ind#0'": 5,
                "$cond'": false,
                "ind#0": 5,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 4,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 5,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 2,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 5,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 5,
                "j": 4,
                "$cond": false,
                "cnt'": 5,
                "ind#0'": 5,
                "$cond'": true,
                "ind#0": 5,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 4,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 5,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 4,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 5,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 5,
                "j": 4,
                "$cond": true,
                "cnt'": 5,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 5,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 5,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 5,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 5,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 5,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 5,
                "j": 5,
                "$cond": true,
                "cnt'": 5,
                "ind#0'": 6,
                "$cond'": false,
                "ind#0": 6,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 5,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 5,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 6,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 5,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 5,
                "j": 5,
                "$cond": false,
                "cnt'": 6,
                "ind#0'": 6,
                "$cond'": false,
                "ind#0": 6,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 5,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 6,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 2,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 6,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 6,
                "j": 5,
                "$cond": false,
                "cnt'": 6,
                "ind#0'": 6,
                "$cond'": true,
                "ind#0": 6,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 5,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 6,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 4,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 6,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 6,
                "j": 5,
                "$cond": true,
                "cnt'": 6,
                "ind#0'": 7,
                "$cond'": true,
                "ind#0": 6,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 6,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 6,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 5,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 6,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 6,
                "j": 6,
                "$cond": true,
                "cnt'": 6,
                "ind#0'": 7,
                "$cond'": false,
                "ind#0": 7,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 6,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 6,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 6,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 6,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 6,
                "j": 6,
                "$cond": false,
                "cnt'": 7,
                "ind#0'": 7,
                "$cond'": false,
                "ind#0": 7,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 6,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 7,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 2,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 7,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 7,
                "j": 6,
                "$cond": false,
                "cnt'": 7,
                "ind#0'": 7,
                "$cond'": false,
                "ind#0": 7,
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 6,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 7,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 3,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#1'": [
                    7,
                    8,
                    9
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 7,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 7,
                "j": 6,
                "$cond": false,
                "cnt'": 7,
                "ind#1'": 0,
                "ind#0'": 7,
                "$cond'": false,
                "ind#1": "<undef>",
                "ind#0": 7,
                "iter#1": "<undef>",
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 6,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 0,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 11,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#1'": [
                    7,
                    8,
                    9
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 7,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 0,
                "j": 6,
                "$cond": false,
                "cnt'": 7,
                "ind#1'": 0,
                "ind#0'": 7,
                "$cond'": true,
                "ind#1": 0,
                "ind#0": 7,
                "iter#1": [
                    7,
                    8,
                    9
                ],
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 6,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 0,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 13,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#1'": [
                    7,
                    8,
                    9
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 7,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 0,
                "j": 6,
                "$cond": true,
                "cnt'": 8,
                "ind#1'": 1,
                "ind#0'": 7,
                "$cond'": true,
                "ind#1": 0,
                "ind#0": 7,
                "iter#1": [
                    7,
                    8,
                    9
                ],
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 7,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 1,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 11,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#1'": [
                    7,
                    8,
                    9
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 8,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 1,
                "j": 7,
                "$cond": true,
                "cnt'": 8,
                "ind#1'": 1,
                "ind#0'": 7,
                "$cond'": true,
                "ind#1": 1,
                "ind#0": 7,
                "iter#1": [
                    7,
                    8,
                    9
                ],
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 7,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 1,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 13,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#1'": [
                    7,
                    8,
                    9
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 8,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 1,
                "j": 7,
                "$cond": true,
                "cnt'": 9,
                "ind#1'": 2,
                "ind#0'": 7,
                "$cond'": true,
                "ind#1": 1,
                "ind#0": 7,
                "iter#1": [
                    7,
                    8,
                    9
                ],
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 8,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 2,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 11,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#1'": [
                    7,
                    8,
                    9
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 9,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 2,
                "j": 8,
                "$cond": true,
                "cnt'": 9,
                "ind#1'": 2,
                "ind#0'": 7,
                "$cond'": true,
                "ind#1": 2,
                "ind#0": 7,
                "iter#1": [
                    7,
                    8,
                    9
                ],
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 8,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 2,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 13,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#1'": [
                    7,
                    8,
                    9
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 9,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 2,
                "j": 8,
                "$cond": true,
                "cnt'": 10,
                "ind#1'": 3,
                "ind#0'": 7,
                "$cond'": true,
                "ind#1": 2,
                "ind#0": 7,
                "iter#1": [
                    7,
                    8,
                    9
                ],
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 9,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 3,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 11,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#1'": [
                    7,
                    8,
                    9
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 10,
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i": 3,
                "j": 9,
                "$cond": true,
                "cnt'": 10,
                "ind#1'": 3,
                "ind#0'": 7,
                "$cond'": false,
                "ind#1": 3,
                "ind#0": 7,
                "iter#1": [
                    7,
                    8,
                    9
                ],
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "j'": 9,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 3,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ]
            },
            "isChecked": false
        },
        {
            "functionName": "maxTasks",
            "location": 12,
            "mem": {
                "pills": 7,
                "strength": 99,
                "iter#1'": [
                    7,
                    8,
                    9
                ],
                "workers'": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "ind#1'": 3,
                "workers": [
                    14,
                    49,
                    51,
                    53,
                    61,
                    73,
                    78,
                    85,
                    87,
                    91
                ],
                "i'": 3,
                "tasks": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "iter#0'": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "tasks'": [
                    0,
                    2,
                    21,
                    27,
                    31,
                    36,
                    62,
                    65,
                    91,
                    92
                ],
                "cnt": 10,
                "i": 3,
                "j": 9,
                "$cond": false,
                "$ret": "<undef>",
                "cnt'": 10,
                "ind#0'": 7,
                "$cond'": false,
                "ind#1": 3,
                "ind#0": 7,
                "iter#1": [
                    7,
                    8,
                    9
                ],
                "iter#0": [
                    0,
                    1,
                    2,
                    3,
                    4,
                    5,
                    6
                ],
                "$ret'": 10,
                "j'": 9
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

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[44, 39, 82, 49, 50, 30, 26, 88, 74, 90], [8, 86, 33, 74, 60, 29, 72, 19, 50, 71], 71, 27]"
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

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[28, 49, 48, 10, 7, 60, 51, 9, 15, 33], [64, 81, 7, 20, 3, 99, 21, 37, 69, 54], 45, 80]"
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

def maxTasks(tasks, workers, pills, strength):
  tasks.sort()
  workers.sort()

  cnt = 0
  i = 0
  for j in range(pills):
    while i < len(tasks) and tasks[i] > workers[j] + strength:
      i += 1
    if i < len(tasks):
      cnt += 1
      i += 1

  i = 0
  for j in range(pills, len(workers)):
    if i < len(tasks) and tasks[i] <= workers[j]:
      cnt += 1
      i += 1
      
  return cnt



```

<details>
<summary>interpreter endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "program_model": "{\"importStatements\": [], \"fncs\": {\"maxTasks\": {\"name\": \"maxTasks\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"tasks\", \"val1\": \"*\", \"valueArray\": [\"tasks\", \"*\"], \"valueList\": [\"tasks\", \"*\"]}, {\"val0\": \"workers\", \"val1\": \"*\", \"valueArray\": [\"workers\", \"*\"], \"valueList\": [\"workers\", \"*\"]}, {\"val0\": \"pills\", \"val1\": \"*\", \"valueArray\": [\"pills\", \"*\"], \"valueList\": [\"pills\", \"*\"]}, {\"val0\": \"strength\", \"val1\": \"*\", \"valueArray\": [\"strength\", \"*\"], \"valueList\": [\"strength\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"tasks\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"tasks\", {\"name\": \"sort\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"workers\", \"val1\": {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"workers\", {\"name\": \"sort\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"cnt\", \"val1\": {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}, \"valueArray\": [\"cnt\", {\"value\": \"0\", \"line\": 6}], \"valueList\": [\"cnt\", {\"value\": \"0\", \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 7, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 7}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 7}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"iter#0\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 8, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 8}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}], \"3\": [{\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 15, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 15}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 15}]}, {\"val0\": \"iter#1\", \"val1\": {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"iter#1\", {\"name\": \"range\", \"args\": [{\"name\": \"pills\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"value\": \"0\", \"line\": 16, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}], \"valueList\": [\"ind#1\", {\"value\": \"0\", \"line\": 16}]}], \"4\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}], \"line\": 8}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}], \"5\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}], \"valueList\": [\"$cond\", {\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Gt\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}, {\"name\": \"strength\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9, \"tokentype\": \"Operation\"}], \"line\": 9}]}], \"6\": [{\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 12, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 12, \"tokentype\": \"Constant\"}], \"line\": 12, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 11, \"tokentype\": \"Variable\"}], \"line\": 11, \"tokentype\": \"Operation\"}], \"line\": 11, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 13, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 13, \"tokentype\": \"Constant\"}], \"line\": 13, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 11}]}], \"7\": [{\"val0\": \"i\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}], \"valueList\": [\"i\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 10, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 10, \"tokentype\": \"Constant\"}], \"line\": 10}]}], \"11\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}], \"line\": 16}]}], \"12\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"cnt\", \"primed\": false, \"line\": 21, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}], \"valueList\": [\"$ret\", {\"name\": \"cnt\", \"primed\": false, \"line\": 21}]}], \"13\": [{\"val0\": \"j\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}], \"valueList\": [\"j\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}], \"line\": 16}]}, {\"val0\": \"ind#1\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}], \"valueList\": [\"ind#1\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#1\", \"primed\": false, \"line\": 16, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 16, \"tokentype\": \"Constant\"}], \"line\": 16}]}, {\"val0\": \"cnt\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"cnt\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"cnt\", \"primed\": false, \"line\": 18, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 18, \"tokentype\": \"Constant\"}], \"line\": 18, \"tokentype\": \"Operation\"}, {\"name\": \"cnt\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}], \"valueList\": [\"i\", {\"name\": \"ite\", \"args\": [{\"name\": \"And\", \"args\": [{\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"LtE\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"tasks\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"workers\", \"primed\": false, \"line\": 17, \"tokentype\": \"Variable\"}, {\"name\": \"j\", \"primed\": true, \"line\": 17, \"tokentype\": \"Variable\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}], \"line\": 17, \"tokentype\": \"Operation\"}, {\"name\": \"AssAdd\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 19, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 19, \"tokentype\": \"Constant\"}], \"line\": 19, \"tokentype\": \"Operation\"}, {\"name\": \"i\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 17}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {\"true\": 11}, \"4\": {\"true\": 5}, \"5\": {\"false\": 6, \"true\": 7}, \"6\": {\"true\": 2}, \"7\": {\"true\": 5}, \"11\": {\"false\": 12, \"true\": 13}, \"12\": {}, \"13\": {\"true\": 11}}, \"locdescs\": {\"1\": \"around the beginning of function 'maxTasks'\", \"2\": \"the condition of the 'for' loop at line 8\", \"3\": \"*after* the 'for' loop starting at line 8\", \"4\": \"inside the body of the 'for' loop beginning at line 9\", \"5\": \"the condition of the 'while' loop at line 9\", \"6\": \"*after* the 'while' loop starting at line 9\", \"7\": \"inside the body of the 'while' loop beginning at line 10\", \"11\": \"the condition of the 'for' loop at line 16\", \"12\": \"*after* the 'for' loop starting at line 16\", \"13\": \"inside the body of the 'for' loop beginning at line 17\"}, \"types\": {\"ind#1\": \"int\", \"ind#0\": \"int\", \"cnt\": \"*\", \"i\": \"*\", \"iter#1\": \"int\", \"iter#0\": \"int\", \"j\": \"*\"}}}}",
    "function": "maxTasks",
    "inputs": "[]",
    "args": "[[0, 94, 25, 79, 3, 25, 61, 19, 23, 22], [52, 60, 5, 20, 71, 9, 21, 45, 73, 60], 75, 96]"
}
```

Message: 
```
No entries in result
```

Actual Output: None

</details>

