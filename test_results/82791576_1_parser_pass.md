# Test Report

Time: 2024-03-30 07:34:14.535621

### Base Program

```py
def findMaximumXOR(nums):
    max_xor = 0
    mask = 0

    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = {num & mask for num in nums}

        possible_max = max_xor | (1 << i)

        for prefix in prefixes:
            if prefix ^ possible_max in prefixes:
                max_xor = possible_max
                break

    return max_xor
```

## Test Case 1

### Modified Program

```py
def findMaximumXOR(nums):
    max_xor = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= 1 << i
        prefixes = {num & mask for num in nums}
        possible_max = max_xor | 1 << i
        for prefix in prefixes:
            if prefix ^ possible_max in prefixes:
                max_xor = possible_max
                break
    return max_xor
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findMaximumXOR(nums):\n    max_xor = 0\n    mask = 0\n    for i in range(31, -1, -1):\n        mask |= 1 << i\n        prefixes = {num & mask for num in nums}\n        possible_max = max_xor | 1 << i\n        for prefix in prefixes:\n            if prefix ^ possible_max in prefixes:\n                max_xor = possible_max\n                break\n    return max_xor"
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
        "findMaximumXOR": {
            "name": "findMaximumXOR",
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
                        "val0": "max_xor",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "max_xor",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "max_xor",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "mask",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "mask",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "mask",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "31",
                                    "line": 4,
                                    "tokentype": "Constant"
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
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "31",
                                        "line": 4,
                                        "tokentype": "Constant"
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
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "31",
                                        "line": 4,
                                        "tokentype": "Constant"
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
                            "name": "max_xor",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "max_xor",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "max_xor",
                                "primed": false,
                                "line": 12
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
                            "i",
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
                            "i",
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
                        "val0": "mask",
                        "val1": {
                            "name": "BitOr",
                            "args": [
                                {
                                    "name": "mask",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 5,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 5,
                                            "tokentype": "Variable"
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
                            "mask",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "mask",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
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
                            "mask",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "mask",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
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
                        "val0": "prefixes",
                        "val1": {
                            "name": "SetInit",
                            "args": [
                                {
                                    "name": "BitAnd",
                                    "args": [
                                        {
                                            "name": "num",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "mask",
                                            "primed": true,
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
                            "prefixes",
                            {
                                "name": "SetInit",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "mask",
                                                "primed": true,
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
                            "prefixes",
                            {
                                "name": "SetInit",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "mask",
                                                "primed": true,
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
                    },
                    {
                        "val0": "possible_max",
                        "val1": {
                            "name": "BitOr",
                            "args": [
                                {
                                    "name": "max_xor",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 7,
                                            "tokentype": "Constant"
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
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "possible_max",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "max_xor",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "possible_max",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "max_xor",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "prefixes",
                            "primed": true,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "prefixes",
                                "primed": true,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "prefixes",
                                "primed": true,
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 8
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
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
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
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "prefix",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "prefix",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "prefix",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "In",
                            "args": [
                                {
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "prefix",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "possible_max",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "prefixes",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "In",
                                "args": [
                                    {
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "prefix",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "possible_max",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "prefixes",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "In",
                                "args": [
                                    {
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "prefix",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "possible_max",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "prefixes",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "max_xor",
                        "val1": {
                            "name": "possible_max",
                            "primed": false,
                            "line": 10,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "max_xor",
                            {
                                "name": "possible_max",
                                "primed": false,
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "max_xor",
                            {
                                "name": "possible_max",
                                "primed": false,
                                "line": 10
                            }
                        ]
                    }
                ],
                "11": []
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
                    "true": 8
                },
                "8": {
                    "false": 11,
                    "true": 9
                },
                "9": {
                    "true": 6
                },
                "11": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'findMaximumXOR'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5",
                "5": "the condition of the 'for' loop at line 8",
                "6": "*after* the 'for' loop starting at line 8",
                "7": "inside the body of the 'for' loop beginning at line 9",
                "8": "the condition of the if-statement at line 9",
                "9": "inside the if-branch starting at line 10",
                "11": "after the if-statement beginning at line 9"
            },
            "types": {
                "prefixes": "*",
                "max_xor": "*",
                "possible_max": "*",
                "ind#1": "int",
                "prefix": "*",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "mask": "*"
            }
        }
    }
}
```

</details>

## Test Case 2

### Modified Program

