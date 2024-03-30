# Test Report

Time: 2024-03-30 08:34:38.034260

### Base Program

```py
def min_operations(arr1, arr2):
    n = len(arr1)
    dp = [float('inf')] * n
    for a in arr2:
        new_dp = [float('inf')] * n
        p = 0
        for i in range(n):
            if a < arr1[i]:
                new_dp[i] = p
            if i > 0 and dp[i - 1] < p:
                p = dp[i - 1]
            if arr1[i] > arr1[i + 1]:
                return -1
        dp = new_dp
    return dp[-1]
```

## Test Case 1

### Modified Program

```py
def min_operations(arr1, arr2):
    n = len(arr1)
    dp = [float('inf')] * n
    for a in arr2:
        new_dp = [float('inf')] * n
        p = 0
        for i in range(n):
            if a < arr1[i]:
                new_dp[i] = p
            if i > 0 and dp[i - 1] < p:
                p = dp[i - 1]
            if arr1[i] > arr1[i + 1]:
                return -1
        dp = new_dp
    return dp[-1]
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_operations(arr1, arr2):\n    n = len(arr1)\n    dp = [float('inf')] * n\n    for a in arr2:\n        new_dp = [float('inf')] * n\n        p = 0\n        for i in range(n):\n            if a < arr1[i]:\n                new_dp[i] = p\n            if i > 0 and dp[i - 1] < p:\n                p = dp[i - 1]\n            if arr1[i] > arr1[i + 1]:\n                return -1\n        dp = new_dp\n    return dp[-1]"
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
        "min_operations": {
            "name": "min_operations",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "arr1",
                    "val1": "*",
                    "valueArray": [
                        "arr1",
                        "*"
                    ],
                    "valueList": [
                        "arr1",
                        "*"
                    ]
                },
                {
                    "val0": "arr2",
                    "val1": "*",
                    "valueArray": [
                        "arr2",
                        "*"
                    ],
                    "valueList": [
                        "arr2",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "arr1",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "arr1",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "arr1",
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
                        "val0": "dp",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "float",
                                            "args": [
                                                {
                                                    "value": "\"inf\"",
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
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "arr2",
                            "primed": false,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "arr2",
                                "primed": false,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "arr2",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 15,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "a",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "a",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "a",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
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
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "new_dp",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "float",
                                            "args": [
                                                {
                                                    "value": "\"inf\"",
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
                                    "name": "n",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "new_dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                                        "name": "n",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "new_dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                                        "name": "n",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "p",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 7
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 7,
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "dp",
                        "val1": {
                            "name": "new_dp",
                            "primed": false,
                            "line": 14,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "new_dp",
                                "primed": false,
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "new_dp",
                                "primed": false,
                                "line": 14
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                    },
                    {
                        "val0": "new_dp",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "arr1",
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
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssignElement",
                                    "args": [
                                        {
                                            "name": "new_dp",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "new_dp",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "new_dp",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
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
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "new_dp",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "new_dp",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "new_dp",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
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
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "new_dp",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "new_dp",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 10,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "dp",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
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
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "p",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "dp",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 11,
                                                    "tokentype": "Constant"
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
                                    "name": "p",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "dp",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "p",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "dp",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
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
                                        "name": "p",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "dp",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "p",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "dp",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
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
                                        "name": "p",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "arr1",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "arr1",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": true,
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
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 13,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
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
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 13,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
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
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 13,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                    "false": 6,
                    "true": 7
                },
                "6": {
                    "true": 2
                },
                "7": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'min_operations'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8"
            },
            "types": {
                "new_dp": "*",
                "p": "*",
                "a": "*",
                "ind#1": "int",
                "ind#0": "int",
                "iter#1": "int",
                "i": "*",
                "iter#0": "int",
                "dp": "*",
                "n": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def min_operations(var_0, var_1):
    n = len(var_0)
    dp = [float('inf')] * n
    for a in var_1:
        new_dp = [float('inf')] * n
        p = 0
        for i in range(n):
            if a < var_0[i]:
                new_dp[i] = p
            if i > 0 and dp[i - 1] < p:
                p = dp[i - 1]
            if var_0[i] > var_0[i + 1]:
                return -1
        dp = new_dp
    return dp[-1]
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_operations(var_0, var_1):\n    n = len(var_0)\n    dp = [float('inf')] * n\n    for a in var_1:\n        new_dp = [float('inf')] * n\n        p = 0\n        for i in range(n):\n            if a < var_0[i]:\n                new_dp[i] = p\n            if i > 0 and dp[i - 1] < p:\n                p = dp[i - 1]\n            if var_0[i] > var_0[i + 1]:\n                return -1\n        dp = new_dp\n    return dp[-1]"
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
        "min_operations": {
            "name": "min_operations",
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
                        "val0": "n",
                        "val1": {
                            "name": "len",
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
                            "n",
                            {
                                "name": "len",
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
                            "n",
                            {
                                "name": "len",
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
                        "val0": "dp",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "float",
                                            "args": [
                                                {
                                                    "value": "\"inf\"",
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
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 3,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 3,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_1",
                            "primed": false,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 15,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "a",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "a",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "a",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
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
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "new_dp",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "float",
                                            "args": [
                                                {
                                                    "value": "\"inf\"",
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
                                    "name": "n",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "new_dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                                        "name": "n",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "new_dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                                        "name": "n",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "p",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 7
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 7,
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "dp",
                        "val1": {
                            "name": "new_dp",
                            "primed": false,
                            "line": 14,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "new_dp",
                                "primed": false,
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "new_dp",
                                "primed": false,
                                "line": 14
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                    },
                    {
                        "val0": "new_dp",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_0",
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
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssignElement",
                                    "args": [
                                        {
                                            "name": "new_dp",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "new_dp",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "new_dp",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
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
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "new_dp",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "new_dp",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "new_dp",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
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
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "new_dp",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "new_dp",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 10,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "dp",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Sub",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
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
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "p",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "dp",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Sub",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "1",
                                                    "line": 11,
                                                    "tokentype": "Constant"
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
                                    "name": "p",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "dp",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "p",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "dp",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
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
                                        "name": "p",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "dp",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Sub",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
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
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "p",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "dp",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Sub",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "1",
                                                        "line": 11,
                                                        "tokentype": "Constant"
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
                                        "name": "p",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_0",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "name": "i",
                                                            "primed": true,
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
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 13,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
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
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 13,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_0",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "name": "i",
                                                                "primed": true,
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
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 13,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                    "false": 6,
                    "true": 7
                },
                "6": {
                    "true": 2
                },
                "7": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'min_operations'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8"
            },
            "types": {
                "new_dp": "*",
                "p": "*",
                "a": "*",
                "ind#1": "int",
                "ind#0": "int",
                "iter#1": "int",
                "i": "*",
                "iter#0": "int",
                "dp": "*",
                "n": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def min_operations(arr1, arr2):
    n = len(arr1)
    dp = n * [float('inf')]
    for a in arr2:
        new_dp = n * [float('inf')]
        p = 0
        for i in range(n):
            if a < arr1[i]:
                new_dp[i] = p
            if i > 0 and dp[i + -1] < p:
                p = dp[i + -1]
            if arr1[i] > arr1[1 + i]:
                return -1
        dp = new_dp
    return dp[-1]
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_operations(arr1, arr2):\n    n = len(arr1)\n    dp = n * [float('inf')]\n    for a in arr2:\n        new_dp = n * [float('inf')]\n        p = 0\n        for i in range(n):\n            if a < arr1[i]:\n                new_dp[i] = p\n            if i > 0 and dp[i + -1] < p:\n                p = dp[i + -1]\n            if arr1[i] > arr1[1 + i]:\n                return -1\n        dp = new_dp\n    return dp[-1]"
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
        "min_operations": {
            "name": "min_operations",
            "rettype": "*",
            "initloc": 1,
            "endloc": 0,
            "params": [
                {
                    "val0": "arr1",
                    "val1": "*",
                    "valueArray": [
                        "arr1",
                        "*"
                    ],
                    "valueList": [
                        "arr1",
                        "*"
                    ]
                },
                {
                    "val0": "arr2",
                    "val1": "*",
                    "valueArray": [
                        "arr2",
                        "*"
                    ],
                    "valueList": [
                        "arr2",
                        "*"
                    ]
                }
            ],
            "locexprs": {
                "1": [
                    {
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
                                {
                                    "name": "arr1",
                                    "primed": false,
                                    "line": 2,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 2,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "arr1",
                                        "primed": false,
                                        "line": 2,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "arr1",
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
                        "val0": "dp",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "float",
                                            "args": [
                                                {
                                                    "value": "\"inf\"",
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
                            "dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                            "dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "arr2",
                            "primed": false,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "arr2",
                                "primed": false,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "arr2",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 15,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "a",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "a",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "a",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
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
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "new_dp",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "float",
                                            "args": [
                                                {
                                                    "value": "\"inf\"",
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
                            "new_dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                            "new_dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "p",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 7
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 7,
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "dp",
                        "val1": {
                            "name": "new_dp",
                            "primed": false,
                            "line": 14,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "new_dp",
                                "primed": false,
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "new_dp",
                                "primed": false,
                                "line": 14
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                    },
                    {
                        "val0": "new_dp",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "arr1",
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
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssignElement",
                                    "args": [
                                        {
                                            "name": "new_dp",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "new_dp",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "new_dp",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
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
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "new_dp",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "new_dp",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "new_dp",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
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
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "new_dp",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "new_dp",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 10,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "dp",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 10,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
                                                                            "line": 10,
                                                                            "tokentype": "Constant"
                                                                        }
                                                                    ],
                                                                    "line": 10,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 10,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "p",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "dp",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 11,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
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
                                    "name": "p",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "dp",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 10,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 10,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 10,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "p",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "dp",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
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
                                        "name": "p",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "dp",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 10,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 10,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 10,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "p",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "dp",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
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
                                        "name": "p",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "arr1",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "arr1",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 12,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
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
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 13,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 12,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
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
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 13,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "arr1",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 12,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
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
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 13,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                    "false": 6,
                    "true": 7
                },
                "6": {
                    "true": 2
                },
                "7": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'min_operations'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8"
            },
            "types": {
                "new_dp": "*",
                "p": "*",
                "a": "*",
                "ind#1": "int",
                "ind#0": "int",
                "iter#1": "int",
                "i": "*",
                "iter#0": "int",
                "dp": "*",
                "n": "*"
            }
        }
    }
}
```

