# Issue 25: Try-Except Equivalent Programs

## Description
We can wrap a program that does not throw an exception in a try-except block. Then, the program is equivalent to not having the try-except block. However, the `errorlocalizer`, `feedback_error`, `feedback_fix` and `repair` endpoints do not detect this, and deem such programs to be unequivalent.

### Base Program

```py
def main():
	return 1
```

### Modified Program
```py
def main():
	try:
		return 1
	except:
		return 0
```


### Input
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"1\", \"line\": 2}], \"valueList\": [\"$ret\", {\"value\": \"1\", \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"value\": \"0\", \"line\": 5, \"tokentype\": \"Constant\"}, \"valueArray\": [\"$ret\", {\"value\": \"0\", \"line\": 5}], \"valueList\": [\"$ret\", {\"value\": \"0\", \"line\": 5}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

### Interpreter Output
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
                                "name": "$ret",
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
                                "name": "$ret",
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
                                "name": "$ret",
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
                                "name": "$ret",
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
                                "name": "$ret",
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
                                "name": "$ret",
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
                                "name": "$ret",
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
                                "name": "$ret",
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
                                "name": "$ret",
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
                                "name": "$ret",
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

### Feedback Error Output
Notice how it suggests that the return value is incorrect.
```json
[
    {
        "lineNumber": 5,
        "hintStrings": [
            "Incorrect return value"
        ]
    }
]
```
### Feedback Fix Output
```json
[
    {
        "lineNumber": 5,
        "oldExpr": "0",
        "newExpr": "1",
        "repairStrings": [
            "Wrong assignment. Change return 0 to return 1"
        ]
    }
]
```

### Repair Output
```json
[
    {
        "totalCost": 1.0,
        "localRepairs": [
            {
                "mapping": [
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
                "cost": 1.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "$ret",
                        "primed": false,
                        "line": 0
                    },
                    "val1": {
                        "tokentype": "Constant",
                        "value": "0",
                        "line": 5
                    },
                    "val2": {
                        "tokentype": "Constant",
                        "value": "1",
                        "line": 2
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Constant",
                            "value": "0",
                            "line": 5
                        },
                        {
                            "tokentype": "Constant",
                            "value": "1",
                            "line": 2
                        }
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Constant",
                            "value": "0",
                            "line": 5
                        },
                        {
                            "tokentype": "Constant",
                            "value": "1",
                            "line": 2
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
Refer to Test Report ID 01f036ff and 7e328c1b.