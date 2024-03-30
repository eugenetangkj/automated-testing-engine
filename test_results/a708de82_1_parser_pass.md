# Test Report

Time: 2024-03-30 08:41:19.291682

### Base Program

```py
def sum_of_divisors_with_four_divisors(nums):
    total_sum = 0

    for num in nums:
        div_count = 0
        div_sum = 0

        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                div_sum += i
                div_count += 1

                if num // i != i:
                    div_sum += num // i
                    div_count += 1

            if div_count > 4:
                break

        if div_count == 4:
            total_sum += div_sum

    return total_sum
```

## Test Case 1

### Modified Program

```py
def sum_of_divisors_with_four_divisors(nums):
    total_sum = 0
    for num in nums:
        div_count = 0
        div_sum = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                div_sum += i
                div_count += 1
                if num // i != i:
                    div_sum += num // i
                    div_count += 1
            if div_count > 4:
                break
        if div_count == 4:
            total_sum += div_sum
    return total_sum
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def sum_of_divisors_with_four_divisors(nums):\n    total_sum = 0\n    for num in nums:\n        div_count = 0\n        div_sum = 0\n        for i in range(1, int(num ** 0.5) + 1):\n            if num % i == 0:\n                div_sum += i\n                div_count += 1\n                if num // i != i:\n                    div_sum += num // i\n                    div_count += 1\n            if div_count > 4:\n                break\n        if div_count == 4:\n            total_sum += div_sum\n    return total_sum"
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
        "sum_of_divisors_with_four_divisors": {
            "name": "sum_of_divisors_with_four_divisors",
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "total_sum",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "total_sum",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "total_sum",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "nums",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "nums",
                                "primed": false,
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
                            "name": "total_sum",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "total_sum",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "total_sum",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "num",
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
                            "num",
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
                            "num",
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
                        "val0": "div_count",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "div_count",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "div_count",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "div_sum",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "div_sum",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "div_sum",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "int",
                                            "args": [
                                                {
                                                    "name": "Pow",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "0.5",
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
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Pow",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0.5",
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
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Pow",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0.5",
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
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    }
                ],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
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
                "6": [
                    {
                        "val0": "total_sum",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "div_count",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "4",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "total_sum",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "div_sum",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "total_sum",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "total_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "div_count",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "4",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "total_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "div_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "total_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "total_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "div_count",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "4",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "total_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "div_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "total_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                    },
                    {
                        "val0": "div_sum",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "Mod",
                                            "args": [
                                                {
                                                    "name": "num",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "name": "div_sum",
                                                            "primed": false,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 8,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "div_sum",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 8,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "div_sum",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "div_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_sum",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_sum",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "div_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_sum",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_sum",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_sum",
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
                        "val0": "div_count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "Mod",
                                            "args": [
                                                {
                                                    "name": "num",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "name": "div_count",
                                                            "primed": false,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "1",
                                                            "line": 9,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 12,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "div_count",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 9,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "div_count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "div_count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_count",
                                                                "primed": false,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 9,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 12,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_count",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 9,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "div_count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_count",
                                                                "primed": false,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 9,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 12,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_count",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 9,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "14": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "div_count",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "4",
                                    "line": 13,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "4",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "4",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ],
                "15": [],
                "17": []
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
                    "false": 6,
                    "true": 7
                },
                "6": {
                    "true": 2
                },
                "7": {
                    "true": 14
                },
                "14": {
                    "false": 17,
                    "true": 15
                },
                "15": {
                    "true": 6
                },
                "17": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'sum_of_divisors_with_four_divisors'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 6",
                "6": "*after* the 'for' loop starting at line 6",
                "7": "inside the body of the 'for' loop beginning at line 7",
                "14": "the condition of the if-statement at line 13",
                "15": "inside the if-branch starting at line 14",
                "17": "after the if-statement beginning at line 13"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "num": "*",
                "div_count": "*",
                "iter#1": "int",
                "i": "*",
                "iter#0": "int",
                "div_sum": "*",
                "total_sum": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def sum_of_divisors_with_four_divisors(var_0):
    total_sum = 0
    for num in var_0:
        div_count = 0
        div_sum = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                div_sum += i
                div_count += 1
                if num // i != i:
                    div_sum += num // i
                    div_count += 1
            if div_count > 4:
                break
        if div_count == 4:
            total_sum += div_sum
    return total_sum
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def sum_of_divisors_with_four_divisors(var_0):\n    total_sum = 0\n    for num in var_0:\n        div_count = 0\n        div_sum = 0\n        for i in range(1, int(num ** 0.5) + 1):\n            if num % i == 0:\n                div_sum += i\n                div_count += 1\n                if num // i != i:\n                    div_sum += num // i\n                    div_count += 1\n            if div_count > 4:\n                break\n        if div_count == 4:\n            total_sum += div_sum\n    return total_sum"
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
        "sum_of_divisors_with_four_divisors": {
            "name": "sum_of_divisors_with_four_divisors",
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
                        "val0": "total_sum",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "total_sum",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "total_sum",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_0",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_0",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_0",
                                "primed": false,
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
                            "name": "total_sum",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "total_sum",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "total_sum",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "num",
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
                            "num",
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
                            "num",
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
                        "val0": "div_count",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "div_count",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "div_count",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "div_sum",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "div_sum",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "div_sum",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "name": "int",
                                            "args": [
                                                {
                                                    "name": "Pow",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "0.5",
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
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Pow",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0.5",
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
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Pow",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0.5",
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
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    }
                ],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
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
                "6": [
                    {
                        "val0": "total_sum",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "div_count",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "4",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "total_sum",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "div_sum",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "total_sum",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "total_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "div_count",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "4",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "total_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "div_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "total_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "total_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "div_count",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "4",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "total_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "div_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "total_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                    },
                    {
                        "val0": "div_sum",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "Mod",
                                            "args": [
                                                {
                                                    "name": "num",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "name": "div_sum",
                                                            "primed": false,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 8,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "div_sum",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 8,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "div_sum",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "div_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_sum",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_sum",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "div_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_sum",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_sum",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_sum",
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
                        "val0": "div_count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "Mod",
                                            "args": [
                                                {
                                                    "name": "num",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "name": "div_count",
                                                            "primed": false,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "1",
                                                            "line": 9,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 12,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "div_count",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 9,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "div_count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "div_count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_count",
                                                                "primed": false,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 9,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 12,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_count",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 9,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "div_count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_count",
                                                                "primed": false,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 9,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 12,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_count",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 9,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "14": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "div_count",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "4",
                                    "line": 13,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "4",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "4",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ],
                "15": [],
                "17": []
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
                    "false": 6,
                    "true": 7
                },
                "6": {
                    "true": 2
                },
                "7": {
                    "true": 14
                },
                "14": {
                    "false": 17,
                    "true": 15
                },
                "15": {
                    "true": 6
                },
                "17": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'sum_of_divisors_with_four_divisors'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 6",
                "6": "*after* the 'for' loop starting at line 6",
                "7": "inside the body of the 'for' loop beginning at line 7",
                "14": "the condition of the if-statement at line 13",
                "15": "inside the if-branch starting at line 14",
                "17": "after the if-statement beginning at line 13"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "num": "*",
                "div_count": "*",
                "iter#1": "int",
                "i": "*",
                "iter#0": "int",
                "div_sum": "*",
                "total_sum": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def sum_of_divisors_with_four_divisors(nums):
    total_sum = 0
    for num in nums:
        div_count = 0
        div_sum = 0
        for i in range(1, 1 + int(num ** 0.5)):
            if num % i == 0:
                div_sum += i
                div_count += 1
                if num // i != i:
                    div_sum += num // i
                    div_count += 1
            if div_count > 4:
                break
        if div_count == 4:
            total_sum += div_sum
    return total_sum
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def sum_of_divisors_with_four_divisors(nums):\n    total_sum = 0\n    for num in nums:\n        div_count = 0\n        div_sum = 0\n        for i in range(1, 1 + int(num ** 0.5)):\n            if num % i == 0:\n                div_sum += i\n                div_count += 1\n                if num // i != i:\n                    div_sum += num // i\n                    div_count += 1\n            if div_count > 4:\n                break\n        if div_count == 4:\n            total_sum += div_sum\n    return total_sum"
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
        "sum_of_divisors_with_four_divisors": {
            "name": "sum_of_divisors_with_four_divisors",
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
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "total_sum",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "total_sum",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "total_sum",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "nums",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "nums",
                                "primed": false,
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
                            "name": "total_sum",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "total_sum",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "total_sum",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "num",
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
                            "num",
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
                            "num",
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
                        "val0": "div_count",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "div_count",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "div_count",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "div_sum",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "div_sum",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "div_sum",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 6,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "int",
                                            "args": [
                                                {
                                                    "name": "Pow",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "0.5",
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 6,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Pow",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0.5",
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 6,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Pow",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0.5",
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
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    }
                ],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
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
                "6": [
                    {
                        "val0": "total_sum",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "div_count",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "4",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "total_sum",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "div_sum",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "total_sum",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "total_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "div_count",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "4",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "total_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "div_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "total_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "total_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "div_count",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "4",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "total_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "div_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "total_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                    },
                    {
                        "val0": "div_sum",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "Mod",
                                            "args": [
                                                {
                                                    "name": "num",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "name": "div_sum",
                                                            "primed": false,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 8,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "div_sum",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 8,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "div_sum",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "div_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_sum",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_sum",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "div_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_sum",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_sum",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_sum",
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
                        "val0": "div_count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "Mod",
                                            "args": [
                                                {
                                                    "name": "num",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "name": "div_count",
                                                            "primed": false,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "1",
                                                            "line": 9,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 12,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "div_count",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 9,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "div_count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "div_count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_count",
                                                                "primed": false,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 9,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 12,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_count",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 9,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "div_count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_count",
                                                                "primed": false,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 9,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 12,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_count",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 9,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "14": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "div_count",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "4",
                                    "line": 13,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "4",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "4",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ],
                "15": [],
                "17": []
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
                    "false": 6,
                    "true": 7
                },
                "6": {
                    "true": 2
                },
                "7": {
                    "true": 14
                },
                "14": {
                    "false": 17,
                    "true": 15
                },
                "15": {
                    "true": 6
                },
                "17": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'sum_of_divisors_with_four_divisors'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 6",
                "6": "*after* the 'for' loop starting at line 6",
                "7": "inside the body of the 'for' loop beginning at line 7",
                "14": "the condition of the if-statement at line 13",
                "15": "inside the if-branch starting at line 14",
                "17": "after the if-statement beginning at line 13"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "num": "*",
                "div_count": "*",
                "iter#1": "int",
                "i": "*",
                "iter#0": "int",
                "div_sum": "*",
                "total_sum": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def sum_of_divisors_with_four_divisors(var_1):
    total_sum = 0
    for num in var_1:
        div_count = 0
        div_sum = 0
        for i in range(1, 1 + int(num ** 0.5)):
            if num % i == 0:
                div_sum += i
                div_count += 1
                if num // i != i:
                    div_sum += num // i
                    div_count += 1
            if div_count > 4:
                break
        if div_count == 4:
            total_sum += div_sum
    return total_sum
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def sum_of_divisors_with_four_divisors(var_1):\n    total_sum = 0\n    for num in var_1:\n        div_count = 0\n        div_sum = 0\n        for i in range(1, 1 + int(num ** 0.5)):\n            if num % i == 0:\n                div_sum += i\n                div_count += 1\n                if num // i != i:\n                    div_sum += num // i\n                    div_count += 1\n            if div_count > 4:\n                break\n        if div_count == 4:\n            total_sum += div_sum\n    return total_sum"
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
        "sum_of_divisors_with_four_divisors": {
            "name": "sum_of_divisors_with_four_divisors",
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
                        "val0": "total_sum",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "total_sum",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "total_sum",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_1",
                            "primed": false,
                            "line": 3,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
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
                            "name": "total_sum",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "total_sum",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "total_sum",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "num",
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
                            "num",
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
                            "num",
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
                        "val0": "div_count",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "div_count",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "div_count",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "div_sum",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "div_sum",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "div_sum",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "1",
                                    "line": 6,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "Add",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 6,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "int",
                                            "args": [
                                                {
                                                    "name": "Pow",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "0.5",
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 6,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Pow",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0.5",
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
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "1",
                                        "line": 6,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "Add",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 6,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "int",
                                                "args": [
                                                    {
                                                        "name": "Pow",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "0.5",
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
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    }
                ],
                "5": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
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
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
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
                "6": [
                    {
                        "val0": "total_sum",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "div_count",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "4",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "total_sum",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "div_sum",
                                            "primed": false,
                                            "line": 16,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 16,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "total_sum",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "total_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "div_count",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "4",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "total_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "div_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "total_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "total_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "div_count",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "4",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "total_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "div_sum",
                                                "primed": false,
                                                "line": 16,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 16,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "total_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ],
                "7": [
                    {
                        "val0": "i",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 6,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "i",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                    },
                    {
                        "val0": "div_sum",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "Mod",
                                            "args": [
                                                {
                                                    "name": "num",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "name": "div_sum",
                                                            "primed": false,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 8,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 8,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 11,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "div_sum",
                                                    "primed": false,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 8,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 8,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "div_sum",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "div_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_sum",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_sum",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_sum",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "div_sum",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_sum",
                                                                "primed": false,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 8,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 8,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 11,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_sum",
                                                        "primed": false,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 8,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 8,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_sum",
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
                        "val0": "div_count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Eq",
                                    "args": [
                                        {
                                            "name": "Mod",
                                            "args": [
                                                {
                                                    "name": "num",
                                                    "primed": false,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 7,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 7,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "0",
                                            "line": 7,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "NotEq",
                                            "args": [
                                                {
                                                    "name": "FloorDiv",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "AssAdd",
                                                    "args": [
                                                        {
                                                            "name": "div_count",
                                                            "primed": false,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "value": "1",
                                                            "line": 9,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 12,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "div_count",
                                                    "primed": false,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 9,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "div_count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "div_count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_count",
                                                                "primed": false,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 9,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 12,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_count",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 9,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "div_count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "Mod",
                                                "args": [
                                                    {
                                                        "name": "num",
                                                        "primed": false,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 7,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 7,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "0",
                                                "line": 7,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "NotEq",
                                                "args": [
                                                    {
                                                        "name": "FloorDiv",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "AssAdd",
                                                        "args": [
                                                            {
                                                                "name": "div_count",
                                                                "primed": false,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 9,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 12,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "div_count",
                                                        "primed": false,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 9,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "14": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Gt",
                            "args": [
                                {
                                    "name": "div_count",
                                    "primed": false,
                                    "line": 13,
                                    "tokentype": "Variable"
                                },
                                {
                                    "value": "4",
                                    "line": 13,
                                    "tokentype": "Constant"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "4",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Gt",
                                "args": [
                                    {
                                        "name": "div_count",
                                        "primed": false,
                                        "line": 13,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "4",
                                        "line": 13,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ],
                "15": [],
                "17": []
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
                    "false": 6,
                    "true": 7
                },
                "6": {
                    "true": 2
                },
                "7": {
                    "true": 14
                },
                "14": {
                    "false": 17,
                    "true": 15
                },
                "15": {
                    "true": 6
                },
                "17": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'sum_of_divisors_with_four_divisors'",
                "2": "the condition of the 'for' loop at line 3",
                "3": "*after* the 'for' loop starting at line 3",
                "4": "inside the body of the 'for' loop beginning at line 4",
                "5": "the condition of the 'for' loop at line 6",
                "6": "*after* the 'for' loop starting at line 6",
                "7": "inside the body of the 'for' loop beginning at line 7",
                "14": "the condition of the if-statement at line 13",
                "15": "inside the if-branch starting at line 14",
                "17": "after the if-statement beginning at line 13"
            },
            "types": {
                "ind#1": "int",
                "ind#0": "int",
                "num": "*",
                "div_count": "*",
                "iter#1": "int",
                "i": "*",
                "iter#0": "int",
                "div_sum": "*",
                "total_sum": "*"
            }
        }
    }
}
```

</details>

