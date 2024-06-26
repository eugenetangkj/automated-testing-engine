# Test Report

Time: 2024-03-30 08:03:50.573832

### Base Program

```py
def last_remaining(n: int) -> int:
    direction = True
    head = 1
    remaining = n
    step = 1

    while remaining > 1:
        if direction or remaining % 2 == 1:
            head += step
        remaining //= 2
        step *= 2
        direction = not direction

    return head
```

## Test Case 1

### Modified Program

```py
def last_remaining(n: int) -> int:
    direction = True
    head = 1
    remaining = n
    step = 1
    while remaining > 1:
        if direction or remaining % 2 == 1:
            head += step
        remaining //= 2
        step *= 2
        direction = not direction
    return head
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def last_remaining(n: int) -> int:\n    direction = True\n    head = 1\n    remaining = n\n    step = 1\n    while remaining > 1:\n        if direction or remaining % 2 == 1:\n            head += step\n        remaining //= 2\n        step *= 2\n        direction = not direction\n    return head"
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
        "last_remaining": {
            "name": "last_remaining",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "n",
                    "val1": "*",
                    "valueArray": [
                        "n",
                        "*"
                    ],
                    "valueList": [
                        "n",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "direction",
                        "val1": {
                            "value": "True",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "direction",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "direction",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "head",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "head",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "head",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "remaining",
                        "val1": {
                            "name": "n",
                            "primed": false,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "remaining",
                            {
                                "name": "n",
                                "primed": false,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "remaining",
                            {
                                "name": "n",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "step",
                        "val1": {
                            "value": "1",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "step",
                            {
                                "value": "1",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "step",
                            {
                                "value": "1",
                                "line": 5
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "remaining",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "head",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "head",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "head",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "head",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Or",
                                    "args": [
                                        {
                                            "name": "direction",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "Mod",
                                                    "args": [
                                                        {
                                                            "name": "remaining",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "2",
                                                            "line": 7,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 7,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 7,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "head",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "step",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "head",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "head",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "direction",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "remaining",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "head",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "step",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "head",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "head",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "direction",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "remaining",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "head",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "step",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "head",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "remaining",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "remaining",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "2",
                                    "line": 9,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "remaining",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "remaining",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "step",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "step",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "2",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "step",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "step",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "step",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "step",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "direction",
                        "val1": {
                            "name": "Not",
                            "args": [
                                {
                                    "name": "direction",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "direction",
                            {
                                "name": "Not",
                                "args": [
                                    {
                                        "name": "direction",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "direction",
                            {
                                "name": "Not",
                                "args": [
                                    {
                                        "name": "direction",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 2
                },
                "2": {
                    "false": 3,
                    "true": 4
                },
                "3": {},
                "4": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'last_remaining'",
                "2": "the condition of the 'while' loop at line 6",
                "3": "*after* the 'while' loop starting at line 6",
                "4": "inside the body of the 'while' loop beginning at line 7"
            },
            "types": {
                "head": "*",
                "step": "*",
                "remaining": "*",
                "direction": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def last_remaining(var_0: int) -> int:
    direction = True
    head = 1
    remaining = var_0
    step = 1
    while remaining > 1:
        if direction or remaining % 2 == 1:
            head += step
        remaining //= 2
        step *= 2
        direction = not direction
    return head
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def last_remaining(var_0: int) -> int:\n    direction = True\n    head = 1\n    remaining = var_0\n    step = 1\n    while remaining > 1:\n        if direction or remaining % 2 == 1:\n            head += step\n        remaining //= 2\n        step *= 2\n        direction = not direction\n    return head"
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
        "last_remaining": {
            "name": "last_remaining",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_0",
                    "val1": "*",
                    "valueArray": [
                        "var_0",
                        "*"
                    ],
                    "valueList": [
                        "var_0",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "direction",
                        "val1": {
                            "value": "True",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "direction",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "direction",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "head",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "head",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "head",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "remaining",
                        "val1": {
                            "name": "var_0",
                            "primed": false,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "remaining",
                            {
                                "name": "var_0",
                                "primed": false,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "remaining",
                            {
                                "name": "var_0",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "step",
                        "val1": {
                            "value": "1",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "step",
                            {
                                "value": "1",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "step",
                            {
                                "value": "1",
                                "line": 5
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "remaining",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "head",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "head",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "head",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "head",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Or",
                                    "args": [
                                        {
                                            "name": "direction",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "Mod",
                                                    "args": [
                                                        {
                                                            "name": "remaining",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "2",
                                                            "line": 7,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 7,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 7,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "head",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "step",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "head",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "head",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "direction",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "remaining",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "head",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "step",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "head",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "head",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "direction",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "remaining",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "head",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "step",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "head",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "remaining",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "remaining",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "2",
                                    "line": 9,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "remaining",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "remaining",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "step",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "step",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "2",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "step",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "step",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "step",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "step",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "direction",
                        "val1": {
                            "name": "Not",
                            "args": [
                                {
                                    "name": "direction",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "direction",
                            {
                                "name": "Not",
                                "args": [
                                    {
                                        "name": "direction",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "direction",
                            {
                                "name": "Not",
                                "args": [
                                    {
                                        "name": "direction",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 2
                },
                "2": {
                    "false": 3,
                    "true": 4
                },
                "3": {},
                "4": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'last_remaining'",
                "2": "the condition of the 'while' loop at line 6",
                "3": "*after* the 'while' loop starting at line 6",
                "4": "inside the body of the 'while' loop beginning at line 7"
            },
            "types": {
                "head": "*",
                "step": "*",
                "remaining": "*",
                "direction": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def last_remaining(var_1: int) -> int:
    direction = True
    head = 1
    remaining = var_1
    step = 1
    while remaining > 1:
        if direction or remaining % 2 == 1:
            head += step
        remaining //= 2
        step *= 2
        direction = not direction
    return head
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def last_remaining(var_1: int) -> int:\n    direction = True\n    head = 1\n    remaining = var_1\n    step = 1\n    while remaining > 1:\n        if direction or remaining % 2 == 1:\n            head += step\n        remaining //= 2\n        step *= 2\n        direction = not direction\n    return head"
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
        "last_remaining": {
            "name": "last_remaining",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_1",
                    "val1": "*",
                    "valueArray": [
                        "var_1",
                        "*"
                    ],
                    "valueList": [
                        "var_1",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "direction",
                        "val1": {
                            "value": "True",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "direction",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "direction",
                            {
                                "value": "True",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "head",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "head",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "head",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "remaining",
                        "val1": {
                            "name": "var_1",
                            "primed": false,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "remaining",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "remaining",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "step",
                        "val1": {
                            "value": "1",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "step",
                            {
                                "value": "1",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "step",
                            {
                                "value": "1",
                                "line": 5
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "remaining",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "head",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "head",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "head",
                                "primed": false,
                                "line": 12
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "head",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Or",
                                    "args": [
                                        {
                                            "name": "direction",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "Mod",
                                                    "args": [
                                                        {
                                                            "name": "remaining",
                                                            "primed": false,
                                                            "line": 7,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "2",
                                                            "line": 7,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 7,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 7,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "head",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "step",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "head",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "head",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "direction",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "remaining",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "head",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "step",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "head",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "head",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Or",
                                        "args": [
                                            {
                                                "name": "direction",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "remaining",
                                                                "primed": false,
                                                                "line": 7,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "2",
                                                                "line": 7,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 7,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 7,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "head",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "step",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "head",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "remaining",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "remaining",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "2",
                                    "line": 9,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "remaining",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "remaining",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "remaining",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 9,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "step",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "step",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "2",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "step",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "step",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "step",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "step",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "2",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "direction",
                        "val1": {
                            "name": "Not",
                            "args": [
                                {
                                    "name": "direction",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "direction",
                            {
                                "name": "Not",
                                "args": [
                                    {
                                        "name": "direction",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "direction",
                            {
                                "name": "Not",
                                "args": [
                                    {
                                        "name": "direction",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 2
                },
                "2": {
                    "false": 3,
                    "true": 4
                },
                "3": {},
                "4": {
                    "true": 2
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'last_remaining'",
                "2": "the condition of the 'while' loop at line 6",
                "3": "*after* the 'while' loop starting at line 6",
                "4": "inside the body of the 'while' loop beginning at line 7"
            },
            "types": {
                "head": "*",
                "step": "*",
                "remaining": "*",
                "direction": "*"
            }
        }
    }
}
```

</details>

