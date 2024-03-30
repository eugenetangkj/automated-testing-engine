# Test Report

Time: 2024-03-30 07:56:01.551839

### Base Program

```py
def xor_beauty(nums):
    n = len(nums)
    maxXOR = 1024
    counter = [0] * maxXOR
    
    for num in nums:
        counter[num % maxXOR] += 1
        
    xor_beauty = 0
    for i in range(maxXOR):
        for j in range(i, maxXOR):
            k = (i | j) & (~(i ^ j))
            if k < maxXOR and k >= j:
                count = counter[i] * counter[j] * (1 if i == j else 2)
                if k != i and k != j:
                    count *= counter[k]
                xor_beauty ^= count
                
    return xor_beauty
```

## Test Case 1

### Modified Program

```py
def xor_beauty(nums):
    n = len(nums)
    maxXOR = 1024
    counter = [0] * maxXOR
    for num in nums:
        counter[num % maxXOR] += 1
    xor_beauty = 0
    for i in range(maxXOR):
        for j in range(i, maxXOR):
            k = (i | j) & ~(i ^ j)
            if k < maxXOR and k >= j:
                count = counter[i] * counter[j] * (1 if i == j else 2)
                if k != i and k != j:
                    count *= counter[k]
                xor_beauty ^= count
    return xor_beauty
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def xor_beauty(nums):\n    n = len(nums)\n    maxXOR = 1024\n    counter = [0] * maxXOR\n    for num in nums:\n        counter[num % maxXOR] += 1\n    xor_beauty = 0\n    for i in range(maxXOR):\n        for j in range(i, maxXOR):\n            k = (i | j) & ~(i ^ j)\n            if k < maxXOR and k >= j:\n                count = counter[i] * counter[j] * (1 if i == j else 2)\n                if k != i and k != j:\n                    count *= counter[k]\n                xor_beauty ^= count\n    return xor_beauty"
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
        "xor_beauty": {
            "name": "xor_beauty",
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
                        "val0": "n",
                        "val1": {
                            "name": "len",
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
                            "n",
                            {
                                "name": "len",
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
                            "n",
                            {
                                "name": "len",
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
                        "val0": "maxXOR",
                        "val1": {
                            "value": "1024",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "maxXOR",
                            {
                                "value": "1024",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "maxXOR",
                            {
                                "value": "1024",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "counter",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "maxXOR",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "counter",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "counter",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "nums",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 5
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
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                    }
                ],
                "3": [
                    {
                        "val0": "xor_beauty",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "xor_beauty",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "xor_beauty",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "maxXOR",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "maxXOR",
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
                "4": [
                    {
                        "val0": "num",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                    },
                    {
                        "val0": "counter",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "counter",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "num",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "maxXOR",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "counter",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Mod",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "maxXOR",
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
                            "counter",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "counter",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "maxXOR",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "counter",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "maxXOR",
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
                            "counter",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "counter",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "maxXOR",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "counter",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "maxXOR",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "xor_beauty",
                            "primed": false,
                            "line": 16,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "xor_beauty",
                                "primed": false,
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "xor_beauty",
                                "primed": false,
                                "line": 16
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
                            "i",
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
                            "i",
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
                    },
                    {
                        "val0": "iter#2",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "maxXOR",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#2",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "iter#2",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "value": "0",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#2",
                                            "primed": false,
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
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "9": [],
                "10": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "j",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#2",
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
                        "valueArray": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
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
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
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
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "k",
                        "val1": {
                            "name": "BitAnd",
                            "args": [
                                {
                                    "name": "BitOr",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "j",
                                            "primed": true,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Invert",
                                    "args": [
                                        {
                                            "name": "BitXor",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
                                                    "primed": true,
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
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "k",
                            {
                                "name": "BitAnd",
                                "args": [
                                    {
                                        "name": "BitOr",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "j",
                                                "primed": true,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Invert",
                                        "args": [
                                            {
                                                "name": "BitXor",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "k",
                            {
                                "name": "BitAnd",
                                "args": [
                                    {
                                        "name": "BitOr",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "j",
                                                "primed": true,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Invert",
                                        "args": [
                                            {
                                                "name": "BitXor",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "maxXOR",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GtE",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "NotEq",
                                                    "args": [
                                                        {
                                                            "name": "k",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "NotEq",
                                                    "args": [
                                                        {
                                                            "name": "k",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 13,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Mult",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
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
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
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
                                                        },
                                                        {
                                                            "name": "ite",
                                                            "args": [
                                                                {
                                                                    "name": "Eq",
                                                                    "args": [
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
                                                                            "primed": true,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "1",
                                                                    "line": 12,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "value": "2",
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
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "counter",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "k",
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
                                        },
                                        {
                                            "name": "Mult",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
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
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
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
                                                },
                                                {
                                                    "name": "ite",
                                                    "args": [
                                                        {
                                                            "name": "Eq",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
                                                                    "primed": true,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 12,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "1",
                                                            "line": 12,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "value": "2",
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
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 13,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
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
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
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
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                    },
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 12,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 12,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "value": "2",
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
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 13,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
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
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
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
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                    },
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 12,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 12,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "value": "2",
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
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    },
                    {
                        "val0": "xor_beauty",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "maxXOR",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GtE",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "xor_beauty",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "ite",
                                            "args": [
                                                {
                                                    "name": "And",
                                                    "args": [
                                                        {
                                                            "name": "NotEq",
                                                            "args": [
                                                                {
                                                                    "name": "k",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 13,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "NotEq",
                                                            "args": [
                                                                {
                                                                    "name": "k",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 13,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "Mult",
                                                                    "args": [
                                                                        {
                                                                            "name": "GetElement",
                                                                            "args": [
                                                                                {
                                                                                    "name": "counter",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
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
                                                                                    "name": "counter",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "j",
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
                                                                },
                                                                {
                                                                    "name": "ite",
                                                                    "args": [
                                                                        {
                                                                            "name": "Eq",
                                                                            "args": [
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "j",
                                                                                    "primed": true,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 12,
                                                                            "tokentype": "Operation"
                                                                        },
                                                                        {
                                                                            "value": "1",
                                                                            "line": 12,
                                                                            "tokentype": "Constant"
                                                                        },
                                                                        {
                                                                            "value": "2",
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
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 14,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "k",
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
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
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
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
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
                                                        },
                                                        {
                                                            "name": "ite",
                                                            "args": [
                                                                {
                                                                    "name": "Eq",
                                                                    "args": [
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
                                                                            "primed": true,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "1",
                                                                    "line": 12,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "value": "2",
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
                                            "line": 13,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "xor_beauty",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "xor_beauty",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_beauty",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "ite",
                                                "args": [
                                                    {
                                                        "name": "And",
                                                        "args": [
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "Mult",
                                                                        "args": [
                                                                            {
                                                                                "name": "GetElement",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
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
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
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
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "k",
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
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
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
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                "line": 13,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "xor_beauty",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "xor_beauty",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_beauty",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "ite",
                                                "args": [
                                                    {
                                                        "name": "And",
                                                        "args": [
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "Mult",
                                                                        "args": [
                                                                            {
                                                                                "name": "GetElement",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
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
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
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
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "k",
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
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
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
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                "line": 13,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "xor_beauty",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
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
                "3": {
                    "true": 5
                },
                "4": {
                    "true": 2
                },
                "5": {
                    "false": 6,
                    "true": 7
                },
                "6": {},
                "7": {
                    "true": 8
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {
                    "true": 5
                },
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'xor_beauty'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6",
                "5": "the condition of the 'for' loop at line 8",
                "6": "*after* the 'for' loop starting at line 8",
                "7": "inside the body of the 'for' loop beginning at line 9",
                "8": "the condition of the 'for' loop at line 9",
                "9": "*after* the 'for' loop starting at line 9",
                "10": "inside the body of the 'for' loop beginning at line 10"
            },
            "types": {
                "num": "*",
                "xor_beauty": "*",
                "count": "*",
                "i": "*",
                "j": "*",
                "counter": "*",
                "k": "*",
                "n": "*",
                "ind#2": "int",
                "ind#1": "int",
                "ind#0": "int",
                "maxXOR": "*",
                "iter#2": "int",
                "iter#1": "int",
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
def xor_beauty(var_0):
    n = len(var_0)
    maxXOR = 1024
    counter = [0] * maxXOR
    for num in var_0:
        counter[num % maxXOR] += 1
    xor_beauty = 0
    for i in range(maxXOR):
        for j in range(i, maxXOR):
            k = (i | j) & ~(i ^ j)
            if k < maxXOR and k >= j:
                count = counter[i] * counter[j] * (1 if i == j else 2)
                if k != i and k != j:
                    count *= counter[k]
                xor_beauty ^= count
    return xor_beauty
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def xor_beauty(var_0):\n    n = len(var_0)\n    maxXOR = 1024\n    counter = [0] * maxXOR\n    for num in var_0:\n        counter[num % maxXOR] += 1\n    xor_beauty = 0\n    for i in range(maxXOR):\n        for j in range(i, maxXOR):\n            k = (i | j) & ~(i ^ j)\n            if k < maxXOR and k >= j:\n                count = counter[i] * counter[j] * (1 if i == j else 2)\n                if k != i and k != j:\n                    count *= counter[k]\n                xor_beauty ^= count\n    return xor_beauty"
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
        "xor_beauty": {
            "name": "xor_beauty",
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
                        "val0": "maxXOR",
                        "val1": {
                            "value": "1024",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "maxXOR",
                            {
                                "value": "1024",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "maxXOR",
                            {
                                "value": "1024",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "counter",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
                                            "line": 4,
                                            "tokentype": "Constant"
                                        }
                                    ],
                                    "line": 4,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "maxXOR",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 4,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "counter",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ],
                        "valueList": [
                            "counter",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
                                                "line": 4,
                                                "tokentype": "Constant"
                                            }
                                        ],
                                        "line": 4,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 4
                            }
                        ]
                    },
                    {
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_0",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_0",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_0",
                                "primed": false,
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 5
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
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                    }
                ],
                "3": [
                    {
                        "val0": "xor_beauty",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "xor_beauty",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "xor_beauty",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "maxXOR",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "maxXOR",
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
                "4": [
                    {
                        "val0": "num",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                    },
                    {
                        "val0": "counter",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "counter",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "num",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "maxXOR",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "counter",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Mod",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "maxXOR",
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
                            "counter",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "counter",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "maxXOR",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "counter",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "maxXOR",
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
                            "counter",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "counter",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "maxXOR",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "counter",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "maxXOR",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "xor_beauty",
                            "primed": false,
                            "line": 16,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "xor_beauty",
                                "primed": false,
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "xor_beauty",
                                "primed": false,
                                "line": 16
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
                            "i",
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
                            "i",
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
                    },
                    {
                        "val0": "iter#2",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "maxXOR",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#2",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "iter#2",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "value": "0",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#2",
                                            "primed": false,
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
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "9": [],
                "10": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "j",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#2",
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
                        "valueArray": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
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
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
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
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "k",
                        "val1": {
                            "name": "BitAnd",
                            "args": [
                                {
                                    "name": "BitOr",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "j",
                                            "primed": true,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Invert",
                                    "args": [
                                        {
                                            "name": "BitXor",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
                                                    "primed": true,
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
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "k",
                            {
                                "name": "BitAnd",
                                "args": [
                                    {
                                        "name": "BitOr",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "j",
                                                "primed": true,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Invert",
                                        "args": [
                                            {
                                                "name": "BitXor",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "k",
                            {
                                "name": "BitAnd",
                                "args": [
                                    {
                                        "name": "BitOr",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "j",
                                                "primed": true,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Invert",
                                        "args": [
                                            {
                                                "name": "BitXor",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "maxXOR",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GtE",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "NotEq",
                                                    "args": [
                                                        {
                                                            "name": "k",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "NotEq",
                                                    "args": [
                                                        {
                                                            "name": "k",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 13,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Mult",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
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
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
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
                                                        },
                                                        {
                                                            "name": "ite",
                                                            "args": [
                                                                {
                                                                    "name": "Eq",
                                                                    "args": [
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
                                                                            "primed": true,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "1",
                                                                    "line": 12,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "value": "2",
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
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "counter",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "k",
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
                                        },
                                        {
                                            "name": "Mult",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
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
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
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
                                                },
                                                {
                                                    "name": "ite",
                                                    "args": [
                                                        {
                                                            "name": "Eq",
                                                            "args": [
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
                                                                    "primed": true,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 12,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "value": "1",
                                                            "line": 12,
                                                            "tokentype": "Constant"
                                                        },
                                                        {
                                                            "value": "2",
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
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 13,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
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
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
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
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                    },
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 12,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 12,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "value": "2",
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
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 13,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
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
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
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
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                    },
                                                    {
                                                        "name": "ite",
                                                        "args": [
                                                            {
                                                                "name": "Eq",
                                                                "args": [
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 12,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "value": "1",
                                                                "line": 12,
                                                                "tokentype": "Constant"
                                                            },
                                                            {
                                                                "value": "2",
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
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    },
                    {
                        "val0": "xor_beauty",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "maxXOR",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GtE",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "xor_beauty",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "ite",
                                            "args": [
                                                {
                                                    "name": "And",
                                                    "args": [
                                                        {
                                                            "name": "NotEq",
                                                            "args": [
                                                                {
                                                                    "name": "k",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 13,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "NotEq",
                                                            "args": [
                                                                {
                                                                    "name": "k",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 13,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "Mult",
                                                                    "args": [
                                                                        {
                                                                            "name": "GetElement",
                                                                            "args": [
                                                                                {
                                                                                    "name": "counter",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
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
                                                                                    "name": "counter",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "j",
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
                                                                },
                                                                {
                                                                    "name": "ite",
                                                                    "args": [
                                                                        {
                                                                            "name": "Eq",
                                                                            "args": [
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "j",
                                                                                    "primed": true,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 12,
                                                                            "tokentype": "Operation"
                                                                        },
                                                                        {
                                                                            "value": "1",
                                                                            "line": 12,
                                                                            "tokentype": "Constant"
                                                                        },
                                                                        {
                                                                            "value": "2",
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
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 14,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "k",
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
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
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
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
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
                                                        },
                                                        {
                                                            "name": "ite",
                                                            "args": [
                                                                {
                                                                    "name": "Eq",
                                                                    "args": [
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
                                                                            "primed": true,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "1",
                                                                    "line": 12,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "value": "2",
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
                                            "line": 13,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "xor_beauty",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "xor_beauty",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_beauty",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "ite",
                                                "args": [
                                                    {
                                                        "name": "And",
                                                        "args": [
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "Mult",
                                                                        "args": [
                                                                            {
                                                                                "name": "GetElement",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
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
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
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
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "k",
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
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
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
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                "line": 13,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "xor_beauty",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "xor_beauty",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_beauty",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "ite",
                                                "args": [
                                                    {
                                                        "name": "And",
                                                        "args": [
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "Mult",
                                                                        "args": [
                                                                            {
                                                                                "name": "GetElement",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
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
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
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
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "k",
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
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
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
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                "line": 13,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "xor_beauty",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
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
                "3": {
                    "true": 5
                },
                "4": {
                    "true": 2
                },
                "5": {
                    "false": 6,
                    "true": 7
                },
                "6": {},
                "7": {
                    "true": 8
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {
                    "true": 5
                },
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'xor_beauty'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6",
                "5": "the condition of the 'for' loop at line 8",
                "6": "*after* the 'for' loop starting at line 8",
                "7": "inside the body of the 'for' loop beginning at line 9",
                "8": "the condition of the 'for' loop at line 9",
                "9": "*after* the 'for' loop starting at line 9",
                "10": "inside the body of the 'for' loop beginning at line 10"
            },
            "types": {
                "num": "*",
                "xor_beauty": "*",
                "count": "*",
                "i": "*",
                "j": "*",
                "counter": "*",
                "k": "*",
                "n": "*",
                "ind#2": "int",
                "ind#1": "int",
                "ind#0": "int",
                "maxXOR": "*",
                "iter#2": "int",
                "iter#1": "int",
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
def xor_beauty(nums):
    n = len(nums)
    maxXOR = 1024
    counter = maxXOR * [0]
    for num in nums:
        counter[num % maxXOR] += 1
    xor_beauty = 0
    for i in range(maxXOR):
        for j in range(i, maxXOR):
            k = (i | j) & ~(i ^ j)
            if k < maxXOR and k >= j:
                count = counter[i] * (1 if i == j else 2) * counter[j]
                if k != i and k != j:
                    count *= counter[k]
                xor_beauty ^= count
    return xor_beauty
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def xor_beauty(nums):\n    n = len(nums)\n    maxXOR = 1024\n    counter = maxXOR * [0]\n    for num in nums:\n        counter[num % maxXOR] += 1\n    xor_beauty = 0\n    for i in range(maxXOR):\n        for j in range(i, maxXOR):\n            k = (i | j) & ~(i ^ j)\n            if k < maxXOR and k >= j:\n                count = counter[i] * (1 if i == j else 2) * counter[j]\n                if k != i and k != j:\n                    count *= counter[k]\n                xor_beauty ^= count\n    return xor_beauty"
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
        "xor_beauty": {
            "name": "xor_beauty",
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
                        "val0": "n",
                        "val1": {
                            "name": "len",
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
                            "n",
                            {
                                "name": "len",
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
                            "n",
                            {
                                "name": "len",
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
                        "val0": "maxXOR",
                        "val1": {
                            "value": "1024",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "maxXOR",
                            {
                                "value": "1024",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "maxXOR",
                            {
                                "value": "1024",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "counter",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "maxXOR",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
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
                            "counter",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "maxXOR",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
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
                            "counter",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "maxXOR",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "nums",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "nums",
                                "primed": false,
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 5
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
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                    }
                ],
                "3": [
                    {
                        "val0": "xor_beauty",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "xor_beauty",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "xor_beauty",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "maxXOR",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "maxXOR",
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
                "4": [
                    {
                        "val0": "num",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                    },
                    {
                        "val0": "counter",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "counter",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "num",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "maxXOR",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "counter",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Mod",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "maxXOR",
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
                            "counter",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "counter",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "maxXOR",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "counter",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "maxXOR",
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
                            "counter",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "counter",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "maxXOR",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "counter",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "maxXOR",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "xor_beauty",
                            "primed": false,
                            "line": 16,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "xor_beauty",
                                "primed": false,
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "xor_beauty",
                                "primed": false,
                                "line": 16
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
                            "i",
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
                            "i",
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
                    },
                    {
                        "val0": "iter#2",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "maxXOR",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#2",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "iter#2",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "value": "0",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#2",
                                            "primed": false,
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
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "9": [],
                "10": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "j",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#2",
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
                        "valueArray": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
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
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
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
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "k",
                        "val1": {
                            "name": "BitAnd",
                            "args": [
                                {
                                    "name": "BitOr",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "j",
                                            "primed": true,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Invert",
                                    "args": [
                                        {
                                            "name": "BitXor",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
                                                    "primed": true,
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
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "k",
                            {
                                "name": "BitAnd",
                                "args": [
                                    {
                                        "name": "BitOr",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "j",
                                                "primed": true,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Invert",
                                        "args": [
                                            {
                                                "name": "BitXor",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "k",
                            {
                                "name": "BitAnd",
                                "args": [
                                    {
                                        "name": "BitOr",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "j",
                                                "primed": true,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Invert",
                                        "args": [
                                            {
                                                "name": "BitXor",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "maxXOR",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GtE",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "NotEq",
                                                    "args": [
                                                        {
                                                            "name": "k",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "NotEq",
                                                    "args": [
                                                        {
                                                            "name": "k",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 13,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Mult",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "name": "ite",
                                                                    "args": [
                                                                        {
                                                                            "name": "Eq",
                                                                            "args": [
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "j",
                                                                                    "primed": true,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 12,
                                                                            "tokentype": "Operation"
                                                                        },
                                                                        {
                                                                            "value": "1",
                                                                            "line": 12,
                                                                            "tokentype": "Constant"
                                                                        },
                                                                        {
                                                                            "value": "2",
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
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
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
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "counter",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "k",
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
                                        },
                                        {
                                            "name": "Mult",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 12,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "ite",
                                                            "args": [
                                                                {
                                                                    "name": "Eq",
                                                                    "args": [
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
                                                                            "primed": true,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "1",
                                                                    "line": 12,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "value": "2",
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
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "counter",
                                                            "primed": false,
                                                            "line": 12,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
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
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 13,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 12,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 12,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 13,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 12,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 12,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    },
                    {
                        "val0": "xor_beauty",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "maxXOR",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GtE",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "xor_beauty",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "ite",
                                            "args": [
                                                {
                                                    "name": "And",
                                                    "args": [
                                                        {
                                                            "name": "NotEq",
                                                            "args": [
                                                                {
                                                                    "name": "k",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 13,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "NotEq",
                                                            "args": [
                                                                {
                                                                    "name": "k",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 13,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "Mult",
                                                                    "args": [
                                                                        {
                                                                            "name": "GetElement",
                                                                            "args": [
                                                                                {
                                                                                    "name": "counter",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 12,
                                                                            "tokentype": "Operation"
                                                                        },
                                                                        {
                                                                            "name": "ite",
                                                                            "args": [
                                                                                {
                                                                                    "name": "Eq",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "i",
                                                                                            "primed": false,
                                                                                            "line": 12,
                                                                                            "tokentype": "Variable"
                                                                                        },
                                                                                        {
                                                                                            "name": "j",
                                                                                            "primed": true,
                                                                                            "line": 12,
                                                                                            "tokentype": "Variable"
                                                                                        }
                                                                                    ],
                                                                                    "line": 12,
                                                                                    "tokentype": "Operation"
                                                                                },
                                                                                {
                                                                                    "value": "1",
                                                                                    "line": 12,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "value": "2",
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
                                                                },
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
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
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 14,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "k",
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
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "name": "ite",
                                                                    "args": [
                                                                        {
                                                                            "name": "Eq",
                                                                            "args": [
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "j",
                                                                                    "primed": true,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 12,
                                                                            "tokentype": "Operation"
                                                                        },
                                                                        {
                                                                            "value": "1",
                                                                            "line": 12,
                                                                            "tokentype": "Constant"
                                                                        },
                                                                        {
                                                                            "value": "2",
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
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
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
                                            "line": 13,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "xor_beauty",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "xor_beauty",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_beauty",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "ite",
                                                "args": [
                                                    {
                                                        "name": "And",
                                                        "args": [
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "Mult",
                                                                        "args": [
                                                                            {
                                                                                "name": "GetElement",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "name": "ite",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "Eq",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "i",
                                                                                                "primed": false,
                                                                                                "line": 12,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "j",
                                                                                                "primed": true,
                                                                                                "line": 12,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 12,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "value": "1",
                                                                                        "line": 12,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "2",
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
                                                                    },
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "k",
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
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                "line": 13,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "xor_beauty",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "xor_beauty",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_beauty",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "ite",
                                                "args": [
                                                    {
                                                        "name": "And",
                                                        "args": [
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "Mult",
                                                                        "args": [
                                                                            {
                                                                                "name": "GetElement",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "name": "ite",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "Eq",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "i",
                                                                                                "primed": false,
                                                                                                "line": 12,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "j",
                                                                                                "primed": true,
                                                                                                "line": 12,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 12,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "value": "1",
                                                                                        "line": 12,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "2",
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
                                                                    },
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "k",
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
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                "line": 13,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "xor_beauty",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
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
                "3": {
                    "true": 5
                },
                "4": {
                    "true": 2
                },
                "5": {
                    "false": 6,
                    "true": 7
                },
                "6": {},
                "7": {
                    "true": 8
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {
                    "true": 5
                },
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'xor_beauty'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6",
                "5": "the condition of the 'for' loop at line 8",
                "6": "*after* the 'for' loop starting at line 8",
                "7": "inside the body of the 'for' loop beginning at line 9",
                "8": "the condition of the 'for' loop at line 9",
                "9": "*after* the 'for' loop starting at line 9",
                "10": "inside the body of the 'for' loop beginning at line 10"
            },
            "types": {
                "num": "*",
                "xor_beauty": "*",
                "count": "*",
                "i": "*",
                "j": "*",
                "counter": "*",
                "k": "*",
                "n": "*",
                "ind#2": "int",
                "ind#1": "int",
                "ind#0": "int",
                "maxXOR": "*",
                "iter#2": "int",
                "iter#1": "int",
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
def xor_beauty(var_1):
    n = len(var_1)
    maxXOR = 1024
    counter = maxXOR * [0]
    for num in var_1:
        counter[num % maxXOR] += 1
    xor_beauty = 0
    for i in range(maxXOR):
        for j in range(i, maxXOR):
            k = (i | j) & ~(i ^ j)
            if k < maxXOR and k >= j:
                count = counter[i] * (1 if i == j else 2) * counter[j]
                if k != i and k != j:
                    count *= counter[k]
                xor_beauty ^= count
    return xor_beauty
```

