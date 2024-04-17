# Test Report

Time: 2024-04-16 12:24 AM

### Base Program

```py
def find_power(base, exponent):
	result = 1
	while exponent > 0:
		result *= base
		exponent -= 1
	return result
```

## Test Case 1

### Modified Program

```py
# Mutated by: 
def find_power(base, exponent):
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[[39, 1], [62, 75], [75, 84], [93, 74], [62, 84], [11, 20], [85, 50], [69, 97], [8, 94], [43, 89]]"
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
# Mutated by: VariableRenamerModifier
def find_power(var_0, var_1):
    result = 1
    while var_1 > 0:
        result *= var_0
        var_1 -= 1
    return result
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_0\", \"val1\": \"*\", \"valueArray\": [\"var_0\", \"*\"], \"valueList\": [\"var_0\", \"*\"]}, {\"val0\": \"var_1\", \"val1\": \"*\", \"valueArray\": [\"var_1\", \"*\"], \"valueList\": [\"var_1\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_0\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"var_1\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"var_1\", {\"name\": \"Sub\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"var_1\", {\"name\": \"Sub\", \"args\": [{\"name\": \"var_1\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"var_1\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[[39, 1], [62, 75], [75, 84], [93, 74], [62, 84], [11, 20], [85, 50], [69, 97], [8, 94], [43, 89]]"
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
# Mutated by: BinOpModifier
def find_power(base, exponent):
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[[39, 1], [62, 75], [75, 84], [93, 74], [62, 84], [11, 20], [85, 50], [69, 97], [8, 94], [43, 89]]"
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
# Mutated by: VariableRenamerModifier, BinOpModifier
def find_power(var_2, var_3):
    result = 1
    while var_3 > 0:
        result *= var_2
        var_3 -= 1
    return result
```

<details>
<summary>feedback_error endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"base\", \"val1\": \"*\", \"valueArray\": [\"base\", \"*\"], \"valueList\": [\"base\", \"*\"]}, {\"val0\": \"exponent\", \"val1\": \"*\", \"valueArray\": [\"exponent\", \"*\"], \"valueList\": [\"exponent\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 2}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 6}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"base\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"exponent\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}], \"valueList\": [\"exponent\", {\"name\": \"Sub\", \"args\": [{\"name\": \"exponent\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 3\", \"3\": \"*after* the 'while' loop starting at line 3\", \"4\": \"inside the body of the 'while' loop beginning at line 4\"}, \"types\": {\"result\": \"*\", \"exponent\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"find_power\": {\"name\": \"find_power\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"var_2\", \"val1\": \"*\", \"valueArray\": [\"var_2\", \"*\"], \"valueList\": [\"var_2\", \"*\"]}, {\"val0\": \"var_3\", \"val1\": \"*\", \"valueArray\": [\"var_3\", \"*\"], \"valueList\": [\"var_3\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"result\", \"val1\": {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, \"valueArray\": [\"result\", {\"value\": \"1\", \"line\": 3}], \"valueList\": [\"result\", {\"value\": \"1\", \"line\": 3}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Gt\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Gt\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"result\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"result\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"result\", \"val1\": {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"result\", {\"name\": \"Mult\", \"args\": [{\"name\": \"result\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"var_2\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5}]}, {\"val0\": \"var_3\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"var_3\", {\"name\": \"Sub\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}], \"valueList\": [\"var_3\", {\"name\": \"Sub\", \"args\": [{\"name\": \"var_3\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'find_power'\", \"2\": \"the condition of the 'while' loop at line 4\", \"3\": \"*after* the 'while' loop starting at line 4\", \"4\": \"inside the body of the 'while' loop beginning at line 5\"}, \"types\": {\"result\": \"*\", \"var_3\": \"*\"}}}}",
    "function": "find_power",
    "inputs": "[]",
    "args": "[[39, 1], [62, 75], [75, 84], [93, 74], [62, 84], [11, 20], [85, 50], [69, 97], [8, 94], [43, 89]]"
}
```

Message: 
```
Success
```

Actual Output: None

</details>

