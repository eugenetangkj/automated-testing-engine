# Test Report

Time: 2024-04-07 09:24:45.664811

### Base Program

```py
def main(a, b):
	diff = a - b
	return diff
```

## Test Case 1

### Modified Program

```py
def main(a, b):
	a, b = b, a
	diff = b - a
	return diff
```

<details>
<summary>repair endpoint: failed ❌</summary>

Request Body: 
```json
{
    "language": "py",
    "reference_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, {\"name\": \"b\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}], \"line\": 2}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 3}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"diff\": \"*\"}}}}",
    "student_solution": "{\"importStatements\": [], \"fncs\": {\"main\": {\"name\": \"main\", \"rettype\": \"*\", \"initloc\": 1, \"endloc\": 0, \"params\": [{\"val0\": \"a\", \"val1\": \"*\", \"valueArray\": [\"a\", \"*\"], \"valueList\": [\"a\", \"*\"]}, {\"val0\": \"b\", \"val1\": \"*\", \"valueArray\": [\"b\", \"*\"], \"valueList\": [\"b\", \"*\"]}], \"locexprs\": {\"1\": [{\"val0\": \"b\", \"val1\": {\"name\": \"a\", \"primed\": false, \"line\": 2, \"tokentype\": \"Variable\"}, \"valueArray\": [\"b\", {\"name\": \"a\", \"primed\": false, \"line\": 2}], \"valueList\": [\"b\", {\"name\": \"a\", \"primed\": false, \"line\": 2}]}, {\"val0\": \"diff\", \"val1\": {\"name\": \"Sub\", \"args\": [{\"name\": \"b\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"a\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3, \"tokentype\": \"Operation\"}, \"valueArray\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"b\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"a\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}], \"valueList\": [\"diff\", {\"name\": \"Sub\", \"args\": [{\"name\": \"b\", \"primed\": true, \"line\": 3, \"tokentype\": \"Variable\"}, {\"name\": \"a\", \"primed\": false, \"line\": 3, \"tokentype\": \"Variable\"}], \"line\": 3}]}, {\"val0\": \"$ret\", \"val1\": {\"name\": \"diff\", \"primed\": true, \"line\": 4, \"tokentype\": \"Variable\"}, \"valueArray\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 4}], \"valueList\": [\"$ret\", {\"name\": \"diff\", \"primed\": true, \"line\": 4}]}]}, \"loctrans\": {\"1\": {}}, \"locdescs\": {\"1\": \"around the beginning of function 'main'\"}, \"types\": {\"b\": \"*\", \"diff\": \"*\"}}}}",
    "function": "main",
    "inputs": "[]",
    "args": "[[87, 27], [65, 39], [30, 14], [46, 96], [47, 77], [94, 56], [78, 29], [37, 50], [44, 80], [62, 87]]"
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
        "totalCost": 3.0,
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
                            "name": "b",
                            "primed": false,
                            "line": 2
                        },
                        {
                            "tokentype": "Variable",
                            "name": "b",
                            "primed": false,
                            "line": 3
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
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "a",
                            "primed": false,
                            "line": 2
                        },
                        {
                            "tokentype": "Variable",
                            "name": "a",
                            "primed": false,
                            "line": 2
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "diff",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "diff",
                            "primed": false,
                            "line": 4
                        }
                    ]
                ],
                "cost": 1.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "b",
                        "primed": false,
                        "line": 3
                    },
                    "val1": {
                        "tokentype": "Variable",
                        "name": "a",
                        "primed": false,
                        "line": 2
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "b",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "a",
                            "primed": false,
                            "line": 2
                        },
                        null
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "b",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "a",
                            "primed": false,
                            "line": 2
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
                            "name": "b",
                            "primed": false,
                            "line": 2
                        },
                        {
                            "tokentype": "Variable",
                            "name": "b",
                            "primed": false,
                            "line": 3
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
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "a",
                            "primed": false,
                            "line": 2
                        },
                        {
                            "tokentype": "Variable",
                            "name": "a",
                            "primed": false,
                            "line": 2
                        }
                    ],
                    [
                        {
                            "tokentype": "Variable",
                            "name": "diff",
                            "primed": false,
                            "line": 3
                        },
                        {
                            "tokentype": "Variable",
                            "name": "diff",
                            "primed": false,
                            "line": 4
                        }
                    ]
                ],
                "cost": 2.0,
                "repairedVariable": {
                    "val0": {
                        "tokentype": "Variable",
                        "name": "diff",
                        "primed": false,
                        "line": 4
                    },
                    "val1": {
                        "tokentype": "Operation",
                        "name": "Sub",
                        "args": [
                            {
                                "tokentype": "Variable",
                                "name": "b",
                                "primed": true,
                                "line": 3
                            },
                            {
                                "tokentype": "Variable",
                                "name": "a",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "line": 3
                    },
                    "val2": {
                        "tokentype": "Operation",
                        "name": "Sub",
                        "args": [
                            {
                                "tokentype": "Variable",
                                "name": "a",
                                "primed": false,
                                "line": 2
                            },
                            {
                                "tokentype": "Variable",
                                "name": "b",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "line": 0
                    },
                    "valueArray": [
                        {
                            "tokentype": "Variable",
                            "name": "diff",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Operation",
                            "name": "Sub",
                            "args": [
                                {
                                    "tokentype": "Variable",
                                    "name": "b",
                                    "primed": true,
                                    "line": 3
                                },
                                {
                                    "tokentype": "Variable",
                                    "name": "a",
                                    "primed": false,
                                    "line": 3
                                }
                            ],
                            "line": 3
                        },
                        {
                            "tokentype": "Operation",
                            "name": "Sub",
                            "args": [
                                {
                                    "tokentype": "Variable",
                                    "name": "a",
                                    "primed": false,
                                    "line": 2
                                },
                                {
                                    "tokentype": "Variable",
                                    "name": "b",
                                    "primed": false,
                                    "line": 3
                                }
                            ],
                            "line": 0
                        }
                    ],
                    "valueList": [
                        {
                            "tokentype": "Variable",
                            "name": "diff",
                            "primed": false,
                            "line": 4
                        },
                        {
                            "tokentype": "Operation",
                            "name": "Sub",
                            "args": [
                                {
                                    "tokentype": "Variable",
                                    "name": "b",
                                    "primed": true,
                                    "line": 3
                                },
                                {
                                    "tokentype": "Variable",
                                    "name": "a",
                                    "primed": false,
                                    "line": 3
                                }
                            ],
                            "line": 3
                        },
                        {
                            "tokentype": "Operation",
                            "name": "Sub",
                            "args": [
                                {
                                    "tokentype": "Variable",
                                    "name": "a",
                                    "primed": false,
                                    "line": 2
                                },
                                {
                                    "tokentype": "Variable",
                                    "name": "b",
                                    "primed": false,
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
            }
        ]
    }
]
```

</details>

