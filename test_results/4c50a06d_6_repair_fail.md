# Test Report

Time: 2024-04-08 04:56:20.339483

### Base Program

```py
def main():
	my_list = [1, 2, 3, 4, 5]
	total = 1 + 2 + 3 + 4 + 5
	return total
```

## Test Case 1

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

<details>
<summary>repair endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"my_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"total\", \"val1\": {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"4\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"total\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"4\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}], \"valueList\": [\"total\", {\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"name\": \"Add\", \"args\": [{\"value\": \"1\", \"line\": 3, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"3\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"4\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3, \"tokentype\": \"Operation\"}, {\"value\": \"5\", \"line\": 3, \"tokentype\": \"Constant\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"total\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"total\": \"*\", \"my_list\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [], \"locexprs\": {\"1\": [{\"val0\": \"my_list\", \"val1\": {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}], \"valueList\": [\"my_list\", {\"name\": \"ListInit\", \"args\": [{\"value\": \"1\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"2\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"3\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"4\", \"line\": 2, \"tokentype\": \"Constant\"}, {\"value\": \"5\", \"line\": 2, \"tokentype\": \"Constant\"}], \"line\": 2}]}, {\"val0\": \"total\", \"val1\": {\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8, \"tokentype\": \"Operation\"}, \"valueArray\": [\"total\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}], \"valueList\": [\"total\", {\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"AssAdd\", \"args\": [{\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, {\"value\": \"0\", \"line\": 4, \"tokentype\": \"Constant\"}], \"line\": 4, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 5, \"tokentype\": \"Variable\"}, {\"value\": \"1\", \"line\": 5, \"tokentype\": \"Constant\"}], \"line\": 5, \"tokentype\": \"Operation\"}], \"line\": 5, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 6, \"tokentype\": \"Variable\"}, {\"value\": \"2\", \"line\": 6, \"tokentype\": \"Constant\"}], \"line\": 6, \"tokentype\": \"Operation\"}], \"line\": 6, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 7, \"tokentype\": \"Variable\"}, {\"value\": \"3\", \"line\": 7, \"tokentype\": \"Constant\"}], \"line\": 7, \"tokentype\": \"Operation\"}], \"line\": 7, \"tokentype\": \"Operation\"}, {\"name\": \"GetElement\", \"args\": [{\"name\": \"my_list\", \"primed\": true, \"line\": 8, \"tokentype\": \"Variable\"}, {\"value\": \"4\", \"line\": 8, \"tokentype\": \"Constant\"}], \"line\": 8, \"tokentype\": \"Operation\"}], \"line\": 8}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"total\", \"primed\": true, \"line\": 9, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 9}], \"valueList\": [\"$ret\", {\"name\": \"total\", \"primed\": true, \"line\": 9}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"total\": \"*\", \"my_list\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[], [], [], [], [], [], [], [], [], []]"
}
```

Message: 
```
Repair endpoint failed
```

Actual Output: 
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

</details>

