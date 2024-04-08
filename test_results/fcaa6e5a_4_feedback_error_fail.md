# Test Report

Time: 2024-04-06 15:51:22.700949

### Base Program

```py
def main():
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	for number in original_list:
		if number % 2 == 0:
			filtered_list.append(number)
	return filtered_list
```

## Test Case 1

### Modified Program

```py
def main():
	original_list = [1, 2, 3, 4, 5]
	filtered_list = []
	i = 0
	while i < len(original_list):
		if original_list[i] % 2 == 0:
			filtered_list.append(original_list[i])
		i = i + 1
	return filtered_list
```

<details>
<summary>feedback_error endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"iter#0\", \"val1\": {\"name\": \"original_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}], \"valueList\": [\"iter#0\", {\"name\": \"original_list\", \"primed\": true, \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"ind#0\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}], \"line\": 4}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 7}]}], \"4\": [{\"val0\": \"number\", \"val1\": {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}], \"valueList\": [\"number\", {\"name\": \"GetElement\", \"args\": [{\"name\": \"iter#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}], \"line\": 4}]}, {\"val0\": \"ind#0\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, \"valueArray\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}], \"valueList\": [\"ind#0\", {\"name\": \"Add\", \"args\": [{\"name\": \"ind#0\", \"primed\": false, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"number\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"number\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 5}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'for' loop at line 4\", \"3\": \"*after* the 'for' loop starting at line 4\", \"4\": \"inside the body of the 'for' loop beginning at line 5\"}, \"types\": {\"original_list\": \"*\", \"number\": \"*\", \"filtered_list\": \"*\", \"ind#0\": \"int\", \"iter#0\": \"int\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"original_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"original_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}], \"valueList\": [\"filtered_list\", {\"name\": \"ListInit\", \"args\": [], \"line\": 3}]}, {\"val0\": \"i\", \"val1\": {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}, \"valueArray\": [\"i\", {\"value\": \"0\", \"line\": 4}], \"valueList\": [\"i\", {\"value\": \"0\", \"line\": 4}]}], \"2\": [{\"val0\": \"$cond\", \"val1\": {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"original_list\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"original_list\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}], \"valueList\": [\"$cond\", {\"name\": \"Lt\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}, {\"name\": \"len\", \"args\": [{\"name\": \"original_list\", \"primed\": false, \"line\": 5, \"tokentype\": \"Variable\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5}]}], \"3\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"filtered_list\", \"primed\": false, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"filtered_list\", \"primed\": false, \"line\": 9}]}], \"4\": [{\"val0\": \"filtered_list\", \"val1\": {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, \"valueArray\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 6}], \"valueList\": [\"filtered_list\", {\"name\": \"ite\", \"args\": [{\"name\": \"Eq\", \"args\": [{\"name\": \"Mod\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 6, \"tokentype\": \"Variable\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"value\": \"0\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"append\", \"args\": [{\"name\": \"filtered_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"original_list\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}, {\"name\": \"i\", \"primed\": false, \"line\": 7, \"tokentype\": \"Variable\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"filtered_list\", \"primed\": false, \"line\": 0, \"tokentype\": \"Variable\"}], \"line\": 6}]}, {\"val0\": \"i\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"i\", {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}], \"valueList\": [\"i\", {\"name\": \"Add\", \"args\": [{\"name\": \"i\", \"primed\": false, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8}]}]}, \"loctrans\": {\"1\": {\"true\": 2}, \"2\": {\"false\": 3, \"true\": 4}, \"3\": {}, \"4\": {\"true\": 2}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\", \"2\": \"the condition of the 'while' loop at line 5\", \"3\": \"*after* the 'while' loop starting at line 5\", \"4\": \"inside the body of the 'while' loop beginning at line 6\"}, \"types\": {\"original_list\": \"*\", \"filtered_list\": \"*\", \"i\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

Message: 
```
Feedback error endpoint failed
```

Actual Output: 
```json
[
    {
        "lineNumber": 4,
        "hintStrings": [
            "Incorrect/Unnecessary expression assigned to variable: *i*"
        ]
    },
    {
        "lineNumber": 1,
        "hintStrings": [
            "You need to assign a suitable value to variable: *dummy1*"
        ]
    },
    {
        "lineNumber": 1,
        "hintStrings": [
            "You need to assign a suitable value to variable: *dummy2*"
        ]
    },
    {
        "lineNumber": 5,
        "hintStrings": [
            "Wrong loop condition: (i < len(original_list);)"
        ]
    },
    {
        "lineNumber": 8,
        "hintStrings": [
            "Wrong expression for variable: *i*"
        ]
    },
    {
        "lineNumber": 4,
        "hintStrings": [
            "You need to assign a suitable value to variable: *dummy1*"
        ]
    },
    {
        "lineNumber": 6,
        "hintStrings": [
            "Unnecessary/Incorrect if (((original_list[i] % 2) == 0)) { filtered_list.append(original_list[i]); } else {  }",
            "Consider conditions if (((i % 2) == 0))"
        ]
    }
]
```

</details>

