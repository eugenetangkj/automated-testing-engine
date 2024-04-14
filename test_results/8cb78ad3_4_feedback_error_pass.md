# Test Report

Time: 2024-04-14 11:25:37.106747

### Base Program

```py
def multiply(x, y):
	return x * y
```

## Test Case 1

### Modified Program

```py
def multiply(x, y):
    return x * y
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"multiply\": {\"name\": \"multiply\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"multiply\": {\"name\": \"multiply\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply'\"}, \"types\": {}}}}",
    "function": "multiply",
    "inputs": "[]",
    "args": "[[62.60869730198982, 82.95548454519331], [89.73286466077337, -39.54167211659752], [26.801466292075673, 77.67476591918549], [44.4129406708206, 39.87407687563456], [26.60113616032625, -6.019801615557768], [-27.673868290536134, 16.80169877975422], [-40.249603066004845, 9.891458403268771], [-4.553067238394419, 29.987130688590952], [-74.3236782388263, 18.88315174662128], [-28.632296290247325, -35.6982006482462]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

## Test Case 2

### Modified Program

```py
def multiply(var_0, var_1):
    return var_0 * var_1
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"multiply\": {\"name\": \"multiply\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"multiply\": {\"name\": \"multiply\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_0\", \"val1\": \"*\", \"valueArray\": [\"var_0\", \"*\"], \"valueList\": [\"var_0\", \"*\"]}, {\"val0\": \"var_1\", \"val1\": \"*\", \"valueArray\": [\"var_1\", \"*\"], \"valueList\": [\"var_1\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"var_0\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_1\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply'\"}, \"types\": {}}}}",
    "function": "multiply",
    "inputs": "[]",
    "args": "[[62.60869730198982, 82.95548454519331], [89.73286466077337, -39.54167211659752], [26.801466292075673, 77.67476591918549], [44.4129406708206, 39.87407687563456], [26.60113616032625, -6.019801615557768], [-27.673868290536134, 16.80169877975422], [-40.249603066004845, 9.891458403268771], [-4.553067238394419, 29.987130688590952], [-74.3236782388263, 18.88315174662128], [-28.632296290247325, -35.6982006482462]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

## Test Case 3

### Modified Program

```py
def multiply(x, y):
    return y * x
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"multiply\": {\"name\": \"multiply\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"multiply\": {\"name\": \"multiply\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply'\"}, \"types\": {}}}}",
    "function": "multiply",
    "inputs": "[]",
    "args": "[[62.60869730198982, 82.95548454519331], [89.73286466077337, -39.54167211659752], [26.801466292075673, 77.67476591918549], [44.4129406708206, 39.87407687563456], [26.60113616032625, -6.019801615557768], [-27.673868290536134, 16.80169877975422], [-40.249603066004845, 9.891458403268771], [-4.553067238394419, 29.987130688590952], [-74.3236782388263, 18.88315174662128], [-28.632296290247325, -35.6982006482462]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

## Test Case 4

### Modified Program

```py
def multiply(var_2, var_3):
    return var_3 * var_2
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"multiply\": {\"name\": \"multiply\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"x\", \"val1\": \"*\", \"valueArray\": [\"x\", \"*\"], \"valueList\": [\"x\", \"*\"]}, {\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"x\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"multiply\": {\"name\": \"multiply\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_2\", \"val1\": \"*\", \"valueArray\": [\"var_2\", \"*\"], \"valueList\": [\"var_2\", \"*\"]}, {\"val0\": \"var_3\", \"val1\": \"*\", \"valueArray\": [\"var_3\", \"*\"], \"valueList\": [\"var_3\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Mult\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'multiply'\"}, \"types\": {}}}}",
    "function": "multiply",
    "inputs": "[]",
    "args": "[[62.60869730198982, 82.95548454519331], [89.73286466077337, -39.54167211659752], [26.801466292075673, 77.67476591918549], [44.4129406708206, 39.87407687563456], [26.60113616032625, -6.019801615557768], [-27.673868290536134, 16.80169877975422], [-40.249603066004845, 9.891458403268771], [-4.553067238394419, 29.987130688590952], [-74.3236782388263, 18.88315174662128], [-28.632296290247325, -35.6982006482462]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