```py
def findMaximumXOR(var_0):
    max_xor = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= 1 << i
        prefixes = {num & mask for num in var_0}
        possible_max = max_xor | 1 << i
        for prefix in prefixes:
            if prefix ^ possible_max in prefixes:
                max_xor = possible_max
                break
    return max_xor
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findMaximumXOR(var_0):\n    max_xor = 0\n    mask = 0\n    for i in range(31, -1, -1):\n        mask |= 1 << i\n        prefixes = {num & mask for num in var_0}\n        possible_max = max_xor | 1 << i\n        for prefix in prefixes:\n            if prefix ^ possible_max in prefixes:\n                max_xor = possible_max\n                break\n    return max_xor"
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
        "findMaximumXOR": {
            "name": "findMaximumXOR",
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
                        "val0": "max_xor",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "max_xor",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "max_xor",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "mask",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "mask",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "mask",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "31",
                                    "line": 4,
                                    "tokentype": "Constant"
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
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "31",
                                        "line": 4,
                                        "tokentype": "Constant"
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
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "31",
                                        "line": 4,
                                        "tokentype": "Constant"
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
                            "name": "max_xor",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "max_xor",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "max_xor",
                                "primed": false,
                                "line": 12
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
                            "i",
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
                            "i",
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
                        "val0": "mask",
                        "val1": {
                            "name": "BitOr",
                            "args": [
                                {
                                    "name": "mask",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 5,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 5,
                                            "tokentype": "Variable"
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
                            "mask",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "mask",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
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
                            "mask",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "mask",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
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
                        "val0": "prefixes",
                        "val1": {
                            "name": "SetInit",
                            "args": [
                                {
                                    "name": "BitAnd",
                                    "args": [
                                        {
                                            "name": "num",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "mask",
                                            "primed": true,
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
                            "prefixes",
                            {
                                "name": "SetInit",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "mask",
                                                "primed": true,
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
                            "prefixes",
                            {
                                "name": "SetInit",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "mask",
                                                "primed": true,
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
                    },
                    {
                        "val0": "possible_max",
                        "val1": {
                            "name": "BitOr",
                            "args": [
                                {
                                    "name": "max_xor",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 7,
                                            "tokentype": "Constant"
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
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "possible_max",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "max_xor",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "possible_max",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "max_xor",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "prefixes",
                            "primed": true,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "prefixes",
                                "primed": true,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "prefixes",
                                "primed": true,
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 8
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
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
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
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "prefix",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "prefix",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "prefix",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "In",
                            "args": [
                                {
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "prefix",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "possible_max",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "prefixes",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "In",
                                "args": [
                                    {
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "prefix",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "possible_max",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "prefixes",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "In",
                                "args": [
                                    {
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "prefix",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "possible_max",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "prefixes",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "max_xor",
                        "val1": {
                            "name": "possible_max",
                            "primed": false,
                            "line": 10,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "max_xor",
                            {
                                "name": "possible_max",
                                "primed": false,
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "max_xor",
                            {
                                "name": "possible_max",
                                "primed": false,
                                "line": 10
                            }
                        ]
                    }
                ],
                "11": []
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
                    "true": 8
                },
                "8": {
                    "false": 11,
                    "true": 9
                },
                "9": {
                    "true": 6
                },
                "11": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'findMaximumXOR'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5",
                "5": "the condition of the 'for' loop at line 8",
                "6": "*after* the 'for' loop starting at line 8",
                "7": "inside the body of the 'for' loop beginning at line 9",
                "8": "the condition of the if-statement at line 9",
                "9": "inside the if-branch starting at line 10",
                "11": "after the if-statement beginning at line 9"
            },
            "types": {
                "prefixes": "*",
                "max_xor": "*",
                "possible_max": "*",
                "ind#1": "int",
                "prefix": "*",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "mask": "*"
            }
        }
    }
}
```

</details>

## Test Case 3

### Modified Program

