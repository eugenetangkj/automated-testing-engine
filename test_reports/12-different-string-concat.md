# Issue 12: Different String Concatenations

## Description
Two different ways of concatenating strings result in programs deemed to be unequivalent by the `error_localizer`, `feedback_error`, `feedback_fix` and `repair` endpoints although they return the same output and thus should be semantically equivalent.

### Base Program

```py
def test_string():
	return ('Part 1'
	'Part 2'
	'Part 3')
```

### Modified Program
```py
def test_string():
	return 'Part 1' + 'Part 2' + 'Part 3'
```

### Input
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"test_string\": {\"name\": \"test_string\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"DictInit\", \"args\": [], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"DictInit\", \"args\": [], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_string'\"}, \"types\": {}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"test_string\": {\"name\": \"test_string\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"$ret\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"\\\"Part 1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"Part 2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"\\\"Part 3\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"\\\"Part 1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"Part 2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"\\\"Part 3\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"$ret\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"\\\"Part 1\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"\\\"Part 2\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"\\\"Part 3\\\"\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'test_string'\"}, \"types\": {}}}}",
    "function": "test_string",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

### Output

#### Error Localizer
```json
{
    "errorLocations": {
        "test_string": [
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

#### Feedback Error
```json
[
    {
        "lineNumber": 2,
        "hintStrings": [
            "Incorrect return value"
        ]
    }
]
```

#### Feedback Fix
```json
[
    {
        "lineNumber": 2,
        "oldExpr": "return ((\"Part 1\" + \"Part 2\") + \"Part 3\")",
        "newExpr": "return {}",
        "repairStrings": [
            "Wrong expression. Change return ((\"Part 1\" + \"Part 2\") + \"Part 3\"); to return {};"
        ]
    }
]
```

#### Repair
```json
[
    {
        "totalCost": 34.0,
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
                "cost": 34.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "$ret",
                        "primed": false,
                        "line": 0
                    },
                    "val1": {
                        "tokentype": "Operation",
                        "name": "Add",
                        "args": [
                            {
                                "tokentype": "Operation",
                                "name": "Add",
                                "args": [
                                    {
                                        "tokentype": "Constant",
                                        "value": "\"Part 1\"",
                                        "line": 2
                                    },
                                    {
                                        "tokentype": "Constant",
                                        "value": "\"Part 2\"",
                                        "line": 2
                                    }
                                ],
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "\"Part 3\"",
                                "line": 2
                            }
                        ],
                        "line": 2
                    },
                    "val2": {
                        "tokentype": "Operation",
                        "name": "DictInit",
                        "args": [],
                        "line": 0
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Operation",
                            "name": "Add",
                            "args": [
                                {
                                    "tokentype": "Operation",
                                    "name": "Add",
                                    "args": [
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Part 1\"",
                                            "line": 2
                                        },
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Part 2\"",
                                            "line": 2
                                        }
                                    ],
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "\"Part 3\"",
                                    "line": 2
                                }
                            ],
                            "line": 2
                        },
                        {
                            "tokentype": "Operation",
                            "name": "DictInit",
                            "args": [],
                            "line": 0
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
                            "tokentype": "Operation",
                            "name": "Add",
                            "args": [
                                {
                                    "tokentype": "Operation",
                                    "name": "Add",
                                    "args": [
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Part 1\"",
                                            "line": 2
                                        },
                                        {
                                            "tokentype": "Constant",
                                            "value": "\"Part 2\"",
                                            "line": 2
                                        }
                                    ],
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "\"Part 3\"",
                                    "line": 2
                                }
                            ],
                            "line": 2
                        },
                        {
                            "tokentype": "Operation",
                            "name": "DictInit",
                            "args": [],
                            "line": 0
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
                "funcName": "test_string"
            }
        ]
    }
]

```

## Related Test Reports
Refer to Test Report ID c8d7daf5.