# Test Report

Time: 2024-03-30 06:13:42.442672

### Base Program

```py
def count_odds(low, high):
    return (high + 1) // 2 - low // 2
```

## Test Case 1

### Modified Program

```py
def count_odds(low, high):
    return (high + 1) // 2 - low // 2
```

<details>
<summary>parser endpoint: passed ✅</summary>

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "source_code": "def count_odds(low, high):\n    return (high + 1) // 2 - low // 2"
}
```

Actual Output: 
```json
{
    "importStatements": [],
    "fncs": {
        "count_odds": {
            "name": "count_odds",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "low",
                    "val1": "*",
                    "valueArray": [
                        "low",
                        "*"
                    ],
                    "valueList": [
                        "low",
                        "*"
                    ]
                },
                {
                    "val0": "high",
                    "val1": "*",
                    "valueArray": [
                        "high",
                        "*"
                    ],
                    "valueList": [
                        "high",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "FloorDiv",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "high",
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
                                        },
                                        {
                                            "value": "2",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "FloorDiv",
                                    "args": [
                                        {
                                            "name": "low",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "2",
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
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "FloorDiv",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "high",
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
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "FloorDiv",
                                        "args": [
                                            {
                                                "name": "low",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "2",
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
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "FloorDiv",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "high",
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
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "FloorDiv",
                                        "args": [
                                            {
                                                "name": "low",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "2",
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
                "1": "around the beginning of function 'count_odds'"
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
def count_odds(var_0, var_1):
    return (var_1 + 1) // 2 - var_0 // 2
```

<details>
<summary>parser endpoint: passed ✅</summary>

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "source_code": "def count_odds(var_0, var_1):\n    return (var_1 + 1) // 2 - var_0 // 2"
}
```

Actual Output: 
```json
{
    "importStatements": [],
    "fncs": {
        "count_odds": {
            "name": "count_odds",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "Sub",
                            "args": [
                                {
                                    "name": "FloorDiv",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "var_1",
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
                                        },
                                        {
                                            "value": "2",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "FloorDiv",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "2",
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
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "FloorDiv",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "var_1",
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
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "FloorDiv",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "2",
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
                                "name": "Sub",
                                "args": [
                                    {
                                        "name": "FloorDiv",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "var_1",
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
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "FloorDiv",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "2",
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
                "1": "around the beginning of function 'count_odds'"
            },
            "types": {}
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def count_odds(low, high):
    return (1 + high) // 2 + -(low // 2)
```

<details>
<summary>parser endpoint: passed ✅</summary>

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "source_code": "def count_odds(low, high):\n    return (1 + high) // 2 + -(low // 2)"
}
```

Actual Output: 
```json
{
    "importStatements": [],
    "fncs": {
        "count_odds": {
            "name": "count_odds",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "low",
                    "val1": "*",
                    "valueArray": [
                        "low",
                        "*"
                    ],
                    "valueList": [
                        "low",
                        "*"
                    ]
                },
                {
                    "val0": "high",
                    "val1": "*",
                    "valueArray": [
                        "high",
                        "*"
                    ],
                    "valueList": [
                        "high",
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
                                    "name": "FloorDiv",
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
                                                    "name": "high",
                                                    "primed": false,
                                                    "line": 2,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "2",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "name": "FloorDiv",
                                            "args": [
                                                {
                                                    "name": "low",
                                                    "primed": false,
                                                    "line": 2,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "2",
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
                                        "name": "FloorDiv",
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
                                                        "name": "high",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "FloorDiv",
                                                "args": [
                                                    {
                                                        "name": "low",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "2",
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
                                        "name": "FloorDiv",
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
                                                        "name": "high",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "FloorDiv",
                                                "args": [
                                                    {
                                                        "name": "low",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "2",
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
                "1": "around the beginning of function 'count_odds'"
            },
            "types": {}
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def count_odds(var_2, var_3):
    return (1 + var_3) // 2 + -(var_2 // 2)
```

<details>
<summary>parser endpoint: passed ✅</summary>

Message: 
```
Success
```

Request Body: 
```json
{
    "language": "py",
    "source_code": "def count_odds(var_2, var_3):\n    return (1 + var_3) // 2 + -(var_2 // 2)"
}
```

Actual Output: 
```json
{
    "importStatements": [],
    "fncs": {
        "count_odds": {
            "name": "count_odds",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "FloorDiv",
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
                                                    "name": "var_3",
                                                    "primed": false,
                                                    "line": 2,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 2,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "2",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "name": "FloorDiv",
                                            "args": [
                                                {
                                                    "name": "var_2",
                                                    "primed": false,
                                                    "line": 2,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "2",
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
                                        "name": "FloorDiv",
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
                                                        "name": "var_3",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "FloorDiv",
                                                "args": [
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "2",
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
                                        "name": "FloorDiv",
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
                                                        "name": "var_3",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 2,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "2",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "name": "FloorDiv",
                                                "args": [
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 2,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "2",
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
                "1": "around the beginning of function 'count_odds'"
            },
            "types": {}
        }
    }
}
```

</details>