</details>

## Test Case 4

### Modified Program

```py
def min_operations(var_2, var_3):
    n = len(var_2)
    dp = n * [float('inf')]
    for a in var_3:
        new_dp = n * [float('inf')]
        p = 0
        for i in range(n):
            if a < var_2[i]:
                new_dp[i] = p
            if i > 0 and dp[i + -1] < p:
                p = dp[i + -1]
            if var_2[i] > var_2[1 + i]:
                return -1
        dp = new_dp
    return dp[-1]
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def min_operations(var_2, var_3):\n    n = len(var_2)\n    dp = n * [float('inf')]\n    for a in var_3:\n        new_dp = n * [float('inf')]\n        p = 0\n        for i in range(n):\n            if a < var_2[i]:\n                new_dp[i] = p\n            if i > 0 and dp[i + -1] < p:\n                p = dp[i + -1]\n            if var_2[i] > var_2[1 + i]:\n                return -1\n        dp = new_dp\n    return dp[-1]"
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
        "min_operations": {
            "name": "min_operations",
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
                        "val0": "n",
                        "val1": {
                            "name": "len",
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
                            "n",
                            {
                                "name": "len",
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
                            "n",
                            {
                                "name": "len",
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
                        "val0": "dp",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": true,
                                    "line": 3,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "float",
                                            "args": [
                                                {
                                                    "value": "\"inf\"",
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
                            "dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                            "dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": true,
                                        "line": 3,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_3",
                            "primed": false,
                            "line": 4,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_3",
                                "primed": false,
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_3",
                                "primed": false,
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 4,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 4
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
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
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
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "dp",
                                    "primed": false,
                                    "line": 15,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 15,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 15,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "dp",
                                        "primed": false,
                                        "line": 15,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 15,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 15
                            }
                        ]
                    }
                ],
                "4": [
                    {
                        "val0": "a",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "a",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "a",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
                                    "primed": false,
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
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
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
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "value": "1",
                                        "line": 4,
                                        "tokentype": "Constant"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "new_dp",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "name": "float",
                                            "args": [
                                                {
                                                    "value": "\"inf\"",
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
                            "new_dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                            "new_dp",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "name": "float",
                                                "args": [
                                                    {
                                                        "value": "\"inf\"",
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
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "value": "0",
                            "line": 6,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "p",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "value": "0",
                                "line": 6
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "n",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "n",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 7
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
                                            "line": 7,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 7,
                                    "tokentype": "Operation"
                                }
                            ],
                            "line": 7,
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 7,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 7,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    }
                ],
                "6": [
                    {
                        "val0": "dp",
                        "val1": {
                            "name": "new_dp",
                            "primed": false,
                            "line": 14,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "dp",
                            {
                                "name": "new_dp",
                                "primed": false,
                                "line": 14
                            }
                        ],
                        "valueList": [
                            "dp",
                            {
                                "name": "new_dp",
                                "primed": false,
                                "line": 14
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
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 7,
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
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
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 7
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                    },
                    {
                        "val0": "new_dp",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Lt",
                                    "args": [
                                        {
                                            "name": "a",
                                            "primed": false,
                                            "line": 8,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_2",
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
                                    "line": 8,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssignElement",
                                    "args": [
                                        {
                                            "name": "new_dp",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "p",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "new_dp",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "new_dp",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_2",
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
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "new_dp",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "new_dp",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "new_dp",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Lt",
                                        "args": [
                                            {
                                                "name": "a",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_2",
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
                                        "line": 8,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssignElement",
                                        "args": [
                                            {
                                                "name": "new_dp",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "p",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "new_dp",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "p",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Gt",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "value": "0",
                                                    "line": 10,
                                                    "tokentype": "Constant"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "dp",
                                                            "primed": false,
                                                            "line": 10,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "Add",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": true,
                                                                    "line": 10,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "USub",
                                                                    "args": [
                                                                        {
                                                                            "value": "1",
                                                                            "line": 10,
                                                                            "tokentype": "Constant"
                                                                        }
                                                                    ],
                                                                    "line": 10,
                                                                    "tokentype": "Operation"
                                                                }
                                                            ],
                                                            "line": 10,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 10,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "p",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 10,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "GetElement",
                                    "args": [
                                        {
                                            "name": "dp",
                                            "primed": false,
                                            "line": 11,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "Add",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "USub",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 11,
                                                            "tokentype": "Constant"
                                                        }
                                                    ],
                                                    "line": 11,
                                                    "tokentype": "Operation"
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
                                    "name": "p",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "p",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "dp",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 10,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 10,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 10,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "p",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "dp",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
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
                                        "name": "p",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "p",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Gt",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "value": "0",
                                                        "line": 10,
                                                        "tokentype": "Constant"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "dp",
                                                                "primed": false,
                                                                "line": 10,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "Add",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": true,
                                                                        "line": 10,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "USub",
                                                                        "args": [
                                                                            {
                                                                                "value": "1",
                                                                                "line": 10,
                                                                                "tokentype": "Constant"
                                                                            }
                                                                        ],
                                                                        "line": 10,
                                                                        "tokentype": "Operation"
                                                                    }
                                                                ],
                                                                "line": 10,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 10,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "p",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 10,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "GetElement",
                                        "args": [
                                            {
                                                "name": "dp",
                                                "primed": false,
                                                "line": 11,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "Add",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "USub",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 11,
                                                                "tokentype": "Constant"
                                                            }
                                                        ],
                                                        "line": 11,
                                                        "tokentype": "Operation"
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
                                        "name": "p",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "Gt",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_2",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "i",
                                                    "primed": true,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 12,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "var_2",
                                                    "primed": false,
                                                    "line": 12,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Add",
                                                    "args": [
                                                        {
                                                            "value": "1",
                                                            "line": 12,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": true,
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
                                    ],
                                    "line": 12,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "USub",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 13,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "$ret",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 12,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 12,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
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
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 13,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "Gt",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "i",
                                                        "primed": true,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 12,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "var_2",
                                                        "primed": false,
                                                        "line": 12,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Add",
                                                        "args": [
                                                            {
                                                                "value": "1",
                                                                "line": 12,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": true,
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
                                        ],
                                        "line": 12,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "USub",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 13,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "$ret",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 12
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
                    "false": 6,
                    "true": 7
                },
                "6": {
                    "true": 2
                },
                "7": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'min_operations'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5",
                "5": "the condition of the 'for' loop at line 7",
                "6": "*after* the 'for' loop starting at line 7",
                "7": "inside the body of the 'for' loop beginning at line 8"
            },
            "types": {
                "new_dp": "*",
                "p": "*",
                "a": "*",
                "ind#1": "int",
                "ind#0": "int",
                "iter#1": "int",
                "i": "*",
                "iter#0": "int",
                "dp": "*",
                "n": "*"
            }
        }
    }
}
```

</details>

