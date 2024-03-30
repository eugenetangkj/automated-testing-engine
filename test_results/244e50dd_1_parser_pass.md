# Test Report

Time: 2024-03-30 08:22:27.192080

### Base Program

```py
def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))
```

## Test Case 1

### Modified Program

```py
def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(max_elem + 1, max_elem + k + 1))
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_append_k_sum(nums, k):\n    max_elem = max(nums)\n    return sum(range(max_elem + 1, max_elem + k + 1))"
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
        "min_append_k_sum": {
            "name": "min_append_k_sum",
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
                    "val0": "k",
                    "val1": "*",
                    "valueArray": [
                        "k",
                        "*"
                    ],
                    "valueList": [
                        "k",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "max_elem",
                        "val1": {
                            "name": "max",
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
                            "max_elem",
                            {
                                "name": "max",
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
                            "max_elem",
                            {
                                "name": "max",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "sum",
                            "args": [
                                {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "max_elem",
                                                    "primed": true,
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
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "max_elem",
                                                            "primed": true,
                                                            "line": 3,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "k",
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
                            "$ret",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "max_elem",
                                                        "primed": true,
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
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "max_elem",
                                                                "primed": true,
                                                                "line": 3,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                            "$ret",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "max_elem",
                                                        "primed": true,
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
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "max_elem",
                                                                "primed": true,
                                                                "line": 3,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'min_append_k_sum'"
            },
            "types": {
                "max_elem": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def min_append_k_sum(var_0, var_1):
    max_elem = max(var_0)
    return sum(range(max_elem + 1, max_elem + var_1 + 1))
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_append_k_sum(var_0, var_1):\n    max_elem = max(var_0)\n    return sum(range(max_elem + 1, max_elem + var_1 + 1))"
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
        "min_append_k_sum": {
            "name": "min_append_k_sum",
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
                        "val0": "max_elem",
                        "val1": {
                            "name": "max",
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
                            "max_elem",
                            {
                                "name": "max",
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
                            "max_elem",
                            {
                                "name": "max",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "sum",
                            "args": [
                                {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "max_elem",
                                                    "primed": true,
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
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "max_elem",
                                                            "primed": true,
                                                            "line": 3,
                                                            "tokentype": "Variable"
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
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "max_elem",
                                                        "primed": true,
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
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "max_elem",
                                                                "primed": true,
                                                                "line": 3,
                                                                "tokentype": "Variable"
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
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "max_elem",
                                                        "primed": true,
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
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "max_elem",
                                                                "primed": true,
                                                                "line": 3,
                                                                "tokentype": "Variable"
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
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'min_append_k_sum'"
            },
            "types": {
                "max_elem": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def min_append_k_sum(nums, k):
    max_elem = max(nums)
    return sum(range(1 + max_elem, max_elem + 1 + k))
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_append_k_sum(nums, k):\n    max_elem = max(nums)\n    return sum(range(1 + max_elem, max_elem + 1 + k))"
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
        "min_append_k_sum": {
            "name": "min_append_k_sum",
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
                    "val0": "k",
                    "val1": "*",
                    "valueArray": [
                        "k",
                        "*"
                    ],
                    "valueList": [
                        "k",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "max_elem",
                        "val1": {
                            "name": "max",
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
                            "max_elem",
                            {
                                "name": "max",
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
                            "max_elem",
                            {
                                "name": "max",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "sum",
                            "args": [
                                {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 3,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "max_elem",
                                                    "primed": true,
                                                    "line": 3,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 3,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "max_elem",
                                                            "primed": true,
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
                                                {
                                                    "name": "k",
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
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "max_elem",
                                                        "primed": true,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "max_elem",
                                                                "primed": true,
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
                                                    {
                                                        "name": "k",
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
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "max_elem",
                                                        "primed": true,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "max_elem",
                                                                "primed": true,
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
                                                    {
                                                        "name": "k",
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
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'min_append_k_sum'"
            },
            "types": {
                "max_elem": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def min_append_k_sum(var_2, var_3):
    max_elem = max(var_2)
    return sum(range(1 + max_elem, max_elem + 1 + var_3))
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_append_k_sum(var_2, var_3):\n    max_elem = max(var_2)\n    return sum(range(1 + max_elem, max_elem + 1 + var_3))"
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
        "min_append_k_sum": {
            "name": "min_append_k_sum",
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
                        "val0": "max_elem",
                        "val1": {
                            "name": "max",
                            "args": [
                                {
                                    "name": "var_2",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "max_elem",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "var_2",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "max_elem",
                            {
                                "name": "max",
                                "args": [
                                    {
                                        "name": "var_2",
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
                        "val0": "$ret",
                        "val1": {
                            "name": "sum",
                            "args": [
                                {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "value": "1",
                                                    "line": 3,
                                                    "tokentype": "Constant"
                                                },
                                                {
                                                    "name": "max_elem",
                                                    "primed": true,
                                                    "line": 3,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 3,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "max_elem",
                                                            "primed": true,
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
                                                {
                                                    "name": "var_3",
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
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "max_elem",
                                                        "primed": true,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "max_elem",
                                                                "primed": true,
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
                                                    {
                                                        "name": "var_3",
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
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "sum",
                                "args": [
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "value": "1",
                                                        "line": 3,
                                                        "tokentype": "Constant"
                                                    },
                                                    {
                                                        "name": "max_elem",
                                                        "primed": true,
                                                        "line": 3,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 3,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "max_elem",
                                                                "primed": true,
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
                                                    {
                                                        "name": "var_3",
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
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {}
            },
            "locdescs": {
                "1": "around the beginning of function 'min_append_k_sum'"
            },
            "types": {
                "max_elem": "*"
            }
        }
    }
}
```

</details>

