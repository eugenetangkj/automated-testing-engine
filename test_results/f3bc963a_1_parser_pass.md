# Test Report

Time: 2024-04-14 11:21:15.713770

### Base Program

```py
def multiply_numbers(a, b): return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

## Test Case 1

### Modified Program

```py
def multiply_numbers(a, b):
    return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def multiply_numbers(a, b):\n    return a * b if type(a) in [int, float] and type(b) in [int, float] else 'Invalid input'"
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
        "multiply_numbers": {
            "name": "multiply_numbers",
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
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "In",
                                            "args": [
                                                {
                                                    "name": "type",
                                                    "args": [
                                                        {
                                                            "name": "a",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 2,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "ListInit",
                                                    "args": [
                                                        {
                                                            "name": "int",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "float",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 2,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "In",
                                            "args": [
                                                {
                                                    "name": "type",
                                                    "args": [
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
                                                    "name": "ListInit",
                                                    "args": [
                                                        {
                                                            "name": "int",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "float",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 2,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Mult",
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
                                    "value": "\"Invalid input\"",
                                    "line": 2,
                                    "tokentype": "Constant"
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
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "type",
                                                        "args": [
                                                            {
                                                                "name": "a",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ListInit",
                                                        "args": [
                                                            {
                                                                "name": "int",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "float",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "type",
                                                        "args": [
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
                                                        "name": "ListInit",
                                                        "args": [
                                                            {
                                                                "name": "int",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "float",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mult",
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
                                        "value": "\"Invalid input\"",
                                        "line": 2,
                                        "tokentype": "Constant"
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
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "type",
                                                        "args": [
                                                            {
                                                                "name": "a",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ListInit",
                                                        "args": [
                                                            {
                                                                "name": "int",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "float",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "type",
                                                        "args": [
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
                                                        "name": "ListInit",
                                                        "args": [
                                                            {
                                                                "name": "int",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "float",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mult",
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
                                        "value": "\"Invalid input\"",
                                        "line": 2,
                                        "tokentype": "Constant"
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
                "1": "around the beginning of function 'multiply_numbers'"
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
def multiply_numbers(a, b):
    if type(a) in [int, float] and type(b) in [int, float]:
        return a * b
    else:
        return 'Invalid input'
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def multiply_numbers(a, b):\n    if type(a) in [int, float] and type(b) in [int, float]:\n        return a * b\n    else:\n        return 'Invalid input'"
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
        "multiply_numbers": {
            "name": "multiply_numbers",
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
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "In",
                                            "args": [
                                                {
                                                    "name": "type",
                                                    "args": [
                                                        {
                                                            "name": "a",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 2,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "ListInit",
                                                    "args": [
                                                        {
                                                            "name": "int",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "float",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 2,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "In",
                                            "args": [
                                                {
                                                    "name": "type",
                                                    "args": [
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
                                                    "name": "ListInit",
                                                    "args": [
                                                        {
                                                            "name": "int",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "float",
                                                            "primed": false,
                                                            "line": 2,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 2,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "b",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "\"Invalid input\"",
                                    "line": 5,
                                    "tokentype": "Constant"
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
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "type",
                                                        "args": [
                                                            {
                                                                "name": "a",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ListInit",
                                                        "args": [
                                                            {
                                                                "name": "int",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "float",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "type",
                                                        "args": [
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
                                                        "name": "ListInit",
                                                        "args": [
                                                            {
                                                                "name": "int",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "float",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "\"Invalid input\"",
                                        "line": 5,
                                        "tokentype": "Constant"
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
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "type",
                                                        "args": [
                                                            {
                                                                "name": "a",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "ListInit",
                                                        "args": [
                                                            {
                                                                "name": "int",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "float",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "type",
                                                        "args": [
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
                                                        "name": "ListInit",
                                                        "args": [
                                                            {
                                                                "name": "int",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "float",
                                                                "primed": false,
                                                                "line": 2,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 2,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "b",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "\"Invalid input\"",
                                        "line": 5,
                                        "tokentype": "Constant"
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
                "1": "around the beginning of function 'multiply_numbers'"
            },
            "types": {}
        }
    }
}
```

</details>

