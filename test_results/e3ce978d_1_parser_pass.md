# Test Report

Time: 2024-04-14 07:32:19.624823

### Base Program

```py
def sum_of_square_root(a, b):
	return (a**0.5) + (b**0.5)
```

## Test Case 1

### Modified Program

```py
def sum_of_square_root(a, b):
    return a ** 0.5 + b ** 0.5
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def sum_of_square_root(a, b):\n    return a ** 0.5 + b ** 0.5"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "importStatements": [],
    "fncs": {
        "sum_of_square_root": {
            "name": "sum_of_square_root",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "a",
                    "val1": "*",
                    "valueArray": [
                        "a",
                        "*"
                    ],
                    "valueList": [
                        "a",
                        "*"
                    ]
                },
                {
                    "val0": "b",
                    "val1": "*",
                    "valueArray": [
                        "b",
                        "*"
                    ],
                    "valueList": [
                        "b",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "Pow",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "0.5",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Pow",
                                    "args": [
                                        {
                                            "name": "b",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "0.5",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "0.5",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "0.5",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "0.5",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "0.5",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'sum_of_square_root'"
            },
            "types": {}
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def sum_of_square_root(a, b):
    if True:
        return a ** 0.5 + b ** 0.5
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def sum_of_square_root(a, b):\n    if True:\n        return a ** 0.5 + b ** 0.5"
}
```

Message: 
```
Success
```

Actual Output: 
```json
{
    "importStatements": [],
    "fncs": {
        "sum_of_square_root": {
            "name": "sum_of_square_root",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "a",
                    "val1": "*",
                    "valueArray": [
                        "a",
                        "*"
                    ],
                    "valueList": [
                        "a",
                        "*"
                    ]
                },
                {
                    "val0": "b",
                    "val1": "*",
                    "valueArray": [
                        "b",
                        "*"
                    ],
                    "valueList": [
                        "b",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "value": "True",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "Pow",
                                            "args": [
                                                {
                                                    "name": "a",
                                                    "primed": false,
                                                    "line": 3,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0.5",
                                                    "line": 3,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 3,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Pow",
                                            "args": [
                                                {
                                                    "name": "b",
                                                    "primed": false,
                                                    "line": 3,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0.5",
                                                    "line": 3,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 3,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "value": "True",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Pow",
                                                "args": [
                                                    {
                                                        "name": "a",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0.5",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Pow",
                                                "args": [
                                                    {
                                                        "name": "b",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0.5",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "value": "True",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Pow",
                                                "args": [
                                                    {
                                                        "name": "a",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0.5",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Pow",
                                                "args": [
                                                    {
                                                        "name": "b",
                                                        "primed": false,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0.5",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'sum_of_square_root'"
            },
            "types": {}
        }
    }
}
```

</details>

