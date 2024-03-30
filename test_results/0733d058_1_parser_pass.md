# Test Report

Time: 2024-03-30 07:57:16.238375

### Base Program

```py
def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    
    return (diff + limit - 1) // limit
```

## Test Case 1

### Modified Program

```py
def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal - sum_nums)
    return (diff + limit - 1) // limit
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minElements(nums, limit, goal):\n    sum_nums = sum(nums)\n    diff = abs(goal - sum_nums)\n    return (diff + limit - 1) // limit"
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
        "minElements": {
            "name": "minElements",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "nums",
                    "val1": "*",
                    "valueArray": [
                        "nums",
                        "*"
                    ],
                    "valueList": [
                        "nums",
                        "*"
                    ]
                },
                {
                    "val0": "limit",
                    "val1": "*",
                    "valueArray": [
                        "limit",
                        "*"
                    ],
                    "valueList": [
                        "limit",
                        "*"
                    ]
                },
                {
                    "val0": "goal",
                    "val1": "*",
                    "valueArray": [
                        "goal",
                        "*"
                    ],
                    "valueList": [
                        "goal",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "sum_nums",
                        "val1": {
                            "name": "sum",
                            "args": [
                                {
                                    "name": "nums",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "sum_nums",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "nums",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "sum_nums",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "nums",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "diff",
                        "val1": {
                            "name": "abs",
                            "args": [
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "goal",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "sum_nums",
                                            "primed": true,
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
                            "diff",
                            {
                                "name": "abs",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "goal",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "sum_nums",
                                                "primed": true,
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
                            "diff",
                            {
                                "name": "abs",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "goal",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "sum_nums",
                                                "primed": true,
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
                        "val0": "$ret",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "diff",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "limit",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
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
                                },
                                {
                                    "name": "limit",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "diff",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "limit",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "limit",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "diff",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "limit",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
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
                                    },
                                    {
                                        "name": "limit",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'minElements'"
            },
            "types": {
                "diff": "*",
                "sum_nums": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def minElements(var_0, var_1, var_2):
    sum_nums = sum(var_0)
    diff = abs(var_2 - sum_nums)
    return (diff + var_1 - 1) // var_1
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minElements(var_0, var_1, var_2):\n    sum_nums = sum(var_0)\n    diff = abs(var_2 - sum_nums)\n    return (diff + var_1 - 1) // var_1"
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
        "minElements": {
            "name": "minElements",
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
                },
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "sum_nums",
                        "val1": {
                            "name": "sum",
                            "args": [
                                {
                                    "name": "var_0",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "sum_nums",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "sum_nums",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "var_0",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "diff",
                        "val1": {
                            "name": "abs",
                            "args": [
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "var_2",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "sum_nums",
                                            "primed": true,
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
                            "diff",
                            {
                                "name": "abs",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "var_2",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "sum_nums",
                                                "primed": true,
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
                            "diff",
                            {
                                "name": "abs",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "var_2",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "sum_nums",
                                                "primed": true,
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
                        "val0": "$ret",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "diff",
                                                    "primed": true,
                                                    "line": 4,
                                                    "tokentype": "Variable"
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
                                            "value": "1",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
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
                        "valueArray": [
                            "$ret",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "diff",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
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
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "diff",
                                                        "primed": true,
                                                        "line": 4,
                                                        "tokentype": "Variable"
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
                                                "value": "1",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_1",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'minElements'"
            },
            "types": {
                "diff": "*",
                "sum_nums": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def minElements(nums, limit, goal):
    sum_nums = sum(nums)
    diff = abs(goal + -sum_nums)
    return (limit + diff + -1) // limit
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minElements(nums, limit, goal):\n    sum_nums = sum(nums)\n    diff = abs(goal + -sum_nums)\n    return (limit + diff + -1) // limit"
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
        "minElements": {
            "name": "minElements",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "nums",
                    "val1": "*",
                    "valueArray": [
                        "nums",
                        "*"
                    ],
                    "valueList": [
                        "nums",
                        "*"
                    ]
                },
                {
                    "val0": "limit",
                    "val1": "*",
                    "valueArray": [
                        "limit",
                        "*"
                    ],
                    "valueList": [
                        "limit",
                        "*"
                    ]
                },
                {
                    "val0": "goal",
                    "val1": "*",
                    "valueArray": [
                        "goal",
                        "*"
                    ],
                    "valueList": [
                        "goal",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "sum_nums",
                        "val1": {
                            "name": "sum",
                            "args": [
                                {
                                    "name": "nums",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "sum_nums",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "nums",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "sum_nums",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "nums",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "diff",
                        "val1": {
                            "name": "abs",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "goal",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "name": "sum_nums",
                                                    "primed": true,
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
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "diff",
                            {
                                "name": "abs",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "goal",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "sum_nums",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "diff",
                            {
                                "name": "abs",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "goal",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "sum_nums",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "limit",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "diff",
                                                    "primed": true,
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
                                {
                                    "name": "limit",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "limit",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "diff",
                                                        "primed": true,
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
                                    {
                                        "name": "limit",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "limit",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "diff",
                                                        "primed": true,
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
                                    {
                                        "name": "limit",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'minElements'"
            },
            "types": {
                "diff": "*",
                "sum_nums": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def minElements(var_3, var_4, var_5):
    sum_nums = sum(var_3)
    diff = abs(var_5 + -sum_nums)
    return (var_4 + diff + -1) // var_4
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def minElements(var_3, var_4, var_5):\n    sum_nums = sum(var_3)\n    diff = abs(var_5 + -sum_nums)\n    return (var_4 + diff + -1) // var_4"
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
        "minElements": {
            "name": "minElements",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
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
                },
                {
                    "val0": "var_4",
                    "val1": "*",
                    "valueArray": [
                        "var_4",
                        "*"
                    ],
                    "valueList": [
                        "var_4",
                        "*"
                    ]
                },
                {
                    "val0": "var_5",
                    "val1": "*",
                    "valueArray": [
                        "var_5",
                        "*"
                    ],
                    "valueList": [
                        "var_5",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "sum_nums",
                        "val1": {
                            "name": "sum",
                            "args": [
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
                        "valueArray": [
                            "sum_nums",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "sum_nums",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "diff",
                        "val1": {
                            "name": "abs",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "var_5",
                                            "primed": false,
                                            "line": 3,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "USub",
                                            "args": [
                                                {
                                                    "name": "sum_nums",
                                                    "primed": true,
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
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "diff",
                            {
                                "name": "abs",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "var_5",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "sum_nums",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "diff",
                            {
                                "name": "abs",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "var_5",
                                                "primed": false,
                                                "line": 3,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "USub",
                                                "args": [
                                                    {
                                                        "name": "sum_nums",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "FloorDiv",
                            "args": [
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "var_4",
                                                    "primed": false,
                                                    "line": 4,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "diff",
                                                    "primed": true,
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
                                {
                                    "name": "var_4",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "var_4",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "diff",
                                                        "primed": true,
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
                                    {
                                        "name": "var_4",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "FloorDiv",
                                "args": [
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "var_4",
                                                        "primed": false,
                                                        "line": 4,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "diff",
                                                        "primed": true,
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
                                    {
                                        "name": "var_4",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'minElements'"
            },
            "types": {
                "diff": "*",
                "sum_nums": "*"
            }
        }
    }
}
```

</details>

