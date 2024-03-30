# Test Report

Time: 2024-03-30 06:29:12.538179

### Base Program

```py
def minNonZeroProduct(p: int) -> int:
    mod = 10**9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod
```

## Test Case 1

### Modified Program

```py
def minNonZeroProduct(p: int) -> int:
    mod = 10 ** 9 + 7
    x = (1 << p) - 1
    y = (1 << p) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minNonZeroProduct(p: int) -> int:\n    mod = 10 ** 9 + 7\n    x = (1 << p) - 1\n    y = (1 << p) - 2\n    z = pow(y, x - 1, mod)\n    return x * z % mod"
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
        "minNonZeroProduct": {
            "name": "minNonZeroProduct",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "p",
                    "val1": "*",
                    "valueArray": [
                        "p",
                        "*"
                    ],
                    "valueList": [
                        "p",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "mod",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "Pow",
                                    "args": [
                                        {
                                            "value": "10",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "9",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "7",
                                    "line": 2,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "mod",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "value": "10",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "9",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "7",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "mod",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "value": "10",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "9",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "7",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "x",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 3,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "x",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "y",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "2",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "y",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "y",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "z",
                        "val1": {
                            "name": "pow",
                            "args": [
                                {
                                    "name": "y",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": true,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 5,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "mod",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "z",
                            {
                                "name": "pow",
                                "args": [
                                    {
                                        "name": "y",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "z",
                            {
                                "name": "pow",
                                "args": [
                                    {
                                        "name": "y",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Mod",
                            "args": [
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "z",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "mod",
                                    "primed": true,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "z",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "z",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'minNonZeroProduct'"
            },
            "types": {
                "mod": "*",
                "x": "*",
                "y": "*",
                "z": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def minNonZeroProduct(var_0: int) -> int:
    mod = 10 ** 9 + 7
    x = (1 << var_0) - 1
    y = (1 << var_0) - 2
    z = pow(y, x - 1, mod)
    return x * z % mod
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minNonZeroProduct(var_0: int) -> int:\n    mod = 10 ** 9 + 7\n    x = (1 << var_0) - 1\n    y = (1 << var_0) - 2\n    z = pow(y, x - 1, mod)\n    return x * z % mod"
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
        "minNonZeroProduct": {
            "name": "minNonZeroProduct",
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
                        "val0": "mod",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "Pow",
                                    "args": [
                                        {
                                            "value": "10",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "9",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "7",
                                    "line": 2,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "mod",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "value": "10",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "9",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "7",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "mod",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "value": "10",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "9",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "7",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "x",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 3,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "x",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "y",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "2",
                                    "line": 4,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "y",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "y",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "2",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "z",
                        "val1": {
                            "name": "pow",
                            "args": [
                                {
                                    "name": "y",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": true,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
                                            "line": 5,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "mod",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "z",
                            {
                                "name": "pow",
                                "args": [
                                    {
                                        "name": "y",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "z",
                            {
                                "name": "pow",
                                "args": [
                                    {
                                        "name": "y",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Mod",
                            "args": [
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "z",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "mod",
                                    "primed": true,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "z",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "z",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'minNonZeroProduct'"
            },
            "types": {
                "mod": "*",
                "x": "*",
                "y": "*",
                "z": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def minNonZeroProduct(p: int) -> int:
    mod = 7 + 10 ** 9
    x = (1 << p) + -1
    y = (1 << p) + -2
    z = pow(y, x + -1, mod)
    return z * x % mod
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minNonZeroProduct(p: int) -> int:\n    mod = 7 + 10 ** 9\n    x = (1 << p) + -1\n    y = (1 << p) + -2\n    z = pow(y, x + -1, mod)\n    return z * x % mod"
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
        "minNonZeroProduct": {
            "name": "minNonZeroProduct",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "p",
                    "val1": "*",
                    "valueArray": [
                        "p",
                        "*"
                    ],
                    "valueList": [
                        "p",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "mod",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "value": "7",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Pow",
                                    "args": [
                                        {
                                            "value": "10",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "9",
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
                            "mod",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "7",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "value": "10",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "9",
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
                            "mod",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "7",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "value": "10",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "9",
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
                    },
                    {
                        "val0": "x",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 3,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
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
                        "valueArray": [
                            "x",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "y",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "2",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "y",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "2",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "y",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "2",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "z",
                        "val1": {
                            "name": "pow",
                            "args": [
                                {
                                    "name": "y",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": true,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "mod",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "z",
                            {
                                "name": "pow",
                                "args": [
                                    {
                                        "name": "y",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "z",
                            {
                                "name": "pow",
                                "args": [
                                    {
                                        "name": "y",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Mod",
                            "args": [
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "z",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "x",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "mod",
                                    "primed": true,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "z",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "z",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'minNonZeroProduct'"
            },
            "types": {
                "mod": "*",
                "x": "*",
                "y": "*",
                "z": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def minNonZeroProduct(var_1: int) -> int:
    mod = 7 + 10 ** 9
    x = (1 << var_1) + -1
    y = (1 << var_1) + -2
    z = pow(y, x + -1, mod)
    return z * x % mod
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minNonZeroProduct(var_1: int) -> int:\n    mod = 7 + 10 ** 9\n    x = (1 << var_1) + -1\n    y = (1 << var_1) + -2\n    z = pow(y, x + -1, mod)\n    return z * x % mod"
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
        "minNonZeroProduct": {
            "name": "minNonZeroProduct",
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
                        "val0": "mod",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "value": "7",
                                    "line": 2,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Pow",
                                    "args": [
                                        {
                                            "value": "10",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "9",
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
                            "mod",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "7",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "value": "10",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "9",
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
                            "mod",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "value": "7",
                                        "line": 2,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Pow",
                                        "args": [
                                            {
                                                "value": "10",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "9",
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
                    },
                    {
                        "val0": "x",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 3,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
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
                        "valueArray": [
                            "x",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "x",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "y",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "2",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "y",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "2",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "y",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "2",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "z",
                        "val1": {
                            "name": "pow",
                            "args": [
                                {
                                    "name": "y",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "x",
                                            "primed": true,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 5,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "mod",
                                    "primed": true,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "z",
                            {
                                "name": "pow",
                                "args": [
                                    {
                                        "name": "y",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "z",
                            {
                                "name": "pow",
                                "args": [
                                    {
                                        "name": "y",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 5,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Mod",
                            "args": [
                                {
                                    "name": "Mult",
                                    "args": [
                                        {
                                            "name": "z",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "x",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "mod",
                                    "primed": true,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "z",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "Mod",
                                "args": [
                                    {
                                        "name": "Mult",
                                        "args": [
                                            {
                                                "name": "z",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "x",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "mod",
                                        "primed": true,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'minNonZeroProduct'"
            },
            "types": {
                "mod": "*",
                "x": "*",
                "y": "*",
                "z": "*"
            }
        }
    }
}
```

</details>

