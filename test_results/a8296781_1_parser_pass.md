# Test Report

Time: 2024-03-30 08:35:09.832914

### Base Program

```py
def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1
    return ans
```

## Test Case 1

### Modified Program

```py
def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i & i - 1] + 1
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def countBits(n):\n    ans = [0] * (n + 1)\n    for i in range(1, n + 1):\n        ans[i] = ans[i & i - 1] + 1\n    return ans"
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
        "countBits": {
            "name": "countBits",
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
                        "val0": "ans",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "n",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 5
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "ans",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "BitAnd",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "value": "1",
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
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
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
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "BitAnd",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "1",
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
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
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
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "BitAnd",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "1",
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
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
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
                "1": "around the beginning of function 'countBits'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def countBits(var_0):
    ans = [0] * (var_0 + 1)
    for i in range(1, var_0 + 1):
        ans[i] = ans[i & i - 1] + 1
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def countBits(var_0):\n    ans = [0] * (var_0 + 1)\n    for i in range(1, var_0 + 1):\n        ans[i] = ans[i & i - 1] + 1\n    return ans"
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
        "countBits": {
            "name": "countBits",
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
                        "val0": "ans",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "1",
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "1",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 5
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "ans",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "BitAnd",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "value": "1",
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
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
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
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "BitAnd",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "1",
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
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
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
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "BitAnd",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "value": "1",
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
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
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
                "1": "around the beginning of function 'countBits'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def countBits(n):
    ans = (1 + n) * [0]
    for i in range(1, 1 + n):
        ans[i] = 1 + ans[i & i + -1]
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def countBits(n):\n    ans = (1 + n) * [0]\n    for i in range(1, 1 + n):\n        ans[i] = 1 + ans[i & i + -1]\n    return ans"
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
        "countBits": {
            "name": "countBits",
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
                        "val0": "ans",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "n",
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
                                            "value": "0",
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "n",
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
                                                "value": "0",
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "n",
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
                                                "value": "0",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 3,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "n",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
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
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 3,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "n",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
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
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 5
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "ans",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "BitAnd",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
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
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
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
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "BitAnd",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
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
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
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
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "BitAnd",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
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
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
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
                "1": "around the beginning of function 'countBits'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def countBits(var_1):
    ans = (1 + var_1) * [0]
    for i in range(1, 1 + var_1):
        ans[i] = 1 + ans[i & i + -1]
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def countBits(var_1):\n    ans = (1 + var_1) * [0]\n    for i in range(1, 1 + var_1):\n        ans[i] = 1 + ans[i & i + -1]\n    return ans"
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
        "countBits": {
            "name": "countBits",
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
                        "val0": "ans",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "var_1",
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
                                            "value": "0",
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_1",
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
                                                "value": "0",
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
                            "ans",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "var_1",
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
                                                "value": "0",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 3,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
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
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
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
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
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
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    }
                ],
                "2": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 5
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
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
                        "val0": "ans",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "ans",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "BitAnd",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 4,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 4,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
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
                                                        }
                                                    ],
                                                    "line": 4,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 4,
                                            "tokentype": "Operation"
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
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "BitAnd",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
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
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
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
                            "ans",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "BitAnd",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 4,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 4,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
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
                                                            }
                                                        ],
                                                        "line": 4,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 4,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 4
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
                "1": "around the beginning of function 'countBits'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4"
            },
            "types": {
                "ans": "*",
                "ind#0": "int",
                "i": "*",
                "iter#0": "int"
            }
        }
    }
}
```

</details>

