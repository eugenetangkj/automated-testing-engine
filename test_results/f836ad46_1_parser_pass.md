# Test Report

Time: 2024-03-30 08:57:46.553661

### Base Program

```py
def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count
```

## Test Case 1

### Modified Program

```py
def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i - 1] - 1:
            while i < len(prices) and prices[i] == prices[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def smooth_descent_periods(prices):\n    count = 0\n    i = 1\n    while i < len(prices):\n        if prices[i] == prices[i - 1] - 1:\n            while i < len(prices) and prices[i] == prices[i - 1] - 1:\n                i += 1\n            count += 1\n        else:\n            i += 1\n    return count"
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
        "smooth_descent_periods": {
            "name": "smooth_descent_periods",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "prices",
                    "val1": "*",
                    "valueArray": [
                        "prices",
                        "*"
                    ],
                    "valueList": [
                        "prices",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "1",
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "prices",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "prices",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "prices",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "count",
                            "primed": false,
                            "line": 11,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 11
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "prices",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "prices",
                                                    "primed": false,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Sub",
                                                    "args": [
                                                        {
                                                            "name": "i",
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
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "prices",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Sub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "prices",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Sub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 5
                            }
                        ]
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "And",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "prices",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "prices",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "prices",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "i",
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
                                                        }
                                                    ],
                                                    "line": 6,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "prices",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
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
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "prices",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
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
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "count",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 7,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "10": [],
                "11": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
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
                    "true": 5
                },
                "5": {
                    "false": 11,
                    "true": 6
                },
                "6": {
                    "true": 7
                },
                "7": {
                    "false": 8,
                    "true": 9
                },
                "8": {
                    "true": 10
                },
                "9": {
                    "true": 7
                },
                "10": {
                    "true": 2
                },
                "11": {
                    "true": 10
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'smooth_descent_periods'",
                "2": "the condition of the 'while' loop at line 4",
                "3": "*after* the 'while' loop starting at line 4",
                "4": "inside the body of the 'while' loop beginning at line 5",
                "5": "the condition of the if-statement at line 5",
                "6": "inside the if-branch starting at line 6",
                "7": "the condition of the 'while' loop at line 6",
                "8": "*after* the 'while' loop starting at line 6",
                "9": "inside the body of the 'while' loop beginning at line 7",
                "10": "after the if-statement beginning at line 5",
                "11": "inside the else-branch starting at line 10"
            },
            "types": {
                "count": "*",
                "i": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def smooth_descent_periods(var_0):
    count = 0
    i = 1
    while i < len(var_0):
        if var_0[i] == var_0[i - 1] - 1:
            while i < len(var_0) and var_0[i] == var_0[i - 1] - 1:
                i += 1
            count += 1
        else:
            i += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def smooth_descent_periods(var_0):\n    count = 0\n    i = 1\n    while i < len(var_0):\n        if var_0[i] == var_0[i - 1] - 1:\n            while i < len(var_0) and var_0[i] == var_0[i - 1] - 1:\n                i += 1\n            count += 1\n        else:\n            i += 1\n    return count"
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
        "smooth_descent_periods": {
            "name": "smooth_descent_periods",
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
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "1",
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "count",
                            "primed": false,
                            "line": 11,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 11
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_0",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Sub",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Sub",
                                                    "args": [
                                                        {
                                                            "name": "i",
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
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
                                        },
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Sub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Sub",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Sub",
                                                        "args": [
                                                            {
                                                                "name": "i",
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
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
                                            },
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
                                "line": 5
                            }
                        ]
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "And",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_0",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "i",
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
                                                        }
                                                    ],
                                                    "line": 6,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 6,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
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
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
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
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 6,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "count",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 7,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "10": [],
                "11": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
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
                    "true": 5
                },
                "5": {
                    "false": 11,
                    "true": 6
                },
                "6": {
                    "true": 7
                },
                "7": {
                    "false": 8,
                    "true": 9
                },
                "8": {
                    "true": 10
                },
                "9": {
                    "true": 7
                },
                "10": {
                    "true": 2
                },
                "11": {
                    "true": 10
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'smooth_descent_periods'",
                "2": "the condition of the 'while' loop at line 4",
                "3": "*after* the 'while' loop starting at line 4",
                "4": "inside the body of the 'while' loop beginning at line 5",
                "5": "the condition of the if-statement at line 5",
                "6": "inside the if-branch starting at line 6",
                "7": "the condition of the 'while' loop at line 6",
                "8": "*after* the 'while' loop starting at line 6",
                "9": "inside the body of the 'while' loop beginning at line 7",
                "10": "after the if-statement beginning at line 5",
                "11": "inside the else-branch starting at line 10"
            },
            "types": {
                "count": "*",
                "i": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def smooth_descent_periods(prices):
    count = 0
    i = 1
    while i < len(prices):
        if prices[i] == prices[i + -1] + -1:
            while i < len(prices) and prices[i] == prices[i + -1] + -1:
                i += 1
            count += 1
        else:
            i += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def smooth_descent_periods(prices):\n    count = 0\n    i = 1\n    while i < len(prices):\n        if prices[i] == prices[i + -1] + -1:\n            while i < len(prices) and prices[i] == prices[i + -1] + -1:\n                i += 1\n            count += 1\n        else:\n            i += 1\n    return count"
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
        "smooth_descent_periods": {
            "name": "smooth_descent_periods",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "prices",
                    "val1": "*",
                    "valueArray": [
                        "prices",
                        "*"
                    ],
                    "valueList": [
                        "prices",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "1",
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "prices",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "prices",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "prices",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "count",
                            "primed": false,
                            "line": 11,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 11
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "prices",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "prices",
                                                    "primed": false,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": false,
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
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
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
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "prices",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": false,
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
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
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
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "prices",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": false,
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
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
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
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "And",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "prices",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "prices",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "prices",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 6,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
                                                                            "line": 6,
                                                                            "tokentype": "Constant"
                                                                        }
                                                                    ],
                                                                    "line": 6,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 6,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 6,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 6,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 6,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "prices",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 6,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 6,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 6,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "prices",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "prices",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 6,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 6,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 6,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "count",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 7,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "10": [],
                "11": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
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
                    "true": 5
                },
                "5": {
                    "false": 11,
                    "true": 6
                },
                "6": {
                    "true": 7
                },
                "7": {
                    "false": 8,
                    "true": 9
                },
                "8": {
                    "true": 10
                },
                "9": {
                    "true": 7
                },
                "10": {
                    "true": 2
                },
                "11": {
                    "true": 10
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'smooth_descent_periods'",
                "2": "the condition of the 'while' loop at line 4",
                "3": "*after* the 'while' loop starting at line 4",
                "4": "inside the body of the 'while' loop beginning at line 5",
                "5": "the condition of the if-statement at line 5",
                "6": "inside the if-branch starting at line 6",
                "7": "the condition of the 'while' loop at line 6",
                "8": "*after* the 'while' loop starting at line 6",
                "9": "inside the body of the 'while' loop beginning at line 7",
                "10": "after the if-statement beginning at line 5",
                "11": "inside the else-branch starting at line 10"
            },
            "types": {
                "count": "*",
                "i": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def smooth_descent_periods(var_1):
    count = 0
    i = 1
    while i < len(var_1):
        if var_1[i] == var_1[i + -1] + -1:
            while i < len(var_1) and var_1[i] == var_1[i + -1] + -1:
                i += 1
            count += 1
        else:
            i += 1
    return count
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def smooth_descent_periods(var_1):\n    count = 0\n    i = 1\n    while i < len(var_1):\n        if var_1[i] == var_1[i + -1] + -1:\n            while i < len(var_1) and var_1[i] == var_1[i + -1] + -1:\n                i += 1\n            count += 1\n        else:\n            i += 1\n    return count"
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
        "smooth_descent_periods": {
            "name": "smooth_descent_periods",
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
                        "val0": "count",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "count",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "i",
                        "val1": {
                            "value": "1",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "i",
                            {
                                "value": "1",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "value": "1",
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
                                    "name": "i",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
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
                ],
                "3": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "count",
                            "primed": false,
                            "line": 11,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "count",
                                "primed": false,
                                "line": 11
                            }
                        ]
                    }
                ],
                "4": [],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Eq",
                            "args": [
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "var_1",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 5,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 5,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_1",
                                                    "primed": false,
                                                    "line": 5,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": false,
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
                                                }
                                            ],
                                            "line": 5,
                                            "tokentype": "Operation"
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
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": false,
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
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
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
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Eq",
                                "args": [
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "var_1",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 5,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 5,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 5,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": false,
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
                                                    }
                                                ],
                                                "line": 5,
                                                "tokentype": "Operation"
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
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "And",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_1",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_1",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "var_1",
                                                            "primed": false,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 6,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
                                                                            "line": 6,
                                                                            "tokentype": "Constant"
                                                                        }
                                                                    ],
                                                                    "line": 6,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 6,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 6,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 6,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 6,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 6,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 6,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 6,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 6,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "And",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_1",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 6,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 6,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 6,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 6,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 6,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 6,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 6,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "count",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 8,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 7,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 7,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "10": [],
                "11": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "AssAdd",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": false,
                                    "line": 10,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "1",
                                    "line": 10,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "AssAdd",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": false,
                                        "line": 10,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 10,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 10
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
                    "true": 5
                },
                "5": {
                    "false": 11,
                    "true": 6
                },
                "6": {
                    "true": 7
                },
                "7": {
                    "false": 8,
                    "true": 9
                },
                "8": {
                    "true": 10
                },
                "9": {
                    "true": 7
                },
                "10": {
                    "true": 2
                },
                "11": {
                    "true": 10
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'smooth_descent_periods'",
                "2": "the condition of the 'while' loop at line 4",
                "3": "*after* the 'while' loop starting at line 4",
                "4": "inside the body of the 'while' loop beginning at line 5",
                "5": "the condition of the if-statement at line 5",
                "6": "inside the if-branch starting at line 6",
                "7": "the condition of the 'while' loop at line 6",
                "8": "*after* the 'while' loop starting at line 6",
                "9": "inside the body of the 'while' loop beginning at line 7",
                "10": "after the if-statement beginning at line 5",
                "11": "inside the else-branch starting at line 10"
            },
            "types": {
                "count": "*",
                "i": "*"
            }
        }
    }
}
```

</details>

