# Issue 20: Sum of Numbers

## Description
Two equivalent programs of counting the sum of numbers from 1 to 5 lead to only the `errorlocalizer` endpoint detecting no error locations, while the `feedback_error`, `feedback_fix` and `repair` endpoints indicate that the programs are not equivalent. On closer inspections, some of the outputs from these endpoints that detect unequivalence do not make sense as well.

### Base Program

```py
def main():
	total = 1 + 2 + 3 + 4 + 5
	return total
```

### Modified Program
```py
def main():
	my_list = [1, 2, 3, 4, 5]
	total = 0
	total = my_list[0]
	total += my_list[1]
	total += my_list[2]
	total += my_list[3]
	total += my_list[4]
	return total
```

### Input
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"total\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"total\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"total\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"total\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"total\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"my_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"total\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"total\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"total\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"total\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 9}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"total\": \"*\", \"my_list\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

### Output

#### Error Localizer
```json
{
    "errorLocations": {},
    "errorInputs": []
}
```

#### Feedback Error
```json
[
    {
        "lineNumber": 2,
        "hintStrings": [
            "Wrong expression for variable: *my_list*"
        ]
    },
    {
        "lineNumber": 8,
        "hintStrings": []
    },
    {
        "lineNumber": 9,
        "hintStrings": []
    }
]
```

#### Feedback Fix
Notice how the repair strings start to contain technical terms like `AssAdd` instead of being in natural language.

```json
[
    {
        "lineNumber": 2,
        "oldExpr": "my_list = [1, 2, 3, 4, 5]",
        "newExpr": "my_list = ((((1 + 2) + 3) + 4) + 5)",
        "repairStrings": [
            "Wrong expression. Change my_list = [1, 2, 3, 4, 5]; to my_list = ((((1 + 2) + 3) + 4) + 5);"
        ]
    },
    {
        "lineNumber": 8,
        "oldExpr": "total = AssAdd(AssAdd(AssAdd(GetElement(my_list', 0), GetElement(my_list', 1)), GetElement(my_list', 2)), GetElement(my_list', 3)) += my_list[4]",
        "newExpr": "total = [1, 2, 3, 4, 5]",
        "repairStrings": [
            "Wrong Expression. total = AssAdd(AssAdd(AssAdd(GetElement(my_list', 0), GetElement(my_list', 1)), GetElement(my_list', 2)), GetElement(my_list', 3)) += my_list[4]; to total = [1, 2, 3, 4, 5];"
        ]
    },
    {
        "lineNumber": 9,
        "oldExpr": null,
        "newExpr": null,
        "repairStrings": []
    }
]
```