<details>
<summary>parser endpoint: passed ✅</summary>

Request Body: 
```json
{
    "language": "py",
    "source_code": "def xor_beauty(var_1):\n    n = len(var_1)\n    maxXOR = 1024\n    counter = maxXOR * [0]\n    for num in var_1:\n        counter[num % maxXOR] += 1\n    xor_beauty = 0\n    for i in range(maxXOR):\n        for j in range(i, maxXOR):\n            k = (i | j) & ~(i ^ j)\n            if k < maxXOR and k >= j:\n                count = counter[i] * (1 if i == j else 2) * counter[j]\n                if k != i and k != j:\n                    count *= counter[k]\n                xor_beauty ^= count\n    return xor_beauty"
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
        "xor_beauty": {
            "name": "xor_beauty",
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
                        "val0": "n",
                        "val1": {
                            "name": "len",
                            "args": [
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
                        "valueArray": [
                            "n",
                            {
                                "name": "len",
                                "args": [
                                    {
                                        "name": "var_1",
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
                                        "name": "var_1",
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
                        "val0": "maxXOR",
                        "val1": {
                            "value": "1024",
                            "line": 3,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "maxXOR",
                            {
                                "value": "1024",
                                "line": 3
                            }
                        ],
                        "valueList": [
                            "maxXOR",
                            {
                                "value": "1024",
                                "line": 3
                            }
                        ]
                    },
                    {
                        "val0": "counter",
                        "val1": {
                            "name": "Mult",
                            "args": [
                                {
                                    "name": "maxXOR",
                                    "primed": true,
                                    "line": 4,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ListInit",
                                    "args": [
                                        {
                                            "value": "0",
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
                            "counter",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "maxXOR",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
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
                            "counter",
                            {
                                "name": "Mult",
                                "args": [
                                    {
                                        "name": "maxXOR",
                                        "primed": true,
                                        "line": 4,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ListInit",
                                        "args": [
                                            {
                                                "value": "0",
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
                        "val0": "iter#0",
                        "val1": {
                            "name": "var_1",
                            "primed": false,
                            "line": 5,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "iter#0",
                            {
                                "name": "var_1",
                                "primed": false,
                                "line": 5
                            }
                        ]
                    },
                    {
                        "val0": "ind#0",
                        "val1": {
                            "value": "0",
                            "line": 5,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 5
                            }
                        ],
                        "valueList": [
                            "ind#0",
                            {
                                "value": "0",
                                "line": 5
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
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#0",
                                            "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#0",
                                                "primed": false,
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
                    }
                ],
                "3": [
                    {
                        "val0": "xor_beauty",
                        "val1": {
                            "value": "0",
                            "line": 7,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "xor_beauty",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ],
                        "valueList": [
                            "xor_beauty",
                            {
                                "value": "0",
                                "line": 7
                            }
                        ]
                    },
                    {
                        "val0": "iter#1",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "maxXOR",
                                    "primed": false,
                                    "line": 8,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 8,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 8,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 8
                            }
                        ],
                        "valueList": [
                            "iter#1",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "maxXOR",
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
                "4": [
                    {
                        "val0": "num",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#0",
                                    "primed": false,
                                    "line": 5,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 5,
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
                                        "primed": false,
                                        "line": 5,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 5
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
                                        "line": 5,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#0",
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
                        "val0": "ind#0",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                            "ind#0",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#0",
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
                    },
                    {
                        "val0": "counter",
                        "val1": {
                            "name": "AssignElement",
                            "args": [
                                {
                                    "name": "counter",
                                    "primed": false,
                                    "line": 6,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "Mod",
                                    "args": [
                                        {
                                            "name": "num",
                                            "primed": true,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "maxXOR",
                                            "primed": false,
                                            "line": 6,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 6,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "AssAdd",
                                    "args": [
                                        {
                                            "name": "GetElement",
                                            "args": [
                                                {
                                                    "name": "counter",
                                                    "primed": false,
                                                    "line": 6,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "Mod",
                                                    "args": [
                                                        {
                                                            "name": "num",
                                                            "primed": true,
                                                            "line": 6,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "maxXOR",
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
                            "counter",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "counter",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "maxXOR",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "counter",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "maxXOR",
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
                            "counter",
                            {
                                "name": "AssignElement",
                                "args": [
                                    {
                                        "name": "counter",
                                        "primed": false,
                                        "line": 6,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "Mod",
                                        "args": [
                                            {
                                                "name": "num",
                                                "primed": true,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "maxXOR",
                                                "primed": false,
                                                "line": 6,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 6,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "AssAdd",
                                        "args": [
                                            {
                                                "name": "GetElement",
                                                "args": [
                                                    {
                                                        "name": "counter",
                                                        "primed": false,
                                                        "line": 6,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "Mod",
                                                        "args": [
                                                            {
                                                                "name": "num",
                                                                "primed": true,
                                                                "line": 6,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "maxXOR",
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
                "6": [
                    {
                        "val0": "$ret",
                        "val1": {
                            "name": "xor_beauty",
                            "primed": false,
                            "line": 16,
                            "tokentype": "Variable"
                        },
                        "valueArray": [
                            "$ret",
                            {
                                "name": "xor_beauty",
                                "primed": false,
                                "line": 16
                            }
                        ],
                        "valueList": [
                            "$ret",
                            {
                                "name": "xor_beauty",
                                "primed": false,
                                "line": 16
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
                            "i",
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
                            "i",
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
                    },
                    {
                        "val0": "iter#2",
                        "val1": {
                            "name": "range",
                            "args": [
                                {
                                    "name": "i",
                                    "primed": true,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "maxXOR",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "iter#2",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "iter#2",
                            {
                                "name": "range",
                                "args": [
                                    {
                                        "name": "i",
                                        "primed": true,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "maxXOR",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "value": "0",
                            "line": 9,
                            "tokentype": "Constant"
                        },
                        "valueArray": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "value": "0",
                                "line": 9
                            }
                        ]
                    }
                ],
                "8": [
                    {
                        "val0": "$cond",
                        "val1": {
                            "name": "Lt",
                            "args": [
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "len",
                                    "args": [
                                        {
                                            "name": "iter#2",
                                            "primed": false,
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
                        },
                        "valueArray": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "$cond",
                            {
                                "name": "Lt",
                                "args": [
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "len",
                                        "args": [
                                            {
                                                "name": "iter#2",
                                                "primed": false,
                                                "line": 9,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 9,
                                        "tokentype": "Operation"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    }
                ],
                "9": [],
                "10": [
                    {
                        "val0": "j",
                        "val1": {
                            "name": "GetElement",
                            "args": [
                                {
                                    "name": "iter#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                },
                                {
                                    "name": "ind#2",
                                    "primed": false,
                                    "line": 9,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 9,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "j",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "j",
                            {
                                "name": "GetElement",
                                "args": [
                                    {
                                        "name": "iter#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    },
                                    {
                                        "name": "ind#2",
                                        "primed": false,
                                        "line": 9,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "ind#2",
                        "val1": {
                            "name": "Add",
                            "args": [
                                {
                                    "name": "ind#2",
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
                        "valueArray": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
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
                                "line": 9
                            }
                        ],
                        "valueList": [
                            "ind#2",
                            {
                                "name": "Add",
                                "args": [
                                    {
                                        "name": "ind#2",
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
                                "line": 9
                            }
                        ]
                    },
                    {
                        "val0": "k",
                        "val1": {
                            "name": "BitAnd",
                            "args": [
                                {
                                    "name": "BitOr",
                                    "args": [
                                        {
                                            "name": "i",
                                            "primed": false,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "j",
                                            "primed": true,
                                            "line": 10,
                                            "tokentype": "Variable"
                                        }
                                    ],
                                    "line": 10,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "Invert",
                                    "args": [
                                        {
                                            "name": "BitXor",
                                            "args": [
                                                {
                                                    "name": "i",
                                                    "primed": false,
                                                    "line": 10,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
                                                    "primed": true,
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
                                }
                            ],
                            "line": 10,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "k",
                            {
                                "name": "BitAnd",
                                "args": [
                                    {
                                        "name": "BitOr",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "j",
                                                "primed": true,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Invert",
                                        "args": [
                                            {
                                                "name": "BitXor",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 10
                            }
                        ],
                        "valueList": [
                            "k",
                            {
                                "name": "BitAnd",
                                "args": [
                                    {
                                        "name": "BitOr",
                                        "args": [
                                            {
                                                "name": "i",
                                                "primed": false,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "j",
                                                "primed": true,
                                                "line": 10,
                                                "tokentype": "Variable"
                                            }
                                        ],
                                        "line": 10,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "Invert",
                                        "args": [
                                            {
                                                "name": "BitXor",
                                                "args": [
                                                    {
                                                        "name": "i",
                                                        "primed": false,
                                                        "line": 10,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
                                                        "primed": true,
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
                                    }
                                ],
                                "line": 10
                            }
                        ]
                    },
                    {
                        "val0": "count",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "maxXOR",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GtE",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "ite",
                                    "args": [
                                        {
                                            "name": "And",
                                            "args": [
                                                {
                                                    "name": "NotEq",
                                                    "args": [
                                                        {
                                                            "name": "k",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "i",
                                                            "primed": false,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "NotEq",
                                                    "args": [
                                                        {
                                                            "name": "k",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
                                                            "primed": true,
                                                            "line": 13,
                                                            "tokentype": "Variable"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                }
                                            ],
                                            "line": 13,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "Mult",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "name": "ite",
                                                                    "args": [
                                                                        {
                                                                            "name": "Eq",
                                                                            "args": [
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "j",
                                                                                    "primed": true,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 12,
                                                                            "tokentype": "Operation"
                                                                        },
                                                                        {
                                                                            "value": "1",
                                                                            "line": 12,
                                                                            "tokentype": "Constant"
                                                                        },
                                                                        {
                                                                            "value": "2",
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
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
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
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "counter",
                                                            "primed": false,
                                                            "line": 14,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "k",
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
                                        },
                                        {
                                            "name": "Mult",
                                            "args": [
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 12,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "ite",
                                                            "args": [
                                                                {
                                                                    "name": "Eq",
                                                                    "args": [
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
                                                                            "primed": true,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "value": "1",
                                                                    "line": 12,
                                                                    "tokentype": "Constant"
                                                                },
                                                                {
                                                                    "value": "2",
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
                                                },
                                                {
                                                    "name": "GetElement",
                                                    "args": [
                                                        {
                                                            "name": "counter",
                                                            "primed": false,
                                                            "line": 12,
                                                            "tokentype": "Variable"
                                                        },
                                                        {
                                                            "name": "j",
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
                                    "line": 13,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "count",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 13,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 12,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 12,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "count",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "ite",
                                        "args": [
                                            {
                                                "name": "And",
                                                "args": [
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "i",
                                                                "primed": false,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "NotEq",
                                                        "args": [
                                                            {
                                                                "name": "k",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
                                                                "primed": true,
                                                                "line": 13,
                                                                "tokentype": "Variable"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    }
                                                ],
                                                "line": 13,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 14,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "k",
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
                                            },
                                            {
                                                "name": "Mult",
                                                "args": [
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 12,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "ite",
                                                                "args": [
                                                                    {
                                                                        "name": "Eq",
                                                                        "args": [
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
                                                                                "primed": true,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "value": "1",
                                                                        "line": 12,
                                                                        "tokentype": "Constant"
                                                                    },
                                                                    {
                                                                        "value": "2",
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
                                                    },
                                                    {
                                                        "name": "GetElement",
                                                        "args": [
                                                            {
                                                                "name": "counter",
                                                                "primed": false,
                                                                "line": 12,
                                                                "tokentype": "Variable"
                                                            },
                                                            {
                                                                "name": "j",
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
                                        "line": 13,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "count",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ]
                    },
                    {
                        "val0": "xor_beauty",
                        "val1": {
                            "name": "ite",
                            "args": [
                                {
                                    "name": "And",
                                    "args": [
                                        {
                                            "name": "Lt",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "maxXOR",
                                                    "primed": false,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                }
                                            ],
                                            "line": 11,
                                            "tokentype": "Operation"
                                        },
                                        {
                                            "name": "GtE",
                                            "args": [
                                                {
                                                    "name": "k",
                                                    "primed": true,
                                                    "line": 11,
                                                    "tokentype": "Variable"
                                                },
                                                {
                                                    "name": "j",
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
                                    "name": "BitXor",
                                    "args": [
                                        {
                                            "name": "xor_beauty",
                                            "primed": false,
                                            "line": 15,
                                            "tokentype": "Variable"
                                        },
                                        {
                                            "name": "ite",
                                            "args": [
                                                {
                                                    "name": "And",
                                                    "args": [
                                                        {
                                                            "name": "NotEq",
                                                            "args": [
                                                                {
                                                                    "name": "k",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "i",
                                                                    "primed": false,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 13,
                                                            "tokentype": "Operation"
                                                        },
                                                        {
                                                            "name": "NotEq",
                                                            "args": [
                                                                {
                                                                    "name": "k",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
                                                                    "primed": true,
                                                                    "line": 13,
                                                                    "tokentype": "Variable"
                                                                }
                                                            ],
                                                            "line": 13,
                                                            "tokentype": "Operation"
                                                        }
                                                    ],
                                                    "line": 13,
                                                    "tokentype": "Operation"
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "Mult",
                                                                    "args": [
                                                                        {
                                                                            "name": "GetElement",
                                                                            "args": [
                                                                                {
                                                                                    "name": "counter",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 12,
                                                                            "tokentype": "Operation"
                                                                        },
                                                                        {
                                                                            "name": "ite",
                                                                            "args": [
                                                                                {
                                                                                    "name": "Eq",
                                                                                    "args": [
                                                                                        {
                                                                                            "name": "i",
                                                                                            "primed": false,
                                                                                            "line": 12,
                                                                                            "tokentype": "Variable"
                                                                                        },
                                                                                        {
                                                                                            "name": "j",
                                                                                            "primed": true,
                                                                                            "line": 12,
                                                                                            "tokentype": "Variable"
                                                                                        }
                                                                                    ],
                                                                                    "line": 12,
                                                                                    "tokentype": "Operation"
                                                                                },
                                                                                {
                                                                                    "value": "1",
                                                                                    "line": 12,
                                                                                    "tokentype": "Constant"
                                                                                },
                                                                                {
                                                                                    "value": "2",
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
                                                                },
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "j",
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
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 14,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "k",
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
                                                },
                                                {
                                                    "name": "Mult",
                                                    "args": [
                                                        {
                                                            "name": "Mult",
                                                            "args": [
                                                                {
                                                                    "name": "GetElement",
                                                                    "args": [
                                                                        {
                                                                            "name": "counter",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        },
                                                                        {
                                                                            "name": "i",
                                                                            "primed": false,
                                                                            "line": 12,
                                                                            "tokentype": "Variable"
                                                                        }
                                                                    ],
                                                                    "line": 12,
                                                                    "tokentype": "Operation"
                                                                },
                                                                {
                                                                    "name": "ite",
                                                                    "args": [
                                                                        {
                                                                            "name": "Eq",
                                                                            "args": [
                                                                                {
                                                                                    "name": "i",
                                                                                    "primed": false,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                },
                                                                                {
                                                                                    "name": "j",
                                                                                    "primed": true,
                                                                                    "line": 12,
                                                                                    "tokentype": "Variable"
                                                                                }
                                                                            ],
                                                                            "line": 12,
                                                                            "tokentype": "Operation"
                                                                        },
                                                                        {
                                                                            "value": "1",
                                                                            "line": 12,
                                                                            "tokentype": "Constant"
                                                                        },
                                                                        {
                                                                            "value": "2",
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
                                                        },
                                                        {
                                                            "name": "GetElement",
                                                            "args": [
                                                                {
                                                                    "name": "counter",
                                                                    "primed": false,
                                                                    "line": 12,
                                                                    "tokentype": "Variable"
                                                                },
                                                                {
                                                                    "name": "j",
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
                                            "line": 13,
                                            "tokentype": "Operation"
                                        }
                                    ],
                                    "line": 15,
                                    "tokentype": "Operation"
                                },
                                {
                                    "name": "xor_beauty",
                                    "primed": false,
                                    "line": 0,
                                    "tokentype": "Variable"
                                }
                            ],
                            "line": 11,
                            "tokentype": "Operation"
                        },
                        "valueArray": [
                            "xor_beauty",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_beauty",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "ite",
                                                "args": [
                                                    {
                                                        "name": "And",
                                                        "args": [
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "Mult",
                                                                        "args": [
                                                                            {
                                                                                "name": "GetElement",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "name": "ite",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "Eq",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "i",
                                                                                                "primed": false,
                                                                                                "line": 12,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "j",
                                                                                                "primed": true,
                                                                                                "line": 12,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 12,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "value": "1",
                                                                                        "line": 12,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "2",
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
                                                                    },
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "k",
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
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                "line": 13,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "xor_beauty",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
                            }
                        ],
                        "valueList": [
                            "xor_beauty",
                            {
                                "name": "ite",
                                "args": [
                                    {
                                        "name": "And",
                                        "args": [
                                            {
                                                "name": "Lt",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "maxXOR",
                                                        "primed": false,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    }
                                                ],
                                                "line": 11,
                                                "tokentype": "Operation"
                                            },
                                            {
                                                "name": "GtE",
                                                "args": [
                                                    {
                                                        "name": "k",
                                                        "primed": true,
                                                        "line": 11,
                                                        "tokentype": "Variable"
                                                    },
                                                    {
                                                        "name": "j",
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
                                        "name": "BitXor",
                                        "args": [
                                            {
                                                "name": "xor_beauty",
                                                "primed": false,
                                                "line": 15,
                                                "tokentype": "Variable"
                                            },
                                            {
                                                "name": "ite",
                                                "args": [
                                                    {
                                                        "name": "And",
                                                        "args": [
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "i",
                                                                        "primed": false,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            },
                                                            {
                                                                "name": "NotEq",
                                                                "args": [
                                                                    {
                                                                        "name": "k",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
                                                                        "primed": true,
                                                                        "line": 13,
                                                                        "tokentype": "Variable"
                                                                    }
                                                                ],
                                                                "line": 13,
                                                                "tokentype": "Operation"
                                                            }
                                                        ],
                                                        "line": 13,
                                                        "tokentype": "Operation"
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "Mult",
                                                                        "args": [
                                                                            {
                                                                                "name": "GetElement",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "counter",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "name": "ite",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "Eq",
                                                                                        "args": [
                                                                                            {
                                                                                                "name": "i",
                                                                                                "primed": false,
                                                                                                "line": 12,
                                                                                                "tokentype": "Variable"
                                                                                            },
                                                                                            {
                                                                                                "name": "j",
                                                                                                "primed": true,
                                                                                                "line": 12,
                                                                                                "tokentype": "Variable"
                                                                                            }
                                                                                        ],
                                                                                        "line": 12,
                                                                                        "tokentype": "Operation"
                                                                                    },
                                                                                    {
                                                                                        "value": "1",
                                                                                        "line": 12,
                                                                                        "tokentype": "Constant"
                                                                                    },
                                                                                    {
                                                                                        "value": "2",
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
                                                                    },
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "j",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 14,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "k",
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
                                                    },
                                                    {
                                                        "name": "Mult",
                                                        "args": [
                                                            {
                                                                "name": "Mult",
                                                                "args": [
                                                                    {
                                                                        "name": "GetElement",
                                                                        "args": [
                                                                            {
                                                                                "name": "counter",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            },
                                                                            {
                                                                                "name": "i",
                                                                                "primed": false,
                                                                                "line": 12,
                                                                                "tokentype": "Variable"
                                                                            }
                                                                        ],
                                                                        "line": 12,
                                                                        "tokentype": "Operation"
                                                                    },
                                                                    {
                                                                        "name": "ite",
                                                                        "args": [
                                                                            {
                                                                                "name": "Eq",
                                                                                "args": [
                                                                                    {
                                                                                        "name": "i",
                                                                                        "primed": false,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    },
                                                                                    {
                                                                                        "name": "j",
                                                                                        "primed": true,
                                                                                        "line": 12,
                                                                                        "tokentype": "Variable"
                                                                                    }
                                                                                ],
                                                                                "line": 12,
                                                                                "tokentype": "Operation"
                                                                            },
                                                                            {
                                                                                "value": "1",
                                                                                "line": 12,
                                                                                "tokentype": "Constant"
                                                                            },
                                                                            {
                                                                                "value": "2",
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
                                                            },
                                                            {
                                                                "name": "GetElement",
                                                                "args": [
                                                                    {
                                                                        "name": "counter",
                                                                        "primed": false,
                                                                        "line": 12,
                                                                        "tokentype": "Variable"
                                                                    },
                                                                    {
                                                                        "name": "j",
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
                                                "line": 13,
                                                "tokentype": "Operation"
                                            }
                                        ],
                                        "line": 15,
                                        "tokentype": "Operation"
                                    },
                                    {
                                        "name": "xor_beauty",
                                        "primed": false,
                                        "line": 0,
                                        "tokentype": "Variable"
                                    }
                                ],
                                "line": 11
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
                "3": {
                    "true": 5
                },
                "4": {
                    "true": 2
                },
                "5": {
                    "false": 6,
                    "true": 7
                },
                "6": {},
                "7": {
                    "true": 8
                },
                "8": {
                    "false": 9,
                    "true": 10
                },
                "9": {
                    "true": 5
                },
                "10": {
                    "true": 8
                }
            },
            "locdescs": {
                "1": "around the beginning of function 'xor_beauty'",
                "2": "the condition of the 'for' loop at line 5",
                "3": "*after* the 'for' loop starting at line 5",
                "4": "inside the body of the 'for' loop beginning at line 6",
                "5": "the condition of the 'for' loop at line 8",
                "6": "*after* the 'for' loop starting at line 8",
                "7": "inside the body of the 'for' loop beginning at line 9",
                "8": "the condition of the 'for' loop at line 9",
                "9": "*after* the 'for' loop starting at line 9",
                "10": "inside the body of the 'for' loop beginning at line 10"
            },
            "types": {
                "num": "*",
                "xor_beauty": "*",
                "count": "*",
                "i": "*",
                "j": "*",
                "counter": "*",
                "k": "*",
                "n": "*",
                "ind#2": "int",
                "ind#1": "int",
                "ind#0": "int",
                "maxXOR": "*",
                "iter#2": "int",
                "iter#1": "int",
                "iter#0": "int"
            }
        }
    }
}
```

</details>