```py
def findMaximumXOR(var_1):
    max_xor = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= 1 << i
        prefixes = {num & mask for num in var_1}
        possible_max = max_xor | 1 << i
        for prefix in prefixes:
            if prefix ^ possible_max in prefixes:
                max_xor = possible_max
                break
    return max_xor
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def findMaximumXOR(var_1):\n    max_xor = 0\n    mask = 0\n    for i in range(31, -1, -1):\n        mask |= 1 << i\n        prefixes = {num & mask for num in var_1}\n        possible_max = max_xor | 1 << i\n        for prefix in prefixes:\n            if prefix ^ possible_max in prefixes:\n                max_xor = possible_max\n                break\n    return max_xor"
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
        "findMaximumXOR": {
            "name": "findMaximumXOR",
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
                        "val0": "max_xor",
                        "val1": {
                            "value": "0",
                            "line": 2,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "max_xor",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ],
                        "valueList": [
                            "max_xor",
                            {
                                "value": "0",
                                "line": 2
                            }
                        ]
                    },
                    {
                        "val0": "mask",
                        "val1": {
                            "value": "0",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "mask",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "mask",
                            {
                                "value": "0",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "value": "31",
                                    "line": 4,
                                    "tokentype": "Constant"
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
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "31",
                                        "line": 4,
                                        "tokentype": "Constant"
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
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "value": "31",
                                        "line": 4,
                                        "tokentype": "Constant"
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
                            "name": "max_xor",
                            "primed": false,
                            "line": 12,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "max_xor",
                                "primed": false,
                                "line": 12
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "max_xor",
                                "primed": false,
                                "line": 12
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
                            "i",
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
                            "i",
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
                        "val0": "mask",
                        "val1": {
                            "name": "BitOr",
                            "args": [
                                {
                                    "name": "mask",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 5,
                                            "tokentype": "Constant"
                                        },
                                        {
                                            "name": "i",
                                            "primed": true,
                                            "line": 5,
                                            "tokentype": "Variable"
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
                            "mask",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "mask",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
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
                            "mask",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "mask",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 5,
                                                "tokentype": "Constant"
                                            },
                                            {
                                                "name": "i",
                                                "primed": true,
                                                "line": 5,
                                                "tokentype": "Variable"
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
                        "val0": "prefixes",
                        "val1": {
                            "name": "SetInit",
                            "args": [
                                {
                                    "name": "BitAnd",
                                    "args": [
                                        {
                                            "name": "num",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "mask",
                                            "primed": true,
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
                            "prefixes",
                            {
                                "name": "SetInit",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "mask",
                                                "primed": true,
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
                            "prefixes",
                            {
                                "name": "SetInit",
                                "args": [
                                    {
                                        "name": "BitAnd",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "mask",
                                                "primed": true,
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
                    },
                    {
                        "val0": "possible_max",
                        "val1": {
                            "name": "BitOr",
                            "args": [
                                {
                                    "name": "max_xor",
                                    "primed": false,
                                    "line": 7,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "LShift",
                                    "args": [
                                        {
                                            "value": "1",
                                            "line": 7,
                                            "tokentype": "Constant"
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
                                }
                            ],
                            "line": 7,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "possible_max",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "max_xor",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                                    }
                                ],
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "possible_max",
                            {
                                "name": "BitOr",
                                "args": [
                                    {
                                        "name": "max_xor",
                                        "primed": false,
                                        "line": 7,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "LShift",
                                        "args": [
                                            {
                                                "value": "1",
                                                "line": 7,
                                                "tokentype": "Constant"
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
                                    }
                                ],
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "prefixes",
                            "primed": true,
                            "line": 8,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "prefixes",
                                "primed": true,
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "prefixes",
                                "primed": true,
                                "line": 8
                            }
                        ]
                    },
                    {
                        "val0": "ind#1",
                        "val1": {
                            "value": "0",
                            "line": 8,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "ind#1",
                            {
                                "value": "0",
                                "line": 8
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
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#1",
                                            "primed": false,
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
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
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
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#1",
                                                "primed": false,
                                                "line": 8,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 8,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 8
                            }
                        ]
                    }
                ],
                "6": [],
                "7": [
                    {
                        "val0": "prefix",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#1",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#1",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "prefix",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "prefix",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#1",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                            "ind#1",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#1",
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
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "In",
                            "args": [
                                {
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "prefix",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "possible_max",
                                            "primed": false,
                                            "line": 9,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 9,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "prefixes",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "In",
                                "args": [
                                    {
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "prefix",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "possible_max",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "prefixes",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "In",
                                "args": [
                                    {
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "prefix",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "possible_max",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "prefixes",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "9": [
                    {
                        "val0": "max_xor",
                        "val1": {
                            "name": "possible_max",
                            "primed": false,
                            "line": 10,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "max_xor",
                            {
                                "name": "possible_max",
                                "primed": false,
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "max_xor",
                            {
                                "name": "possible_max",
                                "primed": false,
                                "line": 10
                            }
                        ]
                    }
                ],
                "11": []
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
                    "true": 8
                },
                "8": {
                    "false": 11,
                    "true": 9
                },
                "9": {
                    "true": 6
                },
                "11": {
                    "true": 5
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'findMaximumXOR'",
                "2": "the condition of the 'for' loop at line 4",
                "3": "*after* the 'for' loop starting at line 4",
                "4": "inside the body of the 'for' loop beginning at line 5",
                "5": "the condition of the 'for' loop at line 8",
                "6": "*after* the 'for' loop starting at line 8",
                "7": "inside the body of the 'for' loop beginning at line 9",
                "8": "the condition of the if-statement at line 9",
                "9": "inside the if-branch starting at line 10",
                "11": "after the if-statement beginning at line 9"
            },
            "types": {
                "prefixes": "*",
                "max_xor": "*",
                "possible_max": "*",
                "ind#1": "int",
                "prefix": "*",
                "ind#0": "int",
                "i": "*",
                "iter#1": "int",
                "iter#0": "int",
                "mask": "*"
            }
        }
    }
}
```

</details>

