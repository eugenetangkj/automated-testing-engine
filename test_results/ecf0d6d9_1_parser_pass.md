# Test Report

Time: 2024-04-14 11:22:10.081294

### Base Program

```py
def max_of_two_numbers(a, b):
    return a if a > b else b
```

## Test Case 1

### Modified Program

```py
def max_of_two_numbers(a, b):
    return a if a > b else b
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def max_of_two_numbers(a, b):\n    return a if a > b else b"
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
        "max_of_two_numbers": {
            "name": "max_of_two_numbers",
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
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "b",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "a",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "b",
                                    "primed": false,
                                    "line": 2,
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 2,
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 2,
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
                "1": "around the beginning of function 'max_of_two_numbers'"
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
def max_of_two_numbers(a, b):
    if a > b:
        return a
    else:
        return b
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def max_of_two_numbers(a, b):\n    if a > b:\n        return a\n    else:\n        return b"
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
        "max_of_two_numbers": {
            "name": "max_of_two_numbers",
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
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "b",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "a",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "b",
                                    "primed": false,
                                    "line": 5,
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 5,
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
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 5,
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
                "1": "around the beginning of function 'max_of_two_numbers'"
            },
            "types": {}
        }
    }
}
```

</details>