#### Repair
```json
[
    {
        "totalCost": 152.0,
        "localRepairs": [
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "total",
                            "primed": false,
                            "line": 9
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
                            "name": "total",
                            "primed": true,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": true,
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
                "cost": 18.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "my_list",
                        "primed": true,
                        "line": 4
                    },
                    "val1": {
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
                        "line": 2
                    },
                    "val2": {
                        "tokentype": "Operation",
                        "name": "Add",
                        "args": [
                            {
                                "tokentype": "Operation",
                                "name": "Add",
                                "args": [
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
                                                        "value": "1",
                                                        "line": 3
                                                    },
                                                    {
                                                        "tokentype": "Constant",
                                                        "value": "2",
                                                        "line": 3
                                                    }
                                                ],
                                                "line": 0
                                            },
                                            {
                                                "tokentype": "Constant",
                                                "value": "3",
                                                "line": 3
                                            }
                                        ],
                                        "line": 0
                                    },
                                    {
                                        "tokentype": "Constant",
                                        "value": "4",
                                        "line": 3
                                    }
                                ],
                                "line": 0
                            },
                            {
                                "tokentype": "Constant",
                                "value": "5",
                                "line": 3
                            }
                        ],
                        "line": 0
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": true,
                            "line": 4
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
                            "line": 2
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
                                            "tokentype": "Operation",
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "tokentype": "Operation",
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "tokentype": "Constant",
                                                            "value": "1",
                                                            "line": 3
                                                        },
                                                        {
                                                            "tokentype": "Constant",
                                                            "value": "2",
                                                            "line": 3
                                                        }
                                                    ],
                                                    "line": 0
                                                },
                                                {
                                                    "tokentype": "Constant",
                                                    "value": "3",
                                                    "line": 3
                                                }
                                            ],
                                            "line": 0
                                        },
                                        {
                                            "tokentype": "Constant",
                                            "value": "4",
                                            "line": 3
                                        }
                                    ],
                                    "line": 0
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "5",
                                    "line": 3
                                }
                            ],
                            "line": 0
                        }
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": true,
                            "line": 4
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
                            "line": 2
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
                                            "tokentype": "Operation",
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "tokentype": "Operation",
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "tokentype": "Constant",
                                                            "value": "1",
                                                            "line": 3
                                                        },
                                                        {
                                                            "tokentype": "Constant",
                                                            "value": "2",
                                                            "line": 3
                                                        }
                                                    ],
                                                    "line": 0
                                                },
                                                {
                                                    "tokentype": "Constant",
                                                    "value": "3",
                                                    "line": 3
                                                }
                                            ],
                                            "line": 0
                                        },
                                        {
                                            "tokentype": "Constant",
                                            "value": "4",
                                            "line": 3
                                        }
                                    ],
                                    "line": 0
                                },
                                {
                                    "tokentype": "Constant",
                                    "value": "5",
                                    "line": 3
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
            },
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "total",
                            "primed": false,
                            "line": 9
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
                            "name": "total",
                            "primed": true,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": true,
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
                "cost": 127.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "total",
                        "primed": false,
                        "line": 9
                    },
                    "val1": {
                        "tokentype": "Operation",
                        "name": "AssAdd",
                        "args": [
                            {
                                "tokentype": "Operation",
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "tokentype": "Operation",
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "tokentype": "Operation",
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "tokentype": "Operation",
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "tokentype": "Variable",
                                                                "name": "my_list",
                                                                "primed": true,
                                                                "line": 4
                                                            },
                                                            {
                                                                "tokentype": "Constant",
                                                                "value": "0",
                                                                "line": 4
                                                            }
                                                        ],
                                                        "line": 4
                                                    },
                                                    {
                                                        "tokentype": "Operation",
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "tokentype": "Variable",
                                                                "name": "my_list",
                                                                "primed": true,
                                                                "line": 5
                                                            },
                                                            {
                                                                "tokentype": "Constant",
                                                                "value": "1",
                                                                "line": 5
                                                            }
                                                        ],
                                                        "line": 5
                                                    }
                                                ],
                                                "line": 5
                                            },
                                            {
                                                "tokentype": "Operation",
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "tokentype": "Variable",
                                                        "name": "my_list",
                                                        "primed": true,
                                                        "line": 6
                                                    },
                                                    {
                                                        "tokentype": "Constant",
                                                        "value": "2",
                                                        "line": 6
                                                    }
                                                ],
                                                "line": 6
                                            }
                                        ],
                                        "line": 6
                                    },
                                    {
                                        "tokentype": "Operation",
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "tokentype": "Variable",
                                                "name": "my_list",
                                                "primed": true,
                                                "line": 7
                                            },
                                            {
                                                "tokentype": "Constant",
                                                "value": "3",
                                                "line": 7
                                            }
                                        ],
                                        "line": 7
                                    }
                                ],
                                "line": 7
                            },
                            {
                                "tokentype": "Operation",
                                "name": "GetElement",
                                "args": [
                                    {
                                        "tokentype": "Variable",
                                        "name": "my_list",
                                        "primed": true,
                                        "line": 8
                                    },
                                    {
                                        "tokentype": "Constant",
                                        "value": "4",
                                        "line": 8
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "line": 8
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
                            "name": "total",
                            "primed": false,
                            "line": 9
                        },
                        {
                            "tokentype": "Operation",
                            "name": "AssAdd",
                            "args": [
                                {
                                    "tokentype": "Operation",
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "tokentype": "Operation",
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "tokentype": "Operation",
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "tokentype": "Operation",
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "tokentype": "Variable",
                                                                    "name": "my_list",
                                                                    "primed": true,
                                                                    "line": 4
                                                                },
                                                                {
                                                                    "tokentype": "Constant",
                                                                    "value": "0",
                                                                    "line": 4
                                                                }
                                                            ],
                                                            "line": 4
                                                        },
                                                        {
                                                            "tokentype": "Operation",
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "tokentype": "Variable",
                                                                    "name": "my_list",
                                                                    "primed": true,
                                                                    "line": 5
                                                                },
                                                                {
                                                                    "tokentype": "Constant",
                                                                    "value": "1",
                                                                    "line": 5
                                                                }
                                                            ],
                                                            "line": 5
                                                        }
                                                    ],
                                                    "line": 5
                                                },
                                                {
                                                    "tokentype": "Operation",
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "tokentype": "Variable",
                                                            "name": "my_list",
                                                            "primed": true,
                                                            "line": 6
                                                        },
                                                        {
                                                            "tokentype": "Constant",
                                                            "value": "2",
                                                            "line": 6
                                                        }
                                                    ],
                                                    "line": 6
                                                }
                                            ],
                                            "line": 6
                                        },
                                        {
                                            "tokentype": "Operation",
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "tokentype": "Variable",
                                                    "name": "my_list",
                                                    "primed": true,
                                                    "line": 7
                                                },
                                                {
                                                    "tokentype": "Constant",
                                                    "value": "3",
                                                    "line": 7
                                                }
                                            ],
                                            "line": 7
                                        }
                                    ],
                                    "line": 7
                                },
                                {
                                    "tokentype": "Operation",
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "tokentype": "Variable",
                                            "name": "my_list",
                                            "primed": true,
                                            "line": 8
                                        },
                                        {
                                            "tokentype": "Constant",
                                            "value": "4",
                                            "line": 8
                                        }
                                    ],
                                    "line": 8
                                }
                            ],
                            "line": 8
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
                            "name": "total",
                            "primed": false,
                            "line": 9
                        },
                        {
                            "tokentype": "Operation",
                            "name": "AssAdd",
                            "args": [
                                {
                                    "tokentype": "Operation",
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "tokentype": "Operation",
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "tokentype": "Operation",
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "tokentype": "Operation",
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "tokentype": "Variable",
                                                                    "name": "my_list",
                                                                    "primed": true,
                                                                    "line": 4
                                                                },
                                                                {
                                                                    "tokentype": "Constant",
                                                                    "value": "0",
                                                                    "line": 4
                                                                }
                                                            ],
                                                            "line": 4
                                                        },
                                                        {
                                                            "tokentype": "Operation",
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "tokentype": "Variable",
                                                                    "name": "my_list",
                                                                    "primed": true,
                                                                    "line": 5
                                                                },
                                                                {
                                                                    "tokentype": "Constant",
                                                                    "value": "1",
                                                                    "line": 5
                                                                }
                                                            ],
                                                            "line": 5
                                                        }
                                                    ],
                                                    "line": 5
                                                },
                                                {
                                                    "tokentype": "Operation",
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "tokentype": "Variable",
                                                            "name": "my_list",
                                                            "primed": true,
                                                            "line": 6
                                                        },
                                                        {
                                                            "tokentype": "Constant",
                                                            "value": "2",
                                                            "line": 6
                                                        }
                                                    ],
                                                    "line": 6
                                                }
                                            ],
                                            "line": 6
                                        },
                                        {
                                            "tokentype": "Operation",
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "tokentype": "Variable",
                                                    "name": "my_list",
                                                    "primed": true,
                                                    "line": 7
                                                },
                                                {
                                                    "tokentype": "Constant",
                                                    "value": "3",
                                                    "line": 7
                                                }
                                            ],
                                            "line": 7
                                        }
                                    ],
                                    "line": 7
                                },
                                {
                                    "tokentype": "Operation",
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "tokentype": "Variable",
                                            "name": "my_list",
                                            "primed": true,
                                            "line": 8
                                        },
                                        {
                                            "tokentype": "Constant",
                                            "value": "4",
                                            "line": 8
                                        }
                                    ],
                                    "line": 8
                                }
                            ],
                            "line": 8
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
            },
            {
                "mapping": [
                    [
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "total",
                            "primed": false,
                            "line": 9
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
                            "name": "total",
                            "primed": true,
                            "line": 4
                        },
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": true,
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
                "cost": 7.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "$ret",
                        "primed": false,
                        "line": 0
                    },
                    "val1": {
                        "tokentype": "Variable",
                        "name": "total",
                        "primed": true,
                        "line": 9
                    },
                    "val2": {
                        "tokentype": "Variable",
                        "name": "my_list",
                        "primed": true,
                        "line": 4
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "$ret",
                            "primed": false,
                            "line": 0
                        },
                        {
                            "tokentype": "Variable",
                            "name": "total",
                            "primed": true,
                            "line": 9
                        },
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": true,
                            "line": 4
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
                            "tokentype": "Variable",
                            "name": "total",
                            "primed": true,
                            "line": 9
                        },
                        {
                            "tokentype": "Variable",
                            "name": "my_list",
                            "primed": true,
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
            }
        ]
    }
]
```

## Related Test Reports
Refer to Test Report ID 4c50a06d.