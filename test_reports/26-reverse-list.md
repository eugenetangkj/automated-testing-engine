# Issue 26: Reverse List

## Description
This issue was caught by one of our metamorphic relations, which is `ReverseListModifier`. We have a base program that has a list variable. In the modified program, if we reverse the list and update the indices used for accessing variables, the semantics are equivalent, but the `errorlocalizer`, `feedback_fix`, `feedback_error` and `repair` endpoints would detect that the programs are not equivalent, suggesting fixes instead.

### Base Program

```py
def main():
	inner_list = [1, 2, 3, 4, 5]
	sum = inner_list[1] + inner_list[2] + inner_list[3]
	return sum
```

### Modified Program
```py
def main():
    inner_list = [5, 4, 3, 2, 1]
    sum = inner_list[3] + inner_list[2] + inner_list[1]
    return sum
```

### Input
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"inner_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"inner_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"sum\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"inner_list\": \"*\", \"sum\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"inner_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"inner_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"inner_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"sum\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}], \"valueList\": [\"sum\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"inner_list\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"sum\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"sum\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"inner_list\": \"*\", \"sum\": \"*\"}}}}",
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
                            "name": "inner_list",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "inner_list",
                            "primed": false,
                            "line": 3
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "sum",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "sum",
                            "primed": false,
                            "line": 4
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
                                "name": "inner_list",
                                "primed": false,
                                "line": 3
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
        "hintStrings": []
    }
]
```

#### Feedback Fix
```json
[
    {
        "lineNumber": 2,
        "oldExpr": "inner_list = [5, 4, 3, 2, 1]",
        "newExpr": "inner_list = [1, 2, 3, 4, 5]",
        "repairStrings": [
            "Wrong Expression. inner_list = [5, 4, 3, 2, 1]; to inner_list = [1, 2, 3, 4, 5];"
        ]
    }
]
```

#### Repair
```json
[
    {
        "totalCost": 4.0,
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
                            "name": "inner_list",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "inner_list",
                            "primed": false,
                            "line": 3
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "sum",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "sum",
                            "primed": false,
                            "line": 4
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
                "cost": 4.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "inner_list",
                        "primed": false,
                        "line": 3
                    },
                    "val1": {
                        "tokentype": "Operation",
                        "name": "ListInit",
                        "args": [
                            {
                                "tokentype": "Constant",
                                "value": "5",
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "4",
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "3",
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "2",
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "1",
                                "line": 2
                            }
                        ],
                        "line": 2
                    },
                    "val2": {
                        "tokentype": "Operation",
                        "name": "ListInit",
                        "args": [
                            {
                                "tokentype": "Constant",
                                "value": "1",
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "2",
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "3",
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "4",
                                "line": 2
                            },
                            {
                                "tokentype": "Constant",
                                "value": "5",
                                "line": 2
                            }
                        ],
                        "line": 0
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "inner_list",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Operation",
                            "name": "ListInit",
                            "args": [
                                {
                                    "tokentype": "Constant",
                                    "value": "5",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "4",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "3",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "2",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "1",
                                    "line": 2
                                }
                            ],
                            "line": 2
                        },
                        {
                            "tokentype": "Operation",
                            "name": "ListInit",
                            "args": [
                                {
                                    "tokentype": "Constant",
                                    "value": "1",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "2",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "3",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "4",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "5",
                                    "line": 2
                                }
                            ],
                            "line": 0
                        }
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "inner_list",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Operation",
                            "name": "ListInit",
                            "args": [
                                {
                                    "tokentype": "Constant",
                                    "value": "5",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "4",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "3",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "2",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "1",
                                    "line": 2
                                }
                            ],
                            "line": 2
                        },
                        {
                            "tokentype": "Operation",
                            "name": "ListInit",
                            "args": [
                                {
                                    "tokentype": "Constant",
                                    "value": "1",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "2",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "3",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "4",
                                    "line": 2
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "5",
                                    "line": 2
                                }
                            ],
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
                "funcName": "main"
            }
        ]
    }
]
```

## Related Test Reports
Refer to Test Report ID 9e34a669.