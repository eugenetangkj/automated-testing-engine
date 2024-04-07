# Issue 16: Handling Extra Variables with the Error Localizer

## Description
There appears to be an inconsistency regarding how the error localizer handles the introduction of extra variables while preserving program semantics.

### Program 1
Consider the following program. Related report ID is 1377d379.

```py
base_program_string = "def main(y):\n\ty = y + 5\n\treturn y"
modified_program_string = "def main(y):\n\ty = y + 5\n\tx = y\n\treturn x"
function_name = "main"
function_arguments = "[[90], [68], [1], [95], [50], [5], [17], [77], [99], [12]]"
```

When we use Program 1, the `error_localizer` endpoint identified multiple error locations, while the `feedback_fix`, `feedback_error` and `repair` endpoints do not detect any differences between the base and modified programs (i.e. Repair cost is 0).

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"y\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Add\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"y\", {\"name\": \"Add\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"y\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"y\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"y\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"y\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"y\", \"val1\": \"*\", \"valueArray\": [\"y\", \"*\"], \"valueList\": [\"y\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"y\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"y\", {\"name\": \"Add\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"y\", {\"name\": \"Add\", \"args\": [{\"name\": \"y\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"x\", \"val1\": {\"name\": \"y\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"x\", {\"name\": \"y\", \"primed\": true, \"line\": 3}], \"valueList\": [\"x\", {\"name\": \"y\", \"primed\": true, \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\", \"y\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[90], [68], [1], [95], [50], [5], [17], [77], [99], [12]]"
}
```

Actual Output: 
```json
{
    "errorLocations": {
        "main": [
            [
                [
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
                            "name": "dummy1",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "y",
                            "primed": false,
                            "line": 2
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
                            "name": "y",
                            "primed": false,
                            "line": 2
                        },
                        {
                            "tokentype": "Variable",
                            "name": "x",
                            "primed": false,
                            "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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
                                "name": "x",
                                "primed": false,
                                "line": 4
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

### Program 2
We thought what was observed in Program 1 could be because the introduction of a new variable leads to the error localizer detecting a potential error location. Thus, we tried the following program and discovered that the error localizer did not identify any error locations. Related report ID is 8744d29e.

```py
base_program_string = "def main(v):\n\tv = v + 5\n\treturn v"
modified_program_string = "def main(v):\n\tv = v + 5\n\tv = v\n\treturn v"
function_name = "main"
function_arguments = "[[30], [26], [63], [59], [53], [68], [62], [52], [66], [59]]"
```
Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"v\", \"val1\": \"*\", \"valueArray\": [\"v\", \"*\"], \"valueList\": [\"v\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"v\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"v\", {\"name\": \"Add\", \"args\": [{\"name\": \"v\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"v\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"v\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"v\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[30], [26], [63], [59], [53], [68], [62], [52], [66], [59]]"
}
```
Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

### Program 3
However, when we tried another program that involves introduction of a new variable, the error localizer endpoint did not detect any possible error locations. Related report ID is d33344d6.

```py
base_program_string = "def main():\n\treturn 2"
modified_program_string = "def main():\n\tx = 2\n\treturn x"
function_name = "main"
function_arguments = "[[], [], [], [], [], [], [], [], [], []]"
```

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"$ret\", {\"value\": \"2\", \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"x\", \"val1\": {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"x\", {\"value\": \"2\", \"line\": 2}], \"valueList\": [\"x\", {\"value\": \"2\", \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"x\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"x\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"x\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

Actual Output: 
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

### Conclusion
The above 3 programs thus leads to the question of why only Program 1 leads to the error_localizer detecting error locations. From the examples, we have seen that it is not because of the introduction of a new variable, and in all 3 examples, the base and modified programs have equivalent semantics.

This hints towards a potential inconsistency within the error localizer component.
