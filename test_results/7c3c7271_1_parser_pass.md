# Test Report

Time: 2024-04-14 09:21 PM

### Base Program

```py
def multiply(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
```

## Test Case 1

### Modified Program

```py
def multiply(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def multiply(a, b):\n    result = 0\n    while b > 0:\n        result += a\n        b -= 1\n    return result"
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
        "multiply": {
            "name": "multiply",
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
                        "val0": "result",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "0",
                                "line": 2
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
                                    "name": "b",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "0",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 3,
                                        "tokentype": "Constant"
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
                            "name": "result",
                            "primed": false,
                            "line": 6,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 6
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "a",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "a",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "b",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "b",
                                    "primed": false,
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
                        "valueArray": [
                            "b",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "b",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "b",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 5
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
                "1": "around the beginning of function 'multiply'",
                "2": "the condition of the 'while' loop at line 3",
                "3": "*after* the 'while' loop starting at line 3",
                "4": "inside the body of the 'while' loop beginning at line 4"
            },
            "types": {
                "result": "*",
                "b": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def multiply(var_0, var_1):
    result = 0
    while var_1 > 0:
        result += var_0
        var_1 -= 1
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def multiply(var_0, var_1):\n    result = 0\n    while var_1 > 0:\n        result += var_0\n        var_1 -= 1\n    return result"
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
        "multiply": {
            "name": "multiply",
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
                },
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
                        "val0": "result",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "0",
                                "line": 2
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
                                    "name": "var_1",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "0",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 3,
                                        "tokentype": "Constant"
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
                            "name": "result",
                            "primed": false,
                            "line": 6,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 6
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
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
                        "valueArray": [
                            "result",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "var_1",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "var_1",
                                    "primed": false,
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
                        "valueArray": [
                            "var_1",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "var_1",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 5
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
                "1": "around the beginning of function 'multiply'",
                "2": "the condition of the 'while' loop at line 3",
                "3": "*after* the 'while' loop starting at line 3",
                "4": "inside the body of the 'while' loop beginning at line 4"
            },
            "types": {
                "result": "*",
                "var_1": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def multiply(var_2, var_3):
    result = 0
    while var_3 > 0:
        result += var_2
        var_3 -= 1
    return result
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def multiply(var_2, var_3):\n    result = 0\n    while var_3 > 0:\n        result += var_2\n        var_3 -= 1\n    return result"
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
        "multiply": {
            "name": "multiply",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_2",
                    "val1": "*",
                    "valueArray": [
                        "var_2",
                        "*"
                    ],
                    "valueList": [
                        "var_2",
                        "*"
                    ]
                },
                {
                    "val0": "var_3",
                    "val1": "*",
                    "valueArray": [
                        "var_3",
                        "*"
                    ],
                    "valueList": [
                        "var_3",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "result",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "result",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "value": "0",
                                "line": 2
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
                                    "name": "var_3",
                                    "primed": false,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "0",
                                    "line": 3,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 3,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "0",
                                        "line": 3,
                                        "tokentype": "Constant"
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
                            "name": "result",
                            "primed": false,
                            "line": 6,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "result",
                                "primed": false,
                                "line": 6
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "result",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "result",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_2",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "result",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "result",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "result",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "var_3",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "var_3",
                                    "primed": false,
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
                        "valueArray": [
                            "var_3",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "var_3",
                            {
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 5,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 5
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
                "1": "around the beginning of function 'multiply'",
                "2": "the condition of the 'while' loop at line 3",
                "3": "*after* the 'while' loop starting at line 3",
                "4": "inside the body of the 'while' loop beginning at line 4"
            },
            "types": {
                "result": "*",
                "var_3": "*"
            }
        }
    }
}
```

</details>

