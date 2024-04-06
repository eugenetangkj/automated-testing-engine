# Issue 12: Counting Items

## Description
Two different ways of counting numbers in a list that are divisible by 2 result in programs deemed to be unequivalent by the `error_localizer`, `feedback_error`, `feedback_fix` and `repair` endpoints although they return the same output and thus should be semantically equivalent.

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

### Input
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

### Output

#### Error Localizer
```json
{
    "errorLocations": {
        "main": [
            [
                [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "filtered_list",
                            "primed": false,
                            "line": 7
                        },
                        {
                            "tokentype": "Variable",
                            "name": "filtered_list",
                            "primed": false,
                            "line": 9
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "number",
                            "primed": false,
                            "line": 5
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": false,
                            "line": 5
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "ind#0",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "i",
                            "primed": false,
                            "line": 5
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "iter#0",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        }
                    ]
                ],
                [
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    },
                    {
                        "errorType": "VariableValueMismatch",
                        "locationInReference": 1,
                        "locationInSubmission": 1,
                        "erroneousVariablesInSubmission": [
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            },
                            {
                                "tokentype": "Variable",
                                "name": "dummy2",
                                "primed": false,
                                "line": 0
                            }
                        ]
                    }
                ]
            ]
        ]
    },
    "errorInputs": []
}
```

#### Feedback Error
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

#### Feedback Fix
```json
[
    {
        "lineNumber": 4,
        "oldExpr": "i = 0",
        "newExpr": "",
        "repairStrings": [
            "Delete i = 0;"
        ]
    },
    {
        "lineNumber": 1,
        "oldExpr": "",
        "newExpr": "dummy1 = 0",
        "repairStrings": [
            "Add dummy1 = 0;"
        ]
    },
    {
        "lineNumber": 1,
        "oldExpr": "",
        "newExpr": "dummy2 = original_list",
        "repairStrings": [
            "Add dummy2 = original_list;"
        ]
    },
    {
        "lineNumber": 5,
        "oldExpr": "(i < len(original_list);)",
        "newExpr": "(dummy1 < len(dummy2);)",
        "repairStrings": [
            "Error with loop condition",
            "Wrong loop condition. Change (i < len(original_list);) to (dummy1 < len(dummy2);)"
        ]
    },
    {
        "lineNumber": 8,
        "oldExpr": "i = (i + 1)",
        "newExpr": "i = dummy2[dummy1]",
        "repairStrings": [
            "Wrong expression. Change i = (i + 1); to i = dummy2[dummy1];"
        ]
    },
    {
        "lineNumber": 4,
        "oldExpr": "",
        "newExpr": "dummy1 = (dummy1 + 1)",
        "repairStrings": [
            "Add dummy1 = (dummy1 + 1);"
        ]
    },
    {
        "lineNumber": 6,
        "oldExpr": "",
        "newExpr": "(((i % 2) == 0)) { filtered_list.append(i); } else {  }",
        "repairStrings": [
            "You need to change the condition/body of if-conditions",
            "Remove if (((original_list[i] % 2) == 0)) { filtered_list.append(original_list[i]); } else {  }",
            "Add if (((i % 2) == 0)) { filtered_list.append(i); } else {  }"
        ]
    }
]
```

#### Repair
```json
[
    {
        "totalCost": 17.0,
        "localRepairs": [
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "filtered_list",
                            "primed": false,
                            "line": 7
                        },
                        {
                            "tokentype": "Variable",
                            "name": "filtered_list",
                            "primed": false,
                            "line": 9
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "number",
                            "primed": false,
                            "line": 5
                        },
                        {
                            "tokentype": "Variable",
                            "name": "i",
                            "primed": false,
                            "line": 5
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": true,
                            "line": 5
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "ind#0",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "iter#0",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        }
                    ]
                ],
                "cost": 2.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "i",
                        "primed": false,
                        "line": 5
                    },
                    "val1": {
                        "tokentype": "Constant",
                        "value": "0",
                        "line": 4
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "i",
                            "primed": false,
                            "line": 5
                        },
                        {
                            "tokentype": "Constant",
                            "value": "0",
                            "line": 4
                        },
                        null
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "i",
                            "primed": false,
                            "line": 5
                        },
                        {
                            "tokentype": "Constant",
                            "value": "0",
                            "line": 4
                        },
                        null
                    ]
                },
                "errorLocation": {
                    "val0": 1,
                    "val1": 1,
                    "valueArray": [
                        1,
                        1
                    ],
                    "valueList": [
                        1,
                        1
                    ]
                },
                "funcName": "main"
            },
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "filtered_list",
                            "primed": false,
                            "line": 7
                        },
                        {
                            "tokentype": "Variable",
                            "name": "filtered_list",
                            "primed": false,
                            "line": 9
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "number",
                            "primed": false,
                            "line": 5
                        },
                        {
                            "tokentype": "Variable",
                            "name": "i",
                            "primed": false,
                            "line": 5
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": true,
                            "line": 5
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "ind#0",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "iter#0",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        }
                    ]
                ],
                "cost": 2.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "dummy1",
                        "primed": false,
                        "line": 0
                    },
                    "val2": {
                        "tokentype": "Constant",
                        "value": "0",
                        "line": 4
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        },
                        null,
                        {
                            "tokentype": "Constant",
                            "value": "0",
                            "line": 4
                        }
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        },
                        null,
                        {
                            "tokentype": "Constant",
                            "value": "0",
                            "line": 4
                        }
                    ]
                },
                "errorLocation": {
                    "val0": 1,
                    "val1": 1,
                    "valueArray": [
                        1,
                        1
                    ],
                    "valueList": [
                        1,
                        1
                    ]
                },
                "funcName": "main"
            },
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "filtered_list",
                            "primed": false,
                            "line": 7
                        },
                        {
                            "tokentype": "Variable",
                            "name": "filtered_list",
                            "primed": false,
                            "line": 9
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$cond",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$out",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "number",
                            "primed": false,
                            "line": 5
                        },
                        {
                            "tokentype": "Variable",
                            "name": "i",
                            "primed": false,
                            "line": 5
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": true,
                            "line": 5
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "ind#0",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "iter#0",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
                            "primed": false,
                            "line": 0
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "$in",
                            "primed": false,
                            "line": 0
                        }
                    ]
                ],
                "cost": 13.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "dummy2",
                        "primed": false,
                        "line": 0
                    },
                    "val2": {
                        "tokentype": "Variable",
                        "name": "original_list",
                        "primed": true,
                        "line": 5
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
                            "primed": false,
                            "line": 0
                        },
                        null,
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": true,
                            "line": 5
                        }
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "dummy2",
                            "primed": false,
                            "line": 0
                        },
                        null,
                        {
                            "tokentype": "Variable",
                            "name": "original_list",
                            "primed": true,
                            "line": 5
                        }
                    ]
                },
                "errorLocation": {
                    "val0": 1,
                    "val1": 1,
                    "valueArray": [
                        1,
                        1
                    ],
                    "valueList": [
                        1,
                        1
                    ]
                },
                "funcName": "main"
            }
        ]
    }
]
```

## Related Test Reports
Refer to Test Report ID fcaa6e5a.