# Test Report

Time: 2024-04-14 11:24:24.133168

### Base Program

```py
def count_routes(locations, start, finish, fuel, curr=None, remaining_fuel=None, memo=None):
    if memo is None:
        memo = {}
     
    if curr is None:
        curr = start
        remaining_fuel = fuel

    if remaining_fuel < 0:
        return 0

    if (curr, remaining_fuel) in memo:
        return memo[(curr, remaining_fuel)]

    ans = 1 if curr == finish else 0
    for next in range(len(locations)):
        if next != curr:
            ans += count_routes(locations, start, finish, fuel, next, remaining_fuel - abs(locations[curr] - locations[next]), memo)
            ans %= 1000000007

    memo[(curr, remaining_fuel)] = ans
    return ans
```

## Test Case 1

### Modified Program

```py
def count_routes(locations, start, finish, fuel, curr=None, remaining_fuel=None, memo=None):
    if memo is None:
        memo = {}
    if curr is None:
        curr = start
        remaining_fuel = fuel
    if remaining_fuel < 0:
        return 0
    if (curr, remaining_fuel) in memo:
        return memo[curr, remaining_fuel]
    ans = 1 if curr == finish else 0
    for next in range(len(locations)):
        if next != curr:
            ans += count_routes(locations, start, finish, fuel, next, remaining_fuel - abs(locations[curr] - locations[next]), memo)
            ans %= 1000000007
    memo[curr, remaining_fuel] = ans
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def count_routes(locations, start, finish, fuel, curr=None, remaining_fuel=None, memo=None):\n    if memo is None:\n        memo = {}\n    if curr is None:\n        curr = start\n        remaining_fuel = fuel\n    if remaining_fuel < 0:\n        return 0\n    if (curr, remaining_fuel) in memo:\n        return memo[curr, remaining_fuel]\n    ans = 1 if curr == finish else 0\n    for next in range(len(locations)):\n        if next != curr:\n            ans += count_routes(locations, start, finish, fuel, next, remaining_fuel - abs(locations[curr] - locations[next]), memo)\n            ans %= 1000000007\n    memo[curr, remaining_fuel] = ans\n    return ans"
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
        "count_routes": {
            "name": "count_routes",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "locations",
                    "val1": "*",
                    "valueArray": [
                        "locations",
                        "*"
                    ],
                    "valueList": [
                        "locations",
                        "*"
                    ]
                },
                {
                    "val0": "start",
                    "val1": "*",
                    "valueArray": [
                        "start",
                        "*"
                    ],
                    "valueList": [
                        "start",
                        "*"
                    ]
                },
                {
                    "val0": "finish",
                    "val1": "*",
                    "valueArray": [
                        "finish",
                        "*"
                    ],
                    "valueList": [
                        "finish",
                        "*"
                    ]
                },
                {
                    "val0": "fuel",
                    "val1": "*",
                    "valueArray": [
                        "fuel",
                        "*"
                    ],
                    "valueList": [
                        "fuel",
                        "*"
                    ]
                },
                {
                    "val0": "curr",
                    "val1": "*",
                    "valueArray": [
                        "curr",
                        "*"
                    ],
                    "valueList": [
                        "curr",
                        "*"
                    ]
                },
                {
                    "val0": "remaining_fuel",
                    "val1": "*",
                    "valueArray": [
                        "remaining_fuel",
                        "*"
                    ],
                    "valueList": [
                        "remaining_fuel",
                        "*"
                    ]
                },
                {
                    "val0": "memo",
                    "val1": "*",
                    "valueArray": [
                        "memo",
                        "*"
                    ],
                    "valueList": [
                        "memo",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "memo",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "memo",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "DictInit",
                                    "args": [],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "memo",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "memo",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "memo",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "DictInit",
                                        "args": [],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "memo",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "memo",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "memo",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "DictInit",
                                        "args": [],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "memo",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "curr",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "curr",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "start",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "curr",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "curr",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "start",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "curr",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "curr",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "start",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "curr",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "remaining_fuel",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "curr",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "fuel",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "remaining_fuel",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "remaining_fuel",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "fuel",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "remaining_fuel",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "remaining_fuel",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "fuel",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "remaining_fuel",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "remaining_fuel",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "curr",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "remaining_fuel",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "memo",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "curr",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "finish",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "originalExpr": {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": true,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "finish",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 11,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "0",
                                        "line": 11,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 11,
                                "tokentype": "Operation"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "curr",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "finish",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11,
                                "originalExpr": {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "curr",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "finish",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "curr",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "finish",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11,
                                "originalExpr": {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "curr",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "finish",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "remaining_fuel",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "curr",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "remaining_fuel",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "memo",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "locations",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "originalExpr": {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "locations",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12,
                                "tokentype": "Operation"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "locations",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "locations",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "locations",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "locations",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "remaining_fuel",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "curr",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "remaining_fuel",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "memo",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "originalExpr": {
                                "value": "0",
                                "line": 12,
                                "tokentype": "Constant"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "remaining_fuel",
                                            "primed": true,
                                            "line": 7,
                                            "tokentype": "Variable"
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
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "In",
                                            "args": [
                                                {
                                                    "name": "TupleInit",
                                                    "args": [
                                                        {
                                                            "name": "curr",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "remaining_fuel",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "memo",
                                                    "primed": true,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "memo",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "remaining_fuel",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "$ret",
                                            "primed": false,
                                            "line": 0,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "remaining_fuel",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
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
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "TupleInit",
                                                        "args": [
                                                            {
                                                                "name": "curr",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "memo",
                                                        "primed": true,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "memo",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "remaining_fuel",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "$ret",
                                                "primed": false,
                                                "line": 0,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "remaining_fuel",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
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
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "TupleInit",
                                                        "args": [
                                                            {
                                                                "name": "curr",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "memo",
                                                        "primed": true,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "memo",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "remaining_fuel",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "$ret",
                                                "primed": false,
                                                "line": 0,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
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
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 12,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 12,
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    }
                ],
                "15": [
                    {
                        "val0": "memo",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "memo",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "remaining_fuel",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 16,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "memo",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "memo",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "remaining_fuel",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "memo",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "memo",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "remaining_fuel",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 16
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "16": [
                    {
                        "val0": "next",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "next",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "next",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                                    "line": 12,
                                    "tokentype": "Variable"
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
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "next",
                                            "primed": true,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "curr",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "ans",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "FuncCall",
                                                    "args": [
                                                        {
                                                            "value": "count_routes",
                                                            "line": 14,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "locations",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "start",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "finish",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "fuel",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "next",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "remaining_fuel",
                                                                    "primed": false,
                                                                    "line": 14,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "abs",
                                                                    "args": [
                                                                        {
                                                                            "name": "Sub",
                                                                            "args": [
                                                                                {
                                                                                    "name": "GetElement",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "locations",
                                                                                            "primed": false,
                                                                                            "line": 14,
                                                                                            "tokentype": "Variable"
                                                                                        },
                                                                                        {
                                                                                            "name": "curr",
                                                                                            "primed": false,
                                                                                            "line": 14,
                                                                                            "tokentype": "Variable"
                                                                                        }
                                                                                    ],
                                                                                    "line": 14,
                                                                                    "tokentype": "Operation"
                                                                                },
                                                                                {
                                                                                    "name": "GetElement",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "locations",
                                                                                            "primed": false,
                                                                                            "line": 14,
                                                                                            "tokentype": "Variable"
                                                                                        },
                                                                                        {
                                                                                            "name": "next",
                                                                                            "primed": true,
                                                                                            "line": 14,
                                                                                            "tokentype": "Variable"
                                                                                        }
                                                                                    ],
                                                                                    "line": 14,
                                                                                    "tokentype": "Operation"
                                                                                }
                                                                            ],
                                                                            "line": 14,
                                                                            "tokentype": "Operation"
                                                                        }
                                                                    ],
                                                                    "line": 14,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 14,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "memo",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1000000007",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "next",
                                                "primed": true,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FuncCall",
                                                        "args": [
                                                            {
                                                                "value": "count_routes",
                                                                "line": 14,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "locations",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "start",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "finish",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "fuel",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "next",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "abs",
                                                                        "args": [
                                                                            {
                                                                                "name": "Sub",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "GetElement",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "locations",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "curr",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "name": "GetElement",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "locations",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "next",
                                                                                                "primed": true,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    }
                                                                                ],
                                                                                "line": 14,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 14,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 14,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1000000007",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "next",
                                                "primed": true,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FuncCall",
                                                        "args": [
                                                            {
                                                                "value": "count_routes",
                                                                "line": 14,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "locations",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "start",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "finish",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "fuel",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "next",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "abs",
                                                                        "args": [
                                                                            {
                                                                                "name": "Sub",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "GetElement",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "locations",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "curr",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "name": "GetElement",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "locations",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "next",
                                                                                                "primed": true,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    }
                                                                                ],
                                                                                "line": 14,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 14,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 14,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1000000007",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 14
                },
                "14": {
                    "false": 15,
                    "true": 16
                },
                "15": {},
                "16": {
                    "true": 14
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'count_routes'",
                "14": "the condition of the 'for' loop at line 12",
                "15": "*after* the 'for' loop starting at line 12",
                "16": "inside the body of the 'for' loop beginning at line 13"
            },
            "types": {
                "next": "*",
                "remaining_fuel": "*",
                "ans": "*",
                "ind#0": "int",
                "memo": "*",
                "iter#0": "int",
                "curr": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def count_routes(var_0, var_1, var_2, var_3, var_4=None, var_5=None, var_6=None):
    if var_6 is None:
        var_6 = {}
    if var_4 is None:
        var_4 = var_1
        var_5 = var_3
    if var_5 < 0:
        return 0
    if (var_4, var_5) in var_6:
        return var_6[var_4, var_5]
    ans = 1 if var_4 == var_2 else 0
    for next in range(len(var_0)):
        if next != var_4:
            ans += count_routes(var_0, var_1, var_2, var_3, next, var_5 - abs(var_0[var_4] - var_0[next]), var_6)
            ans %= 1000000007
    var_6[var_4, var_5] = ans
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def count_routes(var_0, var_1, var_2, var_3, var_4=None, var_5=None, var_6=None):\n    if var_6 is None:\n        var_6 = {}\n    if var_4 is None:\n        var_4 = var_1\n        var_5 = var_3\n    if var_5 < 0:\n        return 0\n    if (var_4, var_5) in var_6:\n        return var_6[var_4, var_5]\n    ans = 1 if var_4 == var_2 else 0\n    for next in range(len(var_0)):\n        if next != var_4:\n            ans += count_routes(var_0, var_1, var_2, var_3, next, var_5 - abs(var_0[var_4] - var_0[next]), var_6)\n            ans %= 1000000007\n    var_6[var_4, var_5] = ans\n    return ans"
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
        "count_routes": {
            "name": "count_routes",
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
                },
                {
                    "val0": "var_6",
                    "val1": "*",
                    "valueArray": [
                        "var_6",
                        "*"
                    ],
                    "valueList": [
                        "var_6",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "var_6",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "var_6",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "DictInit",
                                    "args": [],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "var_6",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_6",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_6",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "DictInit",
                                        "args": [],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_6",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "var_6",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_6",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "DictInit",
                                        "args": [],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_6",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "var_4",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "var_4",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
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
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_4",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_4",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_4",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_4",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "var_4",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_4",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_4",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "var_5",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "var_4",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "var_3",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_5",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_5",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_4",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_5",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "var_5",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_4",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_3",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_5",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "var_5",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "var_4",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "var_5",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "var_6",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "var_4",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_2",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "originalExpr": {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "var_4",
                                                "primed": true,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_2",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 11,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "0",
                                        "line": 11,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 11,
                                "tokentype": "Operation"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_4",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_6",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "var_4",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11,
                                "originalExpr": {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "var_4",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_2",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_4",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_6",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "var_4",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11,
                                "originalExpr": {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "var_4",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_2",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "var_5",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "var_4",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "var_5",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "var_6",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "originalExpr": {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_0",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12,
                                "tokentype": "Operation"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_4",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_6",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_4",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_6",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "var_5",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "var_4",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "var_5",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "var_6",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "originalExpr": {
                                "value": "0",
                                "line": 12,
                                "tokentype": "Constant"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_4",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_6",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_5",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_4",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_6",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "var_5",
                                            "primed": true,
                                            "line": 7,
                                            "tokentype": "Variable"
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
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "In",
                                            "args": [
                                                {
                                                    "name": "TupleInit",
                                                    "args": [
                                                        {
                                                            "name": "var_4",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "var_5",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "var_6",
                                                    "primed": true,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_6",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_5",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "$ret",
                                            "primed": false,
                                            "line": 0,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "var_5",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
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
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "TupleInit",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_5",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "var_6",
                                                        "primed": true,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_6",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_5",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "$ret",
                                                "primed": false,
                                                "line": 0,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "var_5",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
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
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "TupleInit",
                                                        "args": [
                                                            {
                                                                "name": "var_4",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_5",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "var_6",
                                                        "primed": true,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_6",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_5",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "$ret",
                                                "primed": false,
                                                "line": 0,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
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
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 12,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 12,
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    }
                ],
                "15": [
                    {
                        "val0": "var_6",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "var_6",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_5",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 16,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_6",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "var_6",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_5",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "var_6",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "var_6",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_5",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 16
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "16": [
                    {
                        "val0": "next",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "next",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "next",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                                    "line": 12,
                                    "tokentype": "Variable"
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
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "next",
                                            "primed": true,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_4",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "ans",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "FuncCall",
                                                    "args": [
                                                        {
                                                            "value": "count_routes",
                                                            "line": 14,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "var_0",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "var_1",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "var_2",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "var_3",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "next",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "var_5",
                                                                    "primed": false,
                                                                    "line": 14,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "abs",
                                                                    "args": [
                                                                        {
                                                                            "name": "Sub",
                                                                            "args": [
                                                                                {
                                                                                    "name": "GetElement",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "var_0",
                                                                                            "primed": false,
                                                                                            "line": 14,
                                                                                            "tokentype": "Variable"
                                                                                        },
                                                                                        {
                                                                                            "name": "var_4",
                                                                                            "primed": false,
                                                                                            "line": 14,
                                                                                            "tokentype": "Variable"
                                                                                        }
                                                                                    ],
                                                                                    "line": 14,
                                                                                    "tokentype": "Operation"
                                                                                },
                                                                                {
                                                                                    "name": "GetElement",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "var_0",
                                                                                            "primed": false,
                                                                                            "line": 14,
                                                                                            "tokentype": "Variable"
                                                                                        },
                                                                                        {
                                                                                            "name": "next",
                                                                                            "primed": true,
                                                                                            "line": 14,
                                                                                            "tokentype": "Variable"
                                                                                        }
                                                                                    ],
                                                                                    "line": 14,
                                                                                    "tokentype": "Operation"
                                                                                }
                                                                            ],
                                                                            "line": 14,
                                                                            "tokentype": "Operation"
                                                                        }
                                                                    ],
                                                                    "line": 14,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 14,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "var_6",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1000000007",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "next",
                                                "primed": true,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_4",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FuncCall",
                                                        "args": [
                                                            {
                                                                "value": "count_routes",
                                                                "line": 14,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_2",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_3",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "next",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "abs",
                                                                        "args": [
                                                                            {
                                                                                "name": "Sub",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "GetElement",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "var_0",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "var_4",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "name": "GetElement",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "var_0",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "next",
                                                                                                "primed": true,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    }
                                                                                ],
                                                                                "line": 14,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 14,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 14,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_6",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1000000007",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "next",
                                                "primed": true,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_4",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FuncCall",
                                                        "args": [
                                                            {
                                                                "value": "count_routes",
                                                                "line": 14,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "var_0",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_1",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_2",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_3",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "next",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "var_5",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "abs",
                                                                        "args": [
                                                                            {
                                                                                "name": "Sub",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "GetElement",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "var_0",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "var_4",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "name": "GetElement",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "var_0",
                                                                                                "primed": false,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "next",
                                                                                                "primed": true,
                                                                                                "line": 14,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    }
                                                                                ],
                                                                                "line": 14,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 14,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 14,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_6",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1000000007",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 14
                },
                "14": {
                    "false": 15,
                    "true": 16
                },
                "15": {},
                "16": {
                    "true": 14
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'count_routes'",
                "14": "the condition of the 'for' loop at line 12",
                "15": "*after* the 'for' loop starting at line 12",
                "16": "inside the body of the 'for' loop beginning at line 13"
            },
            "types": {
                "var_4": "*",
                "next": "*",
                "var_5": "*",
                "var_6": "*",
                "ans": "*",
                "ind#0": "int",
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
def count_routes(locations, start, finish, fuel, curr=None, remaining_fuel=None, memo=None):
    if memo is None:
        memo = {}
    if curr is None:
        curr = start
        remaining_fuel = fuel
    if remaining_fuel < 0:
        return 0
    if (curr, remaining_fuel) in memo:
        return memo[curr, remaining_fuel]
    ans = 1 if curr == finish else 0
    for next in range(len(locations)):
        if next != curr:
            ans += count_routes(locations, start, finish, fuel, next, remaining_fuel + -abs(locations[curr] + -locations[next]), memo)
            ans %= 1000000007
    memo[curr, remaining_fuel] = ans
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def count_routes(locations, start, finish, fuel, curr=None, remaining_fuel=None, memo=None):\n    if memo is None:\n        memo = {}\n    if curr is None:\n        curr = start\n        remaining_fuel = fuel\n    if remaining_fuel < 0:\n        return 0\n    if (curr, remaining_fuel) in memo:\n        return memo[curr, remaining_fuel]\n    ans = 1 if curr == finish else 0\n    for next in range(len(locations)):\n        if next != curr:\n            ans += count_routes(locations, start, finish, fuel, next, remaining_fuel + -abs(locations[curr] + -locations[next]), memo)\n            ans %= 1000000007\n    memo[curr, remaining_fuel] = ans\n    return ans"
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
        "count_routes": {
            "name": "count_routes",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "locations",
                    "val1": "*",
                    "valueArray": [
                        "locations",
                        "*"
                    ],
                    "valueList": [
                        "locations",
                        "*"
                    ]
                },
                {
                    "val0": "start",
                    "val1": "*",
                    "valueArray": [
                        "start",
                        "*"
                    ],
                    "valueList": [
                        "start",
                        "*"
                    ]
                },
                {
                    "val0": "finish",
                    "val1": "*",
                    "valueArray": [
                        "finish",
                        "*"
                    ],
                    "valueList": [
                        "finish",
                        "*"
                    ]
                },
                {
                    "val0": "fuel",
                    "val1": "*",
                    "valueArray": [
                        "fuel",
                        "*"
                    ],
                    "valueList": [
                        "fuel",
                        "*"
                    ]
                },
                {
                    "val0": "curr",
                    "val1": "*",
                    "valueArray": [
                        "curr",
                        "*"
                    ],
                    "valueList": [
                        "curr",
                        "*"
                    ]
                },
                {
                    "val0": "remaining_fuel",
                    "val1": "*",
                    "valueArray": [
                        "remaining_fuel",
                        "*"
                    ],
                    "valueList": [
                        "remaining_fuel",
                        "*"
                    ]
                },
                {
                    "val0": "memo",
                    "val1": "*",
                    "valueArray": [
                        "memo",
                        "*"
                    ],
                    "valueList": [
                        "memo",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "memo",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "memo",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "DictInit",
                                    "args": [],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "memo",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "memo",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "memo",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "DictInit",
                                        "args": [],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "memo",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "memo",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "memo",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "DictInit",
                                        "args": [],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "memo",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "curr",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "curr",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "start",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "curr",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "curr",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "start",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "curr",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "curr",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "start",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "curr",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "remaining_fuel",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "curr",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "fuel",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "remaining_fuel",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "remaining_fuel",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "fuel",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "remaining_fuel",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "remaining_fuel",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "fuel",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "remaining_fuel",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "remaining_fuel",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "curr",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "remaining_fuel",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "memo",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "curr",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "finish",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "originalExpr": {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "curr",
                                                "primed": true,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "finish",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 11,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "0",
                                        "line": 11,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 11,
                                "tokentype": "Operation"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "curr",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "finish",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11,
                                "originalExpr": {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "curr",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "finish",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "curr",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "finish",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11,
                                "originalExpr": {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "curr",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "finish",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "remaining_fuel",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "curr",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "remaining_fuel",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "memo",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "locations",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "originalExpr": {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "locations",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12,
                                "tokentype": "Operation"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "locations",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "locations",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "locations",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "locations",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "remaining_fuel",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "curr",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "remaining_fuel",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "memo",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "originalExpr": {
                                "value": "0",
                                "line": 12,
                                "tokentype": "Constant"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "curr",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "remaining_fuel",
                                            "primed": true,
                                            "line": 7,
                                            "tokentype": "Variable"
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
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "In",
                                            "args": [
                                                {
                                                    "name": "TupleInit",
                                                    "args": [
                                                        {
                                                            "name": "curr",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "remaining_fuel",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "memo",
                                                    "primed": true,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "memo",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "remaining_fuel",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "$ret",
                                            "primed": false,
                                            "line": 0,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "remaining_fuel",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
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
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "TupleInit",
                                                        "args": [
                                                            {
                                                                "name": "curr",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "memo",
                                                        "primed": true,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "memo",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "remaining_fuel",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "$ret",
                                                "primed": false,
                                                "line": 0,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "remaining_fuel",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
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
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "TupleInit",
                                                        "args": [
                                                            {
                                                                "name": "curr",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "remaining_fuel",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "memo",
                                                        "primed": true,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "memo",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "remaining_fuel",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "$ret",
                                                "primed": false,
                                                "line": 0,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
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
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 12,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 12,
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    }
                ],
                "15": [
                    {
                        "val0": "memo",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "memo",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "remaining_fuel",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 16,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "memo",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "memo",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "remaining_fuel",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "memo",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "memo",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "remaining_fuel",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 16
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "16": [
                    {
                        "val0": "next",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "next",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "next",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                                    "line": 12,
                                    "tokentype": "Variable"
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
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "next",
                                            "primed": true,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "curr",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "ans",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "FuncCall",
                                                    "args": [
                                                        {
                                                            "value": "count_routes",
                                                            "line": 14,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "locations",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "start",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "finish",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "fuel",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "next",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "remaining_fuel",
                                                                    "primed": false,
                                                                    "line": 14,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "name": "abs",
                                                                            "args": [
                                                                                {
                                                                                    "name": "Add",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "GetElement",
                                                                                            "args": [
                                                                                                {
                                                                                                    "name": "locations",
                                                                                                    "primed": false,
                                                                                                    "line": 14,
                                                                                                    "tokentype": "Variable"
                                                                                                },
                                                                                                {
                                                                                                    "name": "curr",
                                                                                                    "primed": false,
                                                                                                    "line": 14,
                                                                                                    "tokentype": "Variable"
                                                                                                }
                                                                                            ],
                                                                                            "line": 14,
                                                                                            "tokentype": "Operation"
                                                                                        },
                                                                                        {
                                                                                            "name": "USub",
                                                                                            "args": [
                                                                                                {
                                                                                                    "name": "GetElement",
                                                                                                    "args": [
                                                                                                        {
                                                                                                            "name": "locations",
                                                                                                            "primed": false,
                                                                                                            "line": 14,
                                                                                                            "tokentype": "Variable"
                                                                                                        },
                                                                                                        {
                                                                                                            "name": "next",
                                                                                                            "primed": true,
                                                                                                            "line": 14,
                                                                                                            "tokentype": "Variable"
                                                                                                        }
                                                                                                    ],
                                                                                                    "line": 14,
                                                                                                    "tokentype": "Operation"
                                                                                                }
                                                                                            ],
                                                                                            "line": 14,
                                                                                            "tokentype": "Operation"
                                                                                        }
                                                                                    ],
                                                                                    "line": 14,
                                                                                    "tokentype": "Operation"
                                                                                }
                                                                            ],
                                                                            "line": 14,
                                                                            "tokentype": "Operation"
                                                                        }
                                                                    ],
                                                                    "line": 14,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 14,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "memo",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1000000007",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "next",
                                                "primed": true,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FuncCall",
                                                        "args": [
                                                            {
                                                                "value": "count_routes",
                                                                "line": 14,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "locations",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "start",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "finish",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "fuel",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "next",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "name": "abs",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "Add",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "GetElement",
                                                                                                "args": [
                                                                                                    {
                                                                                                        "name": "locations",
                                                                                                        "primed": false,
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Variable"
                                                                                                    },
                                                                                                    {
                                                                                                        "name": "curr",
                                                                                                        "primed": false,
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Variable"
                                                                                                    }
                                                                                                ],
                                                                                                "line": 14,
                                                                                                "tokentype": "Operation"
                                                                                            },
                                                                                            {
                                                                                                "name": "USub",
                                                                                                "args": [
                                                                                                    {
                                                                                                        "name": "GetElement",
                                                                                                        "args": [
                                                                                                            {
                                                                                                                "name": "locations",
                                                                                                                "primed": false,
                                                                                                                "line": 14,
                                                                                                                "tokentype": "Variable"
                                                                                                            },
                                                                                                            {
                                                                                                                "name": "next",
                                                                                                                "primed": true,
                                                                                                                "line": 14,
                                                                                                                "tokentype": "Variable"
                                                                                                            }
                                                                                                        ],
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Operation"
                                                                                                    }
                                                                                                ],
                                                                                                "line": 14,
                                                                                                "tokentype": "Operation"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    }
                                                                                ],
                                                                                "line": 14,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 14,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 14,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1000000007",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "next",
                                                "primed": true,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "curr",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FuncCall",
                                                        "args": [
                                                            {
                                                                "value": "count_routes",
                                                                "line": 14,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "locations",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "start",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "finish",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "fuel",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "next",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "remaining_fuel",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "name": "abs",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "Add",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "GetElement",
                                                                                                "args": [
                                                                                                    {
                                                                                                        "name": "locations",
                                                                                                        "primed": false,
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Variable"
                                                                                                    },
                                                                                                    {
                                                                                                        "name": "curr",
                                                                                                        "primed": false,
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Variable"
                                                                                                    }
                                                                                                ],
                                                                                                "line": 14,
                                                                                                "tokentype": "Operation"
                                                                                            },
                                                                                            {
                                                                                                "name": "USub",
                                                                                                "args": [
                                                                                                    {
                                                                                                        "name": "GetElement",
                                                                                                        "args": [
                                                                                                            {
                                                                                                                "name": "locations",
                                                                                                                "primed": false,
                                                                                                                "line": 14,
                                                                                                                "tokentype": "Variable"
                                                                                                            },
                                                                                                            {
                                                                                                                "name": "next",
                                                                                                                "primed": true,
                                                                                                                "line": 14,
                                                                                                                "tokentype": "Variable"
                                                                                                            }
                                                                                                        ],
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Operation"
                                                                                                    }
                                                                                                ],
                                                                                                "line": 14,
                                                                                                "tokentype": "Operation"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    }
                                                                                ],
                                                                                "line": 14,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 14,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 14,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "memo",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1000000007",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 14
                },
                "14": {
                    "false": 15,
                    "true": 16
                },
                "15": {},
                "16": {
                    "true": 14
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'count_routes'",
                "14": "the condition of the 'for' loop at line 12",
                "15": "*after* the 'for' loop starting at line 12",
                "16": "inside the body of the 'for' loop beginning at line 13"
            },
            "types": {
                "next": "*",
                "remaining_fuel": "*",
                "ans": "*",
                "ind#0": "int",
                "memo": "*",
                "iter#0": "int",
                "curr": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def count_routes(var_7, var_8, var_9, var_10, var_11=None, var_12=None, var_13=None):
    if var_13 is None:
        var_13 = {}
    if var_11 is None:
        var_11 = var_8
        var_12 = var_10
    if var_12 < 0:
        return 0
    if (var_11, var_12) in var_13:
        return var_13[var_11, var_12]
    ans = 1 if var_11 == var_9 else 0
    for next in range(len(var_7)):
        if next != var_11:
            ans += count_routes(var_7, var_8, var_9, var_10, next, var_12 + -abs(var_7[var_11] + -var_7[next]), var_13)
            ans %= 1000000007
    var_13[var_11, var_12] = ans
    return ans
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def count_routes(var_7, var_8, var_9, var_10, var_11=None, var_12=None, var_13=None):\n    if var_13 is None:\n        var_13 = {}\n    if var_11 is None:\n        var_11 = var_8\n        var_12 = var_10\n    if var_12 < 0:\n        return 0\n    if (var_11, var_12) in var_13:\n        return var_13[var_11, var_12]\n    ans = 1 if var_11 == var_9 else 0\n    for next in range(len(var_7)):\n        if next != var_11:\n            ans += count_routes(var_7, var_8, var_9, var_10, next, var_12 + -abs(var_7[var_11] + -var_7[next]), var_13)\n            ans %= 1000000007\n    var_13[var_11, var_12] = ans\n    return ans"
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
        "count_routes": {
            "name": "count_routes",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "var_7",
                    "val1": "*",
                    "valueArray": [
                        "var_7",
                        "*"
                    ],
                    "valueList": [
                        "var_7",
                        "*"
                    ]
                },
                {
                    "val0": "var_8",
                    "val1": "*",
                    "valueArray": [
                        "var_8",
                        "*"
                    ],
                    "valueList": [
                        "var_8",
                        "*"
                    ]
                },
                {
                    "val0": "var_9",
                    "val1": "*",
                    "valueArray": [
                        "var_9",
                        "*"
                    ],
                    "valueList": [
                        "var_9",
                        "*"
                    ]
                },
                {
                    "val0": "var_10",
                    "val1": "*",
                    "valueArray": [
                        "var_10",
                        "*"
                    ],
                    "valueList": [
                        "var_10",
                        "*"
                    ]
                },
                {
                    "val0": "var_11",
                    "val1": "*",
                    "valueArray": [
                        "var_11",
                        "*"
                    ],
                    "valueList": [
                        "var_11",
                        "*"
                    ]
                },
                {
                    "val0": "var_12",
                    "val1": "*",
                    "valueArray": [
                        "var_12",
                        "*"
                    ],
                    "valueList": [
                        "var_12",
                        "*"
                    ]
                },
                {
                    "val0": "var_13",
                    "val1": "*",
                    "valueArray": [
                        "var_13",
                        "*"
                    ],
                    "valueList": [
                        "var_13",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "var_13",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "var_13",
                                            "primed": false,
                                            "line": 2,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 2,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 2,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "DictInit",
                                    "args": [],
                                    "line": 3,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "var_13",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_13",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_13",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "DictInit",
                                        "args": [],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_13",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "var_13",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_13",
                                                "primed": false,
                                                "line": 2,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 2,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 2,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "DictInit",
                                        "args": [],
                                        "line": 3,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_13",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "var_11",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "var_11",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "var_8",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_11",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_11",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_11",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_8",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_11",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "var_11",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_11",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_8",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_11",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "var_12",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Is",
                                    "args": [
                                        {
                                            "name": "var_11",
                                            "primed": false,
                                            "line": 4,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "value": "None",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "var_10",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_12",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_12",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_11",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_10",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_12",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "var_12",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Is",
                                        "args": [
                                            {
                                                "name": "var_11",
                                                "primed": false,
                                                "line": 4,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "value": "None",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "var_10",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_12",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "var_12",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "var_11",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "var_12",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "var_13",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "var_11",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_9",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 11,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "originalExpr": {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Eq",
                                        "args": [
                                            {
                                                "name": "var_11",
                                                "primed": true,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_9",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "1",
                                        "line": 11,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "value": "0",
                                        "line": 11,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 11,
                                "tokentype": "Operation"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_12",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_11",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_12",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_13",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "var_11",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_9",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11,
                                "originalExpr": {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "var_11",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_9",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_12",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_11",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_12",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_13",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "Eq",
                                                "args": [
                                                    {
                                                        "name": "var_11",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_9",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "value": "0",
                                                "line": 11,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 11,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 11,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11,
                                "originalExpr": {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "Eq",
                                            "args": [
                                                {
                                                    "name": "var_11",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_9",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "value": "0",
                                            "line": 11,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 11,
                                    "tokentype": "Operation"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "var_12",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "var_11",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "var_12",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "var_13",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_7",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "originalExpr": {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "var_7",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12,
                                "tokentype": "Operation"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_12",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_11",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_12",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_13",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_7",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_7",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_12",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_11",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_12",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_13",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "range",
                                        "args": [
                                            {
                                                "name": "len",
                                                "args": [
                                                    {
                                                        "name": "var_7",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "name": "range",
                                    "args": [
                                        {
                                            "name": "len",
                                            "args": [
                                                {
                                                    "name": "var_7",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Not",
                                    "args": [
                                        {
                                            "name": "Or",
                                            "args": [
                                                {
                                                    "name": "Lt",
                                                    "args": [
                                                        {
                                                            "name": "var_12",
                                                            "primed": true,
                                                            "line": 7,
                                                            "tokentype": "Variable"
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
                                                    "name": "In",
                                                    "args": [
                                                        {
                                                            "name": "TupleInit",
                                                            "args": [
                                                                {
                                                                    "name": "var_11",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "var_12",
                                                                    "primed": true,
                                                                    "line": 9,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 9,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "var_13",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "originalExpr": {
                                "value": "0",
                                "line": 12,
                                "tokentype": "Constant"
                            },
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_12",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_11",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_12",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_13",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Not",
                                        "args": [
                                            {
                                                "name": "Or",
                                                "args": [
                                                    {
                                                        "name": "Lt",
                                                        "args": [
                                                            {
                                                                "name": "var_12",
                                                                "primed": true,
                                                                "line": 7,
                                                                "tokentype": "Variable"
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
                                                        "name": "In",
                                                        "args": [
                                                            {
                                                                "name": "TupleInit",
                                                                "args": [
                                                                    {
                                                                        "name": "var_11",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "var_12",
                                                                        "primed": true,
                                                                        "line": 9,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 9,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_13",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "value": "0",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12,
                                "originalExpr": {
                                    "value": "0",
                                    "line": 12,
                                    "tokentype": "Constant"
                                }
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "var_12",
                                            "primed": true,
                                            "line": 7,
                                            "tokentype": "Variable"
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
                                    "value": "0",
                                    "line": 8,
                                    "tokentype": "Constant"
                                },
                                {
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "In",
                                            "args": [
                                                {
                                                    "name": "TupleInit",
                                                    "args": [
                                                        {
                                                            "name": "var_11",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "var_12",
                                                            "primed": true,
                                                            "line": 9,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 9,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "var_13",
                                                    "primed": true,
                                                    "line": 9,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 9,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_13",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "var_12",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "$ret",
                                            "primed": false,
                                            "line": 0,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "var_12",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
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
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "TupleInit",
                                                        "args": [
                                                            {
                                                                "name": "var_11",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_12",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "var_13",
                                                        "primed": true,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_13",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_12",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "$ret",
                                                "primed": false,
                                                "line": 0,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "var_12",
                                                "primed": true,
                                                "line": 7,
                                                "tokentype": "Variable"
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
                                        "value": "0",
                                        "line": 8,
                                        "tokentype": "Constant"
                                    },
                                    {
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "In",
                                                "args": [
                                                    {
                                                        "name": "TupleInit",
                                                        "args": [
                                                            {
                                                                "name": "var_11",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_12",
                                                                "primed": true,
                                                                "line": 9,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 9,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "var_13",
                                                        "primed": true,
                                                        "line": 9,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 9,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_13",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "var_12",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "$ret",
                                                "primed": false,
                                                "line": 0,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
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
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
                                            "line": 12,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 12,
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
                                                "line": 12,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    }
                ],
                "15": [
                    {
                        "val0": "var_13",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "var_13",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "var_12",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 16,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 16,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "var_13",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "var_13",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_12",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "var_13",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "var_13",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "var_12",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 16,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 16
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ans",
                            "primed": false,
                            "line": 17,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 17
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ans",
                                "primed": false,
                                "line": 17
                            }
                        ]
                    }
                ],
                "16": [
                    {
                        "val0": "next",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 12,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "next",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "next",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                                    "line": 12,
                                    "tokentype": "Variable"
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
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
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
                                        "line": 12,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 12,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 12
                            }
                        ]
                    },
                    {
                        "val0": "ans",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "NotEq",
                                    "args": [
                                        {
                                            "name": "next",
                                            "primed": true,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "var_11",
                                            "primed": false,
                                            "line": 13,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "AssAdd",
                                            "args": [
                                                {
                                                    "name": "ans",
                                                    "primed": false,
                                                    "line": 14,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "FuncCall",
                                                    "args": [
                                                        {
                                                            "value": "count_routes",
                                                            "line": 14,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "var_7",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "var_8",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "var_9",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "var_10",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "next",
                                                            "primed": true,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "var_12",
                                                                    "primed": false,
                                                                    "line": 14,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "name": "abs",
                                                                            "args": [
                                                                                {
                                                                                    "name": "Add",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "GetElement",
                                                                                            "args": [
                                                                                                {
                                                                                                    "name": "var_7",
                                                                                                    "primed": false,
                                                                                                    "line": 14,
                                                                                                    "tokentype": "Variable"
                                                                                                },
                                                                                                {
                                                                                                    "name": "var_11",
                                                                                                    "primed": false,
                                                                                                    "line": 14,
                                                                                                    "tokentype": "Variable"
                                                                                                }
                                                                                            ],
                                                                                            "line": 14,
                                                                                            "tokentype": "Operation"
                                                                                        },
                                                                                        {
                                                                                            "name": "USub",
                                                                                            "args": [
                                                                                                {
                                                                                                    "name": "GetElement",
                                                                                                    "args": [
                                                                                                        {
                                                                                                            "name": "var_7",
                                                                                                            "primed": false,
                                                                                                            "line": 14,
                                                                                                            "tokentype": "Variable"
                                                                                                        },
                                                                                                        {
                                                                                                            "name": "next",
                                                                                                            "primed": true,
                                                                                                            "line": 14,
                                                                                                            "tokentype": "Variable"
                                                                                                        }
                                                                                                    ],
                                                                                                    "line": 14,
                                                                                                    "tokentype": "Operation"
                                                                                                }
                                                                                            ],
                                                                                            "line": 14,
                                                                                            "tokentype": "Operation"
                                                                                        }
                                                                                    ],
                                                                                    "line": 14,
                                                                                    "tokentype": "Operation"
                                                                                }
                                                                            ],
                                                                            "line": 14,
                                                                            "tokentype": "Operation"
                                                                        }
                                                                    ],
                                                                    "line": 14,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 14,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "var_13",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 14,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 14,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "value": "1000000007",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "ans",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 13,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "next",
                                                "primed": true,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_11",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FuncCall",
                                                        "args": [
                                                            {
                                                                "value": "count_routes",
                                                                "line": 14,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "var_7",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_8",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_9",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_10",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "next",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "var_12",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "name": "abs",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "Add",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "GetElement",
                                                                                                "args": [
                                                                                                    {
                                                                                                        "name": "var_7",
                                                                                                        "primed": false,
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Variable"
                                                                                                    },
                                                                                                    {
                                                                                                        "name": "var_11",
                                                                                                        "primed": false,
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Variable"
                                                                                                    }
                                                                                                ],
                                                                                                "line": 14,
                                                                                                "tokentype": "Operation"
                                                                                            },
                                                                                            {
                                                                                                "name": "USub",
                                                                                                "args": [
                                                                                                    {
                                                                                                        "name": "GetElement",
                                                                                                        "args": [
                                                                                                            {
                                                                                                                "name": "var_7",
                                                                                                                "primed": false,
                                                                                                                "line": 14,
                                                                                                                "tokentype": "Variable"
                                                                                                            },
                                                                                                            {
                                                                                                                "name": "next",
                                                                                                                "primed": true,
                                                                                                                "line": 14,
                                                                                                                "tokentype": "Variable"
                                                                                                            }
                                                                                                        ],
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Operation"
                                                                                                    }
                                                                                                ],
                                                                                                "line": 14,
                                                                                                "tokentype": "Operation"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    }
                                                                                ],
                                                                                "line": 14,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 14,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 14,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_13",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1000000007",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ],
                        "valueList": [
                            "ans",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "NotEq",
                                        "args": [
                                            {
                                                "name": "next",
                                                "primed": true,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "var_11",
                                                "primed": false,
                                                "line": 13,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "AssAdd",
                                                "args": [
                                                    {
                                                        "name": "ans",
                                                        "primed": false,
                                                        "line": 14,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "FuncCall",
                                                        "args": [
                                                            {
                                                                "value": "count_routes",
                                                                "line": 14,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "var_7",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_8",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_9",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "var_10",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "next",
                                                                "primed": true,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "var_12",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "name": "abs",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "Add",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "GetElement",
                                                                                                "args": [
                                                                                                    {
                                                                                                        "name": "var_7",
                                                                                                        "primed": false,
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Variable"
                                                                                                    },
                                                                                                    {
                                                                                                        "name": "var_11",
                                                                                                        "primed": false,
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Variable"
                                                                                                    }
                                                                                                ],
                                                                                                "line": 14,
                                                                                                "tokentype": "Operation"
                                                                                            },
                                                                                            {
                                                                                                "name": "USub",
                                                                                                "args": [
                                                                                                    {
                                                                                                        "name": "GetElement",
                                                                                                        "args": [
                                                                                                            {
                                                                                                                "name": "var_7",
                                                                                                                "primed": false,
                                                                                                                "line": 14,
                                                                                                                "tokentype": "Variable"
                                                                                                            },
                                                                                                            {
                                                                                                                "name": "next",
                                                                                                                "primed": true,
                                                                                                                "line": 14,
                                                                                                                "tokentype": "Variable"
                                                                                                            }
                                                                                                        ],
                                                                                                        "line": 14,
                                                                                                        "tokentype": "Operation"
                                                                                                    }
                                                                                                ],
                                                                                                "line": 14,
                                                                                                "tokentype": "Operation"
                                                                                            }
                                                                                        ],
                                                                                        "line": 14,
                                                                                        "tokentype": "Operation"
                                                                                    }
                                                                                ],
                                                                                "line": 14,
                                                                                "tokentype": "Operation"
                                                                            }
                                                                        ],
                                                                        "line": 14,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 14,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "var_13",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 14,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 14,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "value": "1000000007",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "ans",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 13
                            }
                        ]
                    }
                ]
            },
            "loctrans": {
                "1": {
                    "true": 14
                },
                "14": {
                    "false": 15,
                    "true": 16
                },
                "15": {},
                "16": {
                    "true": 14
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'count_routes'",
                "14": "the condition of the 'for' loop at line 12",
                "15": "*after* the 'for' loop starting at line 12",
                "16": "inside the body of the 'for' loop beginning at line 13"
            },
            "types": {
                "next": "*",
                "ans": "*",
                "ind#0": "int",
                "iter#0": "int",
                "var_13": "*",
                "var_12": "*",
                "var_11": "*"
            }
        }
    }
}
```

</details>

